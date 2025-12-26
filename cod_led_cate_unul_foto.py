import board
import digitalio
import analogio
import time

# Pini Cip
data_pin = digitalio.DigitalInOut(board.GP16)
clock_pin = digitalio.DigitalInOut(board.GP17)
latch_pin = digitalio.DigitalInOut(board.GP18)
for p in [data_pin, clock_pin, latch_pin]:
    p.direction = digitalio.Direction.OUTPUT

senzor = analogio.AnalogIn(board.GP27)
ultimul_model = -1 

def update_cip(pattern):
    latch_pin.value = False
    for i in range(8):
        clock_pin.value = False
        data_pin.value = (pattern >> (7 - i)) & 1
        clock_pin.value = True
    latch_pin.value = True

print("--- Sistem Stabil (900 - 9000) ---")
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
    
    time.sleep(0.1)
