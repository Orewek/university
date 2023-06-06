import math
import os
import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Список параметров для задания
drawing = True  # Включить визуализацию обработки
create_median_frame = False  # True - Создать медианный кадр перед началом обработки / False - взять в качестве
# медианного median_frame.png
set_detectors_by_hand = True  # True - Установка детекторов вручную / False - взять координаты детекторов из файла
# Coordinates.csv
metric = 1  # Выбранная метрика 1-4
detector_heigth = 20  # Высота детектора в пикселях
detector_width = 50  # Ширина детектора в пикселях
activation_avg_colour_delta = 1.75  # Значение разницы метрики в % при котором будет проходить активация детектора
frames_unite = 10  # Количество кадров, на которые смотрим вперед от текущего для их объединения
# Класс Детектор


class Detector:
    def __init__(self, x, y):
        self.detX = x  # Координата по x
        self.detY = y  # Координата по y
        self.avgColour = []  # Список средних значений цвета для детектора
        self.detections = []  # Список активаций детектора 0/1

    # Добавление среднего значения цвета для детектора
    def add_avg_colour_sum(self, value):
        self.avgColour.append(value)


mouseX, mouseY = -1, -1  # Переменные для хранения координат курсора мыши
lanes = []  # Список полос
detectors = []  # Список детекторов
lanes_points = []  # Список точек вдоль полосы для интерполяции функции расстановки детекторов
xs_lanes = []  # Координаты по оси x для расстановки детекторов вдоль полосы
cs_lanes = []  # Функции для расстановки детекторов вдоль полосы
linePoints = []  # Список точек вдоль полосы для интерполяции функции расстановки детекторов для всех полос


def set_spline(lanes):
    x = []
    y = []
    for linePoint in lanes:
        x.append(linePoint[0])
        y.append(linePoint[1])
    cs = CubicSpline(x, y)
    xs = np.arange(x[0], x[len(x) - 1], detector_width + 1)
    return xs, cs


def draw_detector(lane, colour_number):
    colours = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [0, 0, 127], [0, 127, 0], [127, 0, 0]]
    for detector in lane:
        image = cv.rectangle(frame, (int(detector.detX - detector_width / 2), int(detector.detY - detector_heigth / 2)),
                             (int(detector.detX + detector_width / 2), int(detector.detY + detector_heigth / 2)),
                             colours[colour_number], 2)


# Создание медианного кадра
def median_frame(filename):
    file_path = filename
    video = cv.VideoCapture(file_path)
    FOI = video.get(cv.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)
    frames = []
    for frameOI in FOI:
        video.set(cv.CAP_PROP_POS_FRAMES, frameOI)
        ret, frame = video.read()
        frames.append(frame)
    result = np.median(frames, axis=0).astype(dtype=np.uint8)
    return result


def sort_points(linePoints):
    return sorted(linePoints, key=lambda x: x[0])


def set_point(event, x, y, flags, param):
    global mouseX, mouseY, drawing
    colours = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [0, 0, 127], [0, 127, 0], [127, 0, 0]]
    if event == cv.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv.putText(median_frame, "Lane  number: " + str(len(lanes_points)), (50, 50 + 50 * len(lanes_points)),
                   cv.FONT_HERSHEY_SIMPLEX, 1, colours[len(lanes_points)], 2, cv.LINE_AA)
        image = cv.circle(median_frame, (mouseX, mouseY), 10, colours[len(lanes_points)], 2)
        linePoints.append((x, y))
        cv.imshow('Median frame', image)
        print(str(mouseX) + " " + str(mouseY))
        if cv.waitKeyEx(0) == ord('w'):
            lanes_points.append(linePoints.copy())
            linePoints.clear()
            print("lane added")


def set_detectors(xs_lanes, cs_lanes):
    i = 0
    for lane in xs_lanes:
        for point in lane:
            detectors.append(Detector(point, int(cs_lanes[i](point))))
        lanes.append(detectors.copy())
        detectors.clear()
        i += 1
    return lanes


def save_detectors():
    print("Saving detectors coordinates: ")
    # Заполняем csv файл координатами детекторов
    data = dict()
    lane_counter = 1
    for lane in lanes:
        detector_number = 1
        for detector in lane:
            new_dict = {"X " + str(lane_counter) + "." + str(detector_number): detector.detX}
            data.update(new_dict)
            new_dict = {"Y " + str(lane_counter) + "." + str(detector_number): detector.detY}
            data.update(new_dict)
            detector_number += 1
        lane_counter += 1

    lane_counter = 1
    for lane in lanes:
        new_dict = {"Number of detectors on lane:" + str(lane_counter): len(lane)}
        data.update(new_dict)
        lane_counter += 1
    df = pd.DataFrame([data])
    df.to_csv(r'csv/Coordinates.csv', sep=';', index=False)
    print("Success")


# Получение среднего значения цвета Метрика1
def get_avg_colour_sum(gray, detectors):
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                             int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
        avg_color_per_row = np.average(detector_zone, axis=0)  # считаем средние цвета для пикселей по горизонтали
        avg_color = np.average(avg_color_per_row, axis=0)  # считаем средний цвет для средних цветов по горизонтали
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(avg_color)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


