from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

def main():
    audio_loader = AudioAdapter.default()
    waveform, sample_rate = audio_loader.load("./audio/Example.mp3")

    separator = Separator("spleeter:2stems")
    prediction = separator.separate(waveform)
    separator.separate_to_file(
        "./audio/Example.mp3",
        "./output",
        codec="wav"
    )

if __name__ == "__main__":
    # Only needed on Windows when multiprocessing is used (Spleeter uses it internally)
    import multiprocessing as mp
    mp.freeze_support()
    main()
