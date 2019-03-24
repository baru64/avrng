import math
import cv2
import numpy as np

class VideoHandler:
    def __init__(self, video_source, frame_size=None):
        self.cap = cv2.VideoCapture(video_source)
        self.frame_size = frame_size

    def get_frame(self):
        ret, frame = self.cap.read()
        if self.frame_size:
            frame = cv2.resize(frame, self.frame_size)
        return frame

    @staticmethod
    def split_frame(frame, n):
        stripes = [[] for i in range(n)]
        for col_id in range(len(frame)):
            stripes[col_id % n].append(frame[col_id])
        return stripes

    def release(self):
        self.cap.release()

if __name__ == "__main__":
    video = VideoHandler(0)
    frame = video.get_frame()
    stripes = video.split_frame(frame, 16)
    print("Frame size:", len(frame), len(frame[0]))
    print("Stripe size: ", len(stripes[0]), len(stripes[0][0]))
    video.release()