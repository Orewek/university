import math
from typing import Any

from MedianFrame import median_frame

import cv2 as cv

import matplotlib.pyplot as pltqwfe

import numpy as np

import pandas as pd

from scipy.interpolate import CubicSpline


class Detector:
    def __init__(self, x: int, y: int):
        self.detX = x
        self.detY = y
        # Список средних значений цвета для детектора
        self.avgColour = []
        # Список активаций детектора 0/1
        self.detections = []

    # Добавление среднего значения цвета для детектора
    def add_avg_colour_sum(self, value: int) -> None:
        self.avgColour.append(value)


drawing = True
# Переменные для хранения координат курсора мыши
mouseX, mouseY = -1, -1
# Высота детектора в пикселях
detector_height = 30
# Ширина детектора в пикселях
detector_width = 60

# Список полос
lanes = []
# Список детекторов
detectors = []
lanes_points = []

xs_lanes = []
cs_lanes = []


def set_spline(lanes: list) -> Any:
    x = []
    y = []
    for linePoint in lanes:
        x.append(linePoint[0])
        y.append(linePoint[1])
    cs = CubicSpline(x, y)
    xs = np.arange(x[0], x[len(x) - 1], width + 1)
    return xs, cs


def draw_detector(lane: list, colour_number: int) -> None:
    colours = [[0, 0, 255],
               [0, 255, 0],
               [255, 0, 0],
               [0, 0, 127],
               [0, 127, 0],
               [127, 0, 0]]
    for detector in lane:
        image = cv.rectangle(frame,
                             (int(detector.detX - width / 2),
                              int(detector.detY - heigth / 2)),
                             (int(detector.detX + width / 2), int(detector.detY + heigth / 2)),
                             colours[colour_number], 2)


linePoints = []
width = 60
heigth = 30


def sort_points(linePoints: list) -> list:
    return sorted(linePoints, key=lambda x: x[0])


def set_point(event: Any, x: int, y: int) -> None:
    global mouseX, mouseY, drawing
    colours = [[0, 0, 255],
               [0, 255, 0],
               [255, 0, 0],
               [0, 0, 127],
               [0, 127, 0],
               [127, 0, 0]]
    if event == cv.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv.putText(frame,
                   f'Lane  number: {str(len(lanes_points))}',
                   (50, 50 + 50 * len(lanes_points)),
                   cv.FONT_HERSHEY_SIMPLEX, 1,
                   colours[len(lanes_points)],
                   2,
                   cv.LINE_AA)
        image = cv.circle(frame, (mouseX, mouseY), 10, colours[len(lanes_points)], 2)
        linePoints.append((x, y))
        cv.imshow('Median frame', image)
        print(str(mouseX) + " " + str(mouseY))
        if cv.waitKeyEx(0) == ord('w'):
            lanes_points.append(linePoints.copy())
            linePoints.clear()
            print("lane added")


def set_detectors(xs_lanes: list, cs_lanes: list) -> list:
    i = 0
    for lane in xs_lanes:
        for point in lane:
            detectors.append(Detector(point, int(cs_lanes[i](point))))
        lanes.append(detectors.copy())
        detectors.clear()
        i += 1
    return lanes


def get_avg_colour_sum(gray: Any, detectors: list) -> None:
    """ Получение среднего значения цвета """
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                             int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        # считаем средние цвета для пикселей по горизонтали
        avg_color_per_row = np.average(detector_zone, axis=0)
        # считаем средний цвет для средних цветов по горизонтали
        avg_color = np.average(avg_color_per_row, axis=0)
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(avg_color)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


def get_avg_square_sum(gray, detectors):
    """ Получение среднего значения квадрата цвета """
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                             int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        sum_pow = 0
        h, w = detector_zone.shape
        for i in range(0, h):
            for j in range(0, w):
                sum_pow += math.pow(detector_zone[i, j], 2)
        sum_sqr_avg = math.sqrt(sum_pow) / detector_zone.size
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(sum_sqr_avg)
        # Выводм значение среднего цвета для детектора в консоль
        # print(avg_color)