# Получение среднего значения квадрата цвета Метрика2
def get_avg_square_sum(gray, detectors):
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                             int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
        sum_pow = 0
        h, w = detector_zone.shape

        new_zone = (detector_zone ** 2)
        for row in detector_zone:
            row = np.square(detector_zone)
        avg_color_per_row = np.average(new_zone, axis=0)  # считаем средние цвета для пикселей по горизонтали
        avg_color = np.average(avg_color_per_row, axis=0)
        detector.add_avg_colour_sum(np.sqrt(avg_color))

        for i in range(0, h):
            for j in range(0, w):
                sum_pow += math.pow(detector_zone[i, j], 2)
        sum_sqr_avg = np.sqrt(sum_pow) / detector_zone.size
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(sum_sqr_avg)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


# Получение среднего разницы цветов текущего и предыдущего кадров Метрика3
def get_avg_diff_sum(gray, previous_gray, detectors):
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                             int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
        previous_detector_zone = previous_gray[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                                               int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
        sum_pow = 0
        h, w = detector_zone.shape
        for i in range(0, h):
            for j in range(0, w):
                sum_pow += abs(detector_zone[i, j] - previous_detector_zone[i, j])
        sum_diff_avg = sum_pow / detector_zone.size
        # Добавляем значение среднего цвета для детектора
        detector.add_avg_colour_sum(sum_diff_avg)
        # print(avg_color)  # Выводм значение среднего цвета для детектора в консоль


def get_var_dif(detectors):
    for i in range(0, len(detectors)):
        for j in range(1, len(detectors[i].avgColour)):
            detectors[i].avgColour[j] = abs(detectors[i].avgColour[j] - detectors[i].avgColour[j - 1])


########################################################################################################################
# Получение среднего разницы цветов текущего и медианного кадров Метрика4
def get_avg_median_sum(gray, median, detectors, eps):
    # для всех детекторов
    for detector in detectors:
        # Вырезаем область детектора
        detector_zone = gray[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                             int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
        median_detector_zone = median[int((detector.detY - (detector_heigth / 2))):int((detector.detY + (detector_heigth / 2))),
                                      int((detector.detX - (detector_width / 2))):int((detector.detX + (detector_width / 2)))]
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


########################################################################################################################
# Дискретизация активаций детекторов
def detectors_discretization(detectors, frameCounter):
    # Задаем начальное значение активации всех детекторов на всех кадрах как 0
    for detector in detectors:
        detector.detections = [0] * frameCounter

    # Проходимся по всем кадрам детектора
    for i in range(0, len(detectors)):
        for j in range(0, frameCounter - 1):
            # Считаем текущую разницу среднего цвета между текущим и предыдущим кадрами
            if detectors[i].avgColour[j] == 0:
                current_avg_colour_delta = 0
            else:
                current_avg_colour_delta = abs(
                    (detectors[i].avgColour[j] - detectors[i].avgColour[j + 1]) / detectors[i].avgColour[j]) * 100
            # Если разница больше заданной, то активируем детектор
            if current_avg_colour_delta > activation_avg_colour_delta:
                detectors[i].detections[j + 1] = 1


########################################################################################################################
# Фильтр для дискретизации активаций детекторов
def detectors_discretization_filter(detectors, frameCounter):
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


# Получаем список всех файлов в папке
video_path = 'Videos/'
files = os.listdir(video_path)
videos = []

# Добавляем в список только файлы с нужным расширением
for file in files:
    if file.endswith(".mp4"):
        videos.append("Videos/" + file)

frame_counter = 0  # Счетчик кадров
frame_step = 1  # Шаг кадров
video_counter = 0  # Счетчик видеофайлов
print("Total videos: " + str(len(videos)))  # Отображаем общее количество видеофайлов

filename = videos[0]
cap = cv.VideoCapture(filename)
if not cap.isOpened():
    print("Error opening file")
if set_detectors_by_hand:
    cv.namedWindow('Median frame', cv.WINDOW_NORMAL)
    cv.resizeWindow('Median frame', 800, 600)
    cv.setMouseCallback('Median frame', set_point)

    if create_median_frame:
        frame = median_frame(filename)
        median_frame = median_frame(filename)
        cv.imwrite('median_frame.png', median_frame)
    else:
        median_frame = cv.imread('median_frame.png')
    median_gray = cv.cvtColor(median_frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Median frame', median_frame)
    cv.resizeWindow('Median frame', 800, 600)

    while 1:
        if cv.waitKeyEx(0) == ord('e'):
            cv.destroyWindow('Median frame')
            break

    for i in range(0, (len(lanes_points))):
        lanes_points[i] = sort_points(lanes_points[i])

    for lane in lanes_points:
        xs, cs = set_spline(lane)
        xs_lanes.append(xs)
        cs_lanes.append(cs)
    lanes = set_detectors(xs_lanes, cs_lanes)
    save_detectors()
else:
    median_frame = cv.imread('median_frame.png')
    median_gray = cv.cvtColor(median_frame, cv.COLOR_BGR2GRAY)
    if os.path.exists('Coordinates.csv'):
        df = pd.read_csv('Coordinates.csv')
        # Проверяем не пустой ли файл
        if df.empty:
            print("Ошибка файл Coordinates.csv с координатами детекторов пустой")
        else:
            # Получаем координаты детекторов из файла
            columns_list = df.columns.values.tolist()
            buf = columns_list[0].split(';')
            buf = buf[len(buf) - 1].split(':')
            number_of_lanes = int(buf[1])
            local_counter = number_of_lanes

            detectors_per_lane = []
            while local_counter > 0:
                buf = df.values[0][0].split(';')
                detectors_per_lane.append(int(buf[len(buf) - local_counter]))
                local_counter -= 1

            for i in range(len(df)):
                coordinates = df.values[i][0].split(';')

            coordinates_counter = 0

            for i in range(0, len(detectors_per_lane)):
                while len(detectors) < detectors_per_lane[i]:
                    detectors.append(
                        Detector(int(coordinates[coordinates_counter]),
                                 int(coordinates[coordinates_counter + 1])))
                    coordinates_counter += 2
                if len(detectors) == detectors_per_lane[i]:
                    lanes.append(detectors.copy())
                    # Очищаем текущий список детекторов
                    detectors.clear()

########################################################################################################################
for video in videos:
    frames_in_video_counter = 0
    cap = cv.VideoCapture(video)
    # Считаем количество кадров в видеофайле
    property_id = int(cv.CAP_PROP_FRAME_COUNT)
    video_length = int(cv.VideoCapture.get(cap, property_id))
    print("Current video name : " + video)  # Отображаем общее имя видеофайла
    print("Current video frames: " + str(video_length - 1))  # Отображаем общее кадров в видеофайле
    print("Videos processed: " + str(video_counter))  # Отображаем количество обработанных видеофайлов
    if drawing:  # Отображать окно обработки?
        cv.namedWindow(video, cv.WINDOW_NORMAL)
        cv.resizeWindow(video, 800, 600)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        if drawing:  # Если включена визуализация
            # Выводим обработанное/общее количество кадров
            cv.putText(frame, "Frame " + str(frames_in_video_counter) + " / " + str(video_length - 1),
                       (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
        colour_counter = 0
        for lane in lanes:
            # Отрисовываем детектор
            draw_detector(lane, colour_counter)
            if drawing:
                cv.imshow(video, frame)
            colour_counter += 1
            # считаем значение для заданной метрики
            if metric == 1:
                get_avg_colour_sum(gray, lane)  # Метрика 1
            elif metric == 2:
                get_avg_square_sum(gray, lane)  # Метрика 2
            elif metric == 3:
                if frame_counter != 0:
                    get_avg_diff_sum(gray, previous_gray, lane)  # Метрика 3
            elif metric == 4:
                get_avg_median_sum(gray, median_gray, lane, 1.5)  # Метрика 4
        if drawing:
            cv.imshow(video, frame)
        frame_counter += 1
        frames_in_video_counter += frame_step
        previous_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    video_counter += 1
    if drawing:
        cv.destroyWindow(video)

########################################################################################################################
# Заполняем csv файл параметрами метрики
print("Saving Metric Values: ")
data = dict()
lane_counter = 1
for lane in lanes:
    detectorNumber = 1
    for detector in lane:
        new_dict = {"lane" + str(lane_counter) + " det" + str(detectorNumber): detector.avgColour}
        data.update(new_dict)
        detectorNumber += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'csv/MetricValues.csv', sep=';', index=False)
print("Success")
########################################################################################################################
# Дискретизируем значения детектров
print("Start of discretization: ")
for lane in lanes:
    detectors_discretization(lane, frame_counter)
print("Success")
########################################################################################################################
# Заполняем csv файл дискретными значениями с детекторов
print("Saving Discretization results: ")
data = dict()
lane_counter = 1
for lane in lanes:
    detectorNumber = 1
    for detector in lane:
        new_dict = {"lane" + str(lane_counter) + " det" + str(detectorNumber): detector.detections}
        data.update(new_dict)
        detectorNumber += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'csv/RawDetections.csv', sep=';', index=False)
print("Success")
########################################################################################################################
# Фильтруем дискретные значения детектров
print("Start of discretization filtering: ")
for lane in lanes:
    detectors_discretization_filter(lane, frame_counter)
print("Success")
########################################################################################################################
# Заполняем csv файл дискретными отфильтрованными значениями с детекторов
print("Saving Filtering results: ")
data = dict()
lane_counter = 1
for lane in lanes:
    detectorNumber = 1
    for detector in lane:
        new_dict = {"lane" + str(lane_counter) + " det" + str(detectorNumber): detector.detections}
        data.update(new_dict)
        detectorNumber += 1
    lane_counter += 1
df = pd.DataFrame(data)
df.to_csv(r'csv/FilteredDetections.csv', sep=';', index=False)
print("Success")
########################################################################################################################
