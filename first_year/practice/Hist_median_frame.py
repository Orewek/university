import cv2

from matplotlib import pyplot as plt

import numpy as np

from scipy import ndimage

img = cv2.imread('median_frame.png', 0)

image_array = np.array(img)

# Calculate the expectation (mean) and variance
expectation = np.mean(image_array)
variance = np.var(image_array)

print("Мат. ожидание:", expectation)
print("Дисперсия:", variance)
print("Ср.кв. отклонение:", np.sqrt(variance))

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

max_value_y = np.max(hist)
min_value_y = np.min(hist)
max_value_x = np.argmax(hist)
min_value_x = np.argmin(hist)
print("Максимум (", max_value_x, ";", max_value_y, ")")
print("Минимум (", min_value_x, ";", min_value_y, ")")

plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlabel('Значение пикселя')
plt.ylabel('Частота')
plt.title('Гистограмма медианного кадра')
plt.xlim([0, 256])
plt.show()
