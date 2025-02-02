import soundfile as sf
import sounddevice as sd
import numpy as np
import atexit
from datetime import datetime

# Cleanup function
def cleanup():
    print("Performing cleanup tasks...")

atexit.register(cleanup)

def analyze(reading, hz):
    audio = reading[0].flatten()

    # Perform FFT
    n = len(audio)
    freqs = np.fft.rfftfreq(n, d=1/hz)
    fft_values = np.abs(np.fft.rfft(audio))

    return np.average(fft_values[90:156]) > 1

def main():
    fs = 48000  # Readings per second

    # Open audio stream
    stream = sd.InputStream(device='MacBook Air Microphone, Core Audio', channels=1, samplerate=fs)
    stream.start()

    batch = []
    save_current_batch = save_next_batch = False

    try:
        while True:
            reading = stream.read(fs)  # Read 1 second (48000 data points)
            batch.append(reading[0])

            if analyze(reading, fs):  # If current reading is flagged, save this and next 5 sec
                save_current_batch = True
                # save_next_batch = True

            if len(batch) >= 5:
                if save_current_batch:
                    # Save batch
                    filename = datetime.now().strftime("sleep_talking_%Y-%m-%d_%H-%M-%S.mp3")
                    print(f'Saving batch as {filename}...')
                    audio_data = np.concatenate(batch, axis=0)
                    sf.write("output/" + filename, audio_data, fs, format='MP3')
                    save_current_batch = save_next_batch
                    save_next_batch = False
                batch = []
    except KeyboardInterrupt:
        print("Stopping the stream...")
        stream.stop()

if __name__ == "__main__":
    main()