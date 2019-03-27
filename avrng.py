import argparse
import warnings
import hashlib
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
        for i in range(16):
            random_byte = np.bitwise_xor(random_byte, self.audio_buffer.pop())

        
        frame = self.frame_buffer.pop()
        x, y, res_y, res_x = 0, 0, len(frame), len(frame[0])
        for i in range(8):
            x = np.bitwise_xor(x, self.audio_buffer.pop()) % res_x
            y = np.bitwise_xor(y, self.audio_buffer.pop()) % res_y


        for i in range(3):
            random_byte = np.bitwise_xor(random_byte, frame[y][x][i])
        
        return random_byte
    
    def release(self):
        self.video_source.release()
    
    @staticmethod
    def dump_sha256(array):
        narray = np.array(array, dtype='uint8')
        if (len(narray)%32.0) != 0.0:
            return None 
        splitted = np.split(narray, (len(narray)/32))
        out = b''
        for block in splitted:
            h = hashlib.sha256()
            h.update(block)
            out += h.digest()
        return out
        

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
