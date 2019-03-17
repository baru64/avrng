import cv2

class VideoHandler:
    def __init__(self, video_source, frame_size=(320,200)):
        self.cap = cv2.VideoCapture(video_source)
        self.frame_size = frame_size

    def get_frame(self):
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, self.frame_size)
        return frame

    def release(self):
        self.cap.release()

if __name__ == "__main__":
    video = VideoHandler(0)
    print(video.get_frame())
    video.release()