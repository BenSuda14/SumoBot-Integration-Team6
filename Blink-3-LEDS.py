from machine import Pin
import time

# GP10, GP11, GP12 (physical pins 14, 15, 16); GND is physical pin 13
leds = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT)]

while True:
    for led in leds:
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)

