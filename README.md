# SonicRunway
CS268 - Sonic Runway Project
## **Overview**

This project recreates the iconic Sonic Runway installation on a scalable, wireless model using addressable LED strips and Wi-Fi-enabled microcontrollers. The system dynamically converts audio input into vibrant, synchronized light patterns, offering an immersive experience of sound transformed into light.

This implementation highlights the intersection of **art and technology**, combining real-time audio analysis, wireless communication, and LED control.

## **Features**

- **Real-Time Audio-to-Light Mapping**: Converts live audio input into dynamic LED brightness levels.
- **Wireless LED Control**: Enables wireless control of addressable LED strips using the WLED library.
- **Adjustable Parameters**:
    - LED color.
    - Brightness decay rate.
    - Audio sensitivity and thresholds.
    - Delay between updates for smoother transitions.

## **Hardware**

- **NodeMCU (ESP8266)**: Wi-Fi-enabled microcontroller for LED control.
- **Addressable LED Strip (WS2812B)**: Fully addressable LEDs for individual light control.
- **Microphone (or Virtual Audio Input)**: Captures audio input for sound analysis.
- **Power Supply**: 5V power supply matching LED strip requirements.

## **Software**

- **Python**: For real-time audio processing and LED control.
- **WLED**: Open-source software for wireless LED strip management.
- **Voicemeeter**: Virtual audio mixer for audio input/output routing.
- **NumPy**: For efficient numerical computations.
- **PyAudio**: For audio input stream handling.

### **Hardware Setup**

1. Connect the LED strip to the NodeMCU (ESP8266) as per the WLED documentation:
    - **DIN (Data In)** to NodeMCU's GPIO pin.
    - **VCC and GND** to a 5V power source.
2. Flash the WLED firmware onto the NodeMCU using the WLED Installer.
3. Configure WLED to connect to your Wi-Fi network.

### **Software Setup**

1. Clone the repository:
    `git clone https://github.com/aldridge-fonseca/sonicrunway`
2. Install the required Python libraries:
    `pip install pyaudio numpy requests`  
3. Route your audio input:
    - For physical microphones, connect via your system's input device settings.
    - For virtual audio input (e.g., YouTube), use Voicemeeter to route sound to a virtual microphone.

## **Implementation Steps**

### **Method 1**

1. **Hardware Assembly**: Set up the NodeMCU and LED strip with proper wiring and power supply.
2. **Firmware Installation**: Flash WLED onto the NodeMCU and configure Wi-Fi settings.
3. **Code Execution**: Run the Python script, configure parameters, and enjoy the dynamic light show.

### **Method 2**

1. **Install LEDFx**: Refer to the LEDFx Documentation for detailed installation guides.
2. **Configure Audio Input**: Use Voicemeeter to route system audio or microphone to LEDFx.
3. **Connect LEDFx to WLED**: Launch LEDFx and go to the settings page.
4. **Add a new WLED device**: Enter the IP address of NodeMCU running WLED. Save the configuration.
5. **Select a Visualization**: In LEDFx, choose an audio visualization effect (e.g., spectrum analyzer, wave, or pulse). Adjust parameters for brightness, speed, and intensity as needed.
6. **Test the Setup**: Play any audio source (e.g., Spotify, YouTube) and enjoy the real-time visual effects on LED strip synchronized to the audio.


## **References**

- Sonic Runway
- WLED Documentation
- Voicemeeter
- [LEDFx](https://github.com/LedFx/LedFx)

## **Contributors**

1. **Aldridge Fonseca**
2. **Gitika Rath**
