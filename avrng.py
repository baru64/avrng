import argparse
import warnings
import numpy as np
from video import VideoHandler
from audio import AudioHandler

class Avrng():
    

    def __init__(self, video_source, audio_source):
        self.video_source = VideoHandler(video_source)
        self.audio_source = AudioHandler(device=int(audio_source))
        self.audio_buffer = []
        self.frame_buffer = []

    def get_byte(self):
        if len(self.audio_buffer) < 32:
            self.audio_buffer.extend(self.audio_source.get_recording())
        if not len(self.frame_buffer):
            self.frame_buffer.extend(VideoHandler
                                    .split_frame
                                    (self.video_source.get_frame(),32))

        random_byte = np.uint8(0)
        warnings.simplefilter("ignore")
        for i in range(15):
            random_byte = random_byte + self.audio_buffer.pop()
        
        frame = self.frame_buffer.pop()
        x, y, res_y, res_x = 0, 0, len(frame), len(frame[0])
        for i in range(15):
            x = (x + self.audio_buffer.pop()) % res_x
            y = (y + self.audio_buffer.pop()) % res_y

        for i in range(3):
            random_byte = random_byte + frame[y][x][i]
        
        return random_byte
    
    def release(self):
        self.video_source.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="True random number generator based on audio and video sources"
        )
    parser.add_argument('-a', '--audio-source', type=int, default=0)
    parser.add_argument('-v', '--video-source', default=0)
    parser.add_argument('length', type=int, help='Length of random bytes array')
    args = parser.parse_args()

    trng = Avrng(args.video_source, args.audio_source)
    print([trng.get_byte() for i in range(int(args.length))])
    trng.release()
