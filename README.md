# AmbientSense-IoT-Dashboard
A comprehensive IoT Environmental Monitoring and Alert System built with Raspberry Pi Pico 2W.
IoT Ambient Light Monitoring System 💡🌐
An end-to-end IoT project using Raspberry Pi Pico 2 W to monitor ambient light levels, provide local visual feedback via a shift register, and stream real-time telemetry to the Adafruit IO cloud platform.

🚀 Features
Real-time Telemetry: Streams light intensity data to Adafruit IO via HTTPS.

Local Visual Feedback: Controls an 8-LED bar graph using a 74HC595 Shift Register to minimize GPIO usage.

Adaptive Logic: The LED display updates instantly based on light thresholds, while cloud updates are throttled to respect API limits.

Secure Connectivity: Implements SSL/TLS encryption for secure data transmission.

Cloud Dashboard: Remote monitoring via a web-based gauge and line chart.

🛠️ Hardware Components
Microcontroller: Raspberry Pi Pico 2 W (Dual-core ARM Cortex-M33).

Shift Register: 74HC595 (8-bit serial-in, parallel-out).

Sensor: Photoresistor (LDR) in a voltage divider circuit.

Display: 8x LEDs with current-limiting resistors.

Breadboard & Jumpers.

💻 Tech Stack
Language: CircuitPython.

Protocols: HTTPS, SSL/TLS, SPI-like Serial Communication.

Cloud Platform: Adafruit IO.

Libraries: adafruit_requests, adafruit_connection_manager, ssl, socketpool.

🔧 Installation & Setup
CircuitPython: Ensure your Pico 2 W is running the latest CircuitPython firmware.

Libraries: Copy the following .mpy files to your /lib folder:

adafruit_io, adafruit_requests, adafruit_connection_manager, adafruit_ticks.

Credentials: Create a secrets.py file on the Pico:

Python

secrets = {
    'ssid': 'Your_WiFi_Name',
    'password': 'Your_WiFi_Password',
    'aio_username': 'Your_Adafruit_User',
    'aio_key': 'Your_Adafruit_Active_Key'
}
Code: Upload code.py and run it via Thonny.

📈 Challenges Overcome
Signal Integrity: Resolved flickering issues by stabilizing the Latch and Reset pins of the 74HC595.

Cloud Optimization: Optimized the sampling rate to 3 seconds to maximize data resolution without triggering API throttling.

Dependency Management: Manually resolved library conflicts and "ImportRelative" errors in a resource-constrained environment.
