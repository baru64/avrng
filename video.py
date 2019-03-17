import cv2


class VideoHandler:
    def __init__(self):
        pass

    def get_frame(self):

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        px = frame[100, 100]
        cap.release()
        cv2.destroyAllWindows()
        return px
