import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 5
sample_rate = 48000

print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
sd.wait()
print("Recording complete.")

sf.write("thing.mp3", audio, sample_rate, format='MP3')

audio = audio.flatten()

# Perform FFT
n = len(audio)
freqs = np.fft.rfftfreq(n, d=1/sample_rate)
fft_values = np.abs(np.fft.rfft(audio))

plt.figure(figsize=(10, 5))
plt.plot(freqs, fft_values)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Frequency Spectrum")
plt.grid()
plt.show()
