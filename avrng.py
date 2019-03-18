import argparse
import numpy as np
from video import VideoHandler
from audio import AudioHandler

class Avrng():
    

    def __init__(self, video_source, audio_source):
        self.video_source = VideoHandler(video_source)
        self.audio_source = AudioHandler(device=int(audio_source))
        self.audio_buffer = []

    def get_byte(self):
        # TODO avrng algorithm
        if len(self.audio_buffer) < 16:
            self.audio_buffer.extend(self.audio_source.get_recording())
        random_byte = np.uint8(0)
        for i in range(15):
            random_byte = (random_byte + self.audio_buffer.pop()) % 255
        
        frame = self.video_source.get_frame()
        x, y = 0, 0
        for i in range(9):
            x += frame[98+i][148+i][i%3]
            y += frame[98+i][148+i][(i+1)%3]
        
        x = x % 320
        y = y % 200

        for i in range(3):
            random_byte = (random_byte + frame[y][x][i]) % 255
        
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