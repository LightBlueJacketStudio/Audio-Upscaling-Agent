import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# Load audio
NAME = "Example" # the folder we are using
#normal: data, samplerate = sf.read(f"./output/{NAME}/accompaniment.wav")
#preprocess:
#data, samplerate = sf.read(f"./audio/{NAME}.mp3")
#postporcess
data, samplerate = sf.read(f"./preprocess/{NAME}.wav")

# Make sure it's stereo
if len(data.shape) == 1:
    print("Audio is mono. Converting to 2-channel for demonstration.")
    data = np.column_stack((data, data))

left = data[:, 0]
right = data[:, 1]

# FFT function
def compute_fft(signal):
    fft_vals = np.fft.rfft(signal)
    fft_freq = np.fft.rfftfreq(len(signal), 1/samplerate)
    return fft_freq, np.abs(fft_vals)

freq_l, fft_l = compute_fft(left)
freq_r, fft_r = compute_fft(right)

# Define 4 frequency bands
bands = [
    (0, 300),       # Bass
    (300, 2000),    # Low-mid
    (2000, 6000),   # High-mid
    (6000, 20000)   # Treble
]

# Plotting
plt.figure(figsize=(12, 10))

for i, (low, high) in enumerate(bands):
    plt.subplot(4, 1, i+1)
    
    mask = (freq_l >= low) & (freq_l <= high)
    
    plt.plot(freq_l[mask], fft_l[mask], label="Left")
    plt.plot(freq_r[mask], fft_r[mask], linestyle="dashed", label="Right")
    
    plt.title(f"Frequency Band: {low} Hz - {high} Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Intensity")
    plt.legend()

plt.tight_layout()
plt.show()