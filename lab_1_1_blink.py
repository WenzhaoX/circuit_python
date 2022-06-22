import time
from adafruit_circuitplayground import cp

while True: 
    cp.red_led = True 
    times.sleep(0.5)
    cp.red_led = False
    time.sleep(0.5)
