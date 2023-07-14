import os

import cv2 as cv

import numpy as np


def median_frame(filename):
    file_path = filename
    video = cv.VideoCapture(file_path)
    FOI = video.get(cv.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=1)
    frames = []
    for frameOI in FOI:
        video.set(cv.CAP_PROP_POS_FRAMES, frameOI)
        ret, frame = video.read()
        frames.append(frame)
    result = np.median(frames, axis=0).astype(dtype=np.uint8)
    return result


def make_frame(path, frame_folder, video_folder):
    result = median_frame(f'{video_folder}/{path}.mp4')
    cv.imwrite(f'median_frame_{path}.png', result)
    try:
        os.rename(f'median_frame_{path}.png', f'median_frames/{frame_folder}/median_frame_{path}.png')
    except:
        os.remove(f'median_frame_{path}.png')
    cv.namedWindow('Median filtering result', cv.WINDOW_NORMAL)
    cv.resizeWindow('Median filtering result', 800, 600)
    # cv.imshow("Median filtering result", result)
    # cv.waitKey(0)