def get_avg_diff_sum(gray: Any, previous_gray: Any, detectors: list) -> None:
    """ Получение среднего разницы цветов текущего и предыдущего кадров """
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                             int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        previous_detector_zone = previous_gray[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                                               int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        sum_pow = 0
        h, w = detector_zone.shape
        for i in range(0, h):
            for j in range(0, w):
                sum_pow += abs(detector_zone[i, j] - previous_detector_zone[i, j])
        sum_diff_avg = sum_pow / detector_zone.size
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(sum_diff_avg)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


def get_avg_median_sum(gray: Any, median: Any, detectors: list, eps: float) -> None:
    """ Получение среднего разницы цветов текущего и медианного кадров """
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                             int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        median_detector_zone = median[int((detector.detY - (heigth / 2))):int((detector.detY + (heigth / 2))),
                                      int((detector.detX - (width / 2))):int((detector.detX + (width / 2)))]
        sum = 0
        h, w = detector_zone.shape
        for i in range(0, h):
            for j in range(0, w):
                if (abs(detector_zone[i, j] - median_detector_zone[i, j]) / detector_zone[i, j]) * 100 > eps:
                    sum += 1
        sum_diff_avg = sum / detector_zone.size
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(sum_diff_avg)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


def detectors_discretization(detectors: list, frameCounter: int) -> None:
    """ Дискретизация активаций детекторов """
    # Значение разницы среднего цвета в % при котором будет проходить активация детектора
    activation_avg_colour_delta = 1.5
    # Задаем начальное значение активации всех детекторов на всех кадрах как 0
    for detector in detectors:
        detector.detections = [0] * frameCounter

    # Проходимся по всем кадрам детектора
    for i in range(0, len(detectors)):
        for j in range(0, frameCounter - 1):
            # Считаем текущую разницу среднего цвета между текущим и предыдущим кадрами
            current_avg_colour_delta = abs((detectors[i].avgColour[j] - detectors[i].avgColour[j + 1]) / detectors[i].avgColour[j]) * 100
            # Если разница больше заданной, то активируем детектор
            if current_avg_colour_delta > activation_avg_colour_delta:
                detectors[i].detections[j + 1] = 1


def detectors_discretization_filter(detectors: list, frameCounter: int) -> None:
    """ Фильтр для дискретизации активаций детекторов """
    frames_unite = 10  # Количество кадров на которые смотрим вперед от текущего
    # Проходим по всем детекторам полосы
    for i in range(0, len(detectors)):
        for j in range(0, frameCounter - 1):
            detector_activations_count = 0  # Счетчик активаций детектора
            # Смотрим на 1..frames_unite кадров вперед от текущего
            for k in range(1, frames_unite):
                # Если детектор активирован на текущем и 1..frames_unite кадре
                if (detectors[i].detections[j] == 1 and ((j + k) < (frameCounter - k - 1)) and (
                        detectors[i].detections[j + k] == 1)):
                    # Увеличиваем счетчик срабатываний детектора
                    detector_activations_count += 1
                # Вручную активируем детектор на detector_activations_count кадров от текущего
                for l in range(j, j + detector_activations_count):
                    detectors[i].detections[l] = 1

    #  Еще раз проходим по всем детекторам полосы
    for i in range(0, len(detectors)):
        # Смотрим значения активации детекторов для предыдущего и следующего кадров
        for j in range(0, frameCounter - 2):
            neighbours_sum = detectors[i].detections[j - 1] + detectors[i].detections[j + 1]
            # Если активации отсутствуют, то деактивируем детектор на текущем кадре
            if detectors[i].detections[j] == 1 and neighbours_sum == 0:
                detectors[i].detections[j] = 0


filename = "traffic2.mp4"
cap = cv.VideoCapture(filename)
if not cap.isOpened():
    print("Error opening file")

cv.namedWindow('Median frame', cv.WINDOW_NORMAL)
cv.resizeWindow('Median frame', 800, 600)
cv.setMouseCallback('Median frame', set_point)

frame = median_frame(filename)
median_frame = median_frame(filename)
median_gray = cv.cvtColor(median_frame, cv.COLOR_BGR2GRAY)
cv.imshow('Median frame', frame)
while 1:
    if cv.waitKeyEx(0) == ord('e'):
        break

for i in range(0, (len(lanes_points))):
    lanes_points[i] = sort_points(lanes_points[i])

for lane in lanes_points:
    xs, cs = set_spline(lane)
    xs_lanes.append(xs)
    cs_lanes.append(cs)

lanes = set_detectors(xs_lanes, cs_lanes)
frame_counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    colour_counter = 0
    for lane in lanes:
        draw_detector(lane, colour_counter)
        cv.imshow('Median frame', frame)
        colour_counter += 1
        get_avg_colour_sum(gray, lane)  # Метрика 1
        # get_avg_square_sum(gray, lane) # Метрика 2
        # if frame_counter!=0:
        # get_avg_diff_sum(gray, previous_gray,lane) # Метрика 3
        # get_avg_median_sum(gray, median_gray, lane, 1.5) # Метрика 4
    cv.imshow('Median frame', frame)
    frame_counter += 1
    previous_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

# Заполняем csv файл средними цветами с детекторов
data = dict()
lane_counter = 1
for lane in lanes:
    DETECTOR_NUMBER = 1
    for detector in lane:
        new_dict = {f'lane {str(lane_counter)} det {str(DETECTOR_NUMBER)}': detector.avgColour}
        data.update(new_dict)
        DETECTOR_NUMBER += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'AvgColours.csv', sep=';', index=False)
# Дискретизируем значения детектров
for lane in lanes:
    detectors_discretization(lane, frame_counter)

# Заполняем csv файл дискретными значениями с детекторов
data = dict()
lane_counter = 1
for lane in lanes:
    DETECTOR_NUMBER = 1
    for detector in lane:
        new_dict = {f'lane {str(lane_counter)} det {str(DETECTOR_NUMBER)}': detector.detections}
        data.update(new_dict)
        DETECTOR_NUMBER += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'RawDetections.csv', sep=';', index=False)

# Фильтруем дискретные значения детектров
for lane in lanes:
    detectors_discretization_filter(lane, frame_counter)

# Заполняем csv файл дискретными отфильтрованными значениями с детекторов
data = dict()
lane_counter = 1
for lane in lanes:
    DETECTOR_NUMBER = 1
    for detector in lane:
        new_dict = {"lane" + f'{str(lane_counter)} det{str(DETECTOR_NUMBER)}': detector.detections}
        data.update(new_dict)
        DETECTOR_NUMBER += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'FilteredDetections.csv', sep=';', index=False)
