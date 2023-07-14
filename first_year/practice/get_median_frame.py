import cv2 as cv

import numpy as np


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


result = median_frame('10.00.03-10.05.00[R][0@0][0].mp4')
cv.imwrite('median_frame.png', result)
cv.namedWindow('Median filtering result', cv.WINDOW_NORMAL)
cv.resizeWindow('Median filtering result', 800, 600)
cv.imshow("Median filtering result", result)
cv.waitKey(0)
