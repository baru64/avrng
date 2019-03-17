import sounddevice as sd

class AudioHandler():


    def __init__(self, duration=1, sample_rate=48000, device=0):
        sd.default.samplerate = sample_rate
        sd.default.device = device
        sd.default.channels = 2
        self.fs = sample_rate
        self.duration = duration

    def get_recording(self):
        recording = sd.rec(self.duration*self.fs, blocking=True)
        return recording

    def get_sample(self, index=0, channel=0):
        recording = self.get_recording()
        return int((recording[index][channel] + 1) * 128)

if __name__ == "__main__":
    audio = AudioHandler()
    print(audio.get_sample())