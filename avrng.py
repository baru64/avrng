from video import VideoHandler
from audio import AudioHandler

class Avrng():
    

    def __init__(self, video_source, audio_source):
        self.video_source = VideoHandler(video_source)
        self.audio_source = AudioHandler(audio_source)

    def get_byte(self):
        # TODO avrng algorithm
        pass

if __name__ == "__main__":
    #TODO cli app
    print("Not implemented yet")
