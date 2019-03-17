import argparse
from video import VideoHandler
from audio import AudioHandler

class Avrng():
    

    def __init__(self, video_source, audio_source):
        self.video_source = VideoHandler(video_source)
        self.audio_source = AudioHandler(device=int(audio_source))

    def get_byte(self):
        # TODO avrng algorithm

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