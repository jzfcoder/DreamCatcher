import sounddevice as sd
import numpy as np
import atexit

def cleanup():
    print("Performing cleanup tasks...")

atexit.register(cleanup)

def analyze(reading):
    print(np.average(reading[0]), np.average(reading[1]))
    return False

def main():
    fs=48000 # readings / sec

    stream = sd.InputStream(device='MacBook Air Microphone, Core Audio', channels=1, samplerate=fs)
    stream.start()

    batch = []

    save_current_batch = save_next_batch = False

    while True:
        reading = stream.read(fs) # every read is 1 sec (48000 dps)

        batch.append(reading)

        if analyze(reading): # if current reading is flagged, save this and next 5 sec
            save_current_batch = True
            save_next_batch = True

        if len(batch) >= 5:
            if save_current_batch:
                # save batch
                print('saving batch...')
                save_current_batch = save_next_batch
                save_next_batch = False
            batch = []


if __name__ == "__main__":
    main()