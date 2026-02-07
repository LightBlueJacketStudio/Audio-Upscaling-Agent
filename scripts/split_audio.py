from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
import ffmpeg
import numpy as np

def standardize_audio(input_path, output_path):
    (
        ffmpeg
        .input(input_path)
        .output(
            output_path,
            ar=44100,
            ac=2,
            format="wav"
        )
        .overwrite_output()
        .run(quiet=True)
    )

def main():
    audio_loader = AudioAdapter.default()
    FILE_NAME = "Example"
    INPUT_PATH = f"./audio/{FILE_NAME}.mp3"
    PRE_PATH = f"./preprocess/{FILE_NAME}.wav"
    OUTPUT_FOLD = "./output"

    standardize_audio(INPUT_PATH, PRE_PATH)
    waveform, sample_rate = audio_loader.load(INPUT_PATH)

    
    
    separator = Separator("spleeter:2stems")
    prediction = separator.separate(waveform)
    separator.separate_to_file(
        PRE_PATH,
        OUTPUT_FOLD,
        codec="wav"
    )

if __name__ == "__main__":
    # Only needed on Windows when multiprocessing is used (Spleeter uses it internally)
    import multiprocessing as mp
    mp.freeze_support()
    main()
