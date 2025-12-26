import board
import digitalio
import analogio
import time
import wifi
import socketpool
import adafruit_requests
import ssl  
from secrets import secrets


print("Resetare WiFi...")
wifi.radio.enabled = False
wifi.radio.enabled = True
print("Conectare la WiFi...")

print("Conectare la WiFi...")
try:
    wifi.radio.connect(secrets['ssid'], secrets['password'])
    print(f"Conectat la retea!")
except Exception as e:
    print("Eroare WiFi:", e)


pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context() 
requests = adafruit_requests.Session(pool, context) 


AIO_USER = secrets['aio_username']
AIO_KEY = secrets['aio_key']
FEED_NAME = "welcome-feed" 
url = f"https://io.adafruit.com/api/v2/{AIO_USER}/feeds/{FEED_NAME}/data"
headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}


data_pin = digitalio.DigitalInOut(board.GP16)
clock_pin = digitalio.DigitalInOut(board.GP17)
latch_pin = digitalio.DigitalInOut(board.GP18)
for p in [data_pin, clock_pin, latch_pin]:
    p.direction = digitalio.Direction.OUTPUT

senzor = analogio.AnalogIn(board.GP27)
ultimul_model = -1
ultimul_timp_cloud = 0

def update_cip(pattern):
    latch_pin.value = False
    for i in range(8):
        clock_pin.value = False
        data_pin.value = (pattern >> (7 - i)) & 1
        clock_pin.value = True
    latch_pin.value = True

print("--- Sistem IoT Online ---")

while True:
    val = senzor.value
    
    
    if val < 1000:
        model = 0b00000000 
    elif val < 2000:
        model = 0b00000001 
    elif val < 3000:
        model = 0b00000010 
    elif val < 4000:
        model = 0b00000100
    elif val < 5000:
        model = 0b00001000 
    elif val < 6500:
        model = 0b00010000 
    elif val < 7500:
        model = 0b00100000 
    elif val < 8500:
        model = 0b01000000 
    else:
        model = 0b10000000 

    if model != ultimul_model:
        update_cip(model)
        ultimul_model = model
        print(f"Lumina: {val} | Bit activ: {bin(model)}")
    
    

 
    if (time.monotonic() - ultimul_timp_cloud) > 3:
        try:
            print(f"📤 Trimitere Cloud: {val}")
            payload = {"value": val}
            response = requests.post(url, json=payload, headers=headers)
            print("Status server:", response.status_code)
            response.close()
            ultimul_timp_cloud = time.monotonic()
        except Exception as e:
            print("Eroare Cloud:", e)

    time.sleep(0.1)
