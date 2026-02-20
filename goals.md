## goal: use AI to improve the quality for split tracks
## Next steps: learn FFmpeg


MP3 input
↓
[0] Decode / standardize audio
FFmpeg: MP3 → WAV, set sample rate/channels
What “audio standardizing” means (practically)

In ML / DSP pipelines, this usually means:

Decode compressed audio (MP3 → PCM)

Force sample rate (e.g. 44.1 kHz)

Force channel layout (mono or stereo)

Optionally normalize loudness or peak level

You don’t have to do loudness normalization — sample rate + channels are the big ones.
↓
[1] Source separation (stems)
Spleeter (or Demucs for higher quality)
↓ done Feb 6
[2] Upscale / enhance (per stem)
Music SR / restoration (AudioSR, diffusion SR, denoise/de-reverb as needed)
↓
[3] Loudness normalize + export
WAV stems + (optional) metadata report