# This Python script adjusts the brightness of a WLED LED strip in real time based on audio input. It uses a microphone (physical or virtual) to capture audio, analyzes its amplitude, and maps it to brightness levels for the LED strip.

# Key Features:

# Dynamically adjusts brightness based on audio amplitude.
# Includes a decay mechanism to smoothly reduce brightness when audio quiets down.
# Allows user configuration for microphone selection, update delay, decay rate, and LED color.
# Parameters:

# WLED_IP: IP address of the WLED controller.
# TOTAL_LEDS: Total number of LEDs in the strip.
# DEFAULT_COLOR: Base color of the LED strip (RGB format).
# CHUNK: Number of audio samples per frame (smaller values improve responsiveness).
# RATE: Sampling rate for audio input, dynamically adjusted to match the selected microphone.
# DECAY_RATE: Speed at which brightness decreases when audio amplitude drops.
# MIN_BRIGHTNESS and MAX_BRIGHTNESS: Define the range of LED brightness.


import pyaudio
import numpy as np
import requests
import time

########################################################
WLED_IP = "10.0.0.192"
TOTAL_LEDS = 300
DEFAULT_COLOR = [255, 0, 255]
CHUNK = 24
DECAY_RATE = 0.9
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 255
DEBUG = False
########################################################


def list_input_devices():
    p = pyaudio.PyAudio()
    print("Available audio input devices:")
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        print(f"{i}: {dev['name']}")
    p.terminate()

def set_led_brightness(brightness):
    url = f"http://{WLED_IP}/json/state"
    payload = {
        "on": True,
        "bri": brightness,
        "seg": [{"start": 0, "stop": TOTAL_LEDS, "col": [DEFAULT_COLOR]}]
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200 and DEBUG:
            print(f"Set brightness to {brightness}")
    except Exception as e:
        print(f"Error setting brightness: {e}")

def main():
    list_input_devices()
    mic_index = int(input("Enter the index of the microphone to use: "))
    delay = float(input("Enter delay between LED updates in seconds (e.g., 0.05): "))

    p = pyaudio.PyAudio()
    device_info = p.get_device_info_by_index(mic_index)
    RATE = int(device_info["defaultSampleRate"])

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=mic_index)

    current_brightness = 0
    threshold = 0

    try:
        while True:
            data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
            amplitude = np.abs(data).mean()
            target_brightness = int(np.interp(amplitude, [threshold, 32767], [MIN_BRIGHTNESS, MAX_BRIGHTNESS]))
            if amplitude < threshold:
                target_brightness = 0
            current_brightness = max(0, max(current_brightness - int(DECAY_RATE * MAX_BRIGHTNESS), target_brightness))
            set_led_brightness(current_brightness)
            if DEBUG:
                print(f"Amplitude: {amplitude}, Brightness: {current_brightness}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
