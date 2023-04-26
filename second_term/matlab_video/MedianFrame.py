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