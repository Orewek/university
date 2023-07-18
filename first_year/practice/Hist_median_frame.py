import cv2

from matplotlib import pyplot as plt

import numpy as np

from scipy import ndimage


def make_hist(file_name, frame_folder, mega_frame):
    img = cv2.imread(f'median_frames/{mega_frame}/{frame_folder}/median_frame_{file_name}.png', 0)
    data_list = []

    image_array = np.array(img)

    # Calculate the expectation (mean) and variance
    expectation = np.mean(image_array)
    variance = np.var(image_array)

    # print("Мат. ожидание:", round(expectation), 14)
    # print("Дисперсия:", round(variance, 8))
    # print("Ср.кв. отклонение:", round(np.sqrt(variance), 7))
    data_list.append(round(expectation, 14))
    data_list.append(round(variance, 8))
    data_list.append(round(np.sqrt(variance), 7))

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    max_value_y = np.max(hist)
    min_value_y = np.min(hist)
    max_value_x = np.argmax(hist)
    min_value_x = np.argmin(hist)
    # print("Максимум (", max_value_x, ";", max_value_y, ")")
    # print("Минимум (", min_value_x, ";", min_value_y, ")")
    data_list.append(max_value_x)
    data_list.append(max_value_y)
    data_list.append(min_value_x)
    data_list.append(min_value_y)

    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlabel('Значение пикселя')
    plt.ylabel('Частота')
    plt.title('Гистограмма медианного кадра')
    plt.xlim([0, 256])
    plt.savefig(f'{mega_frame}/{frame_folder}/hist_{file_name}.png')
    # plt.show()

    return data_list
