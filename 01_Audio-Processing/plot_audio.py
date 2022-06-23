import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("dont_speak-no_doubt.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(12, 6))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (seconds)")
plt.xlim(0, t_audio)
plt.show()

plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()
