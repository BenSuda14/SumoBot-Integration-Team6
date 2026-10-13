from machine import Pin
from time import sleep_ms
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

# Motor A
phaseA = Pin(9, Pin.OUT, value=0)
enableA = Pin(8, Pin.OUT, value=1)

# Motor B
phaseB = Pin(14, Pin.OUT, value=0)
enableB = Pin(15, Pin.OUT, value=1)


def ir_callback(data, addr, ctrl):
    if data < 0:
        return  # Ignore held-button repeats

    if data == 0x01:
        phaseA.value(1)
        phaseB.value(1)
        enableA.value(1)
        enableB.value(1)
        print("Motor A, B Forward")

    elif data == 0x02:
        phaseA.value(0)
        phaseB.value(0)
        enableA.value(1)
        enableB.value(1)
        print("Motor A, B Backward")

    elif data == 0x03:
        enableA.value(0)
        enableB.value(0)
        print("Motors Stop")

    else:
        return

    print("Data: 0x{:02X}, Address: 0x{:02X}".format(data, addr))


ir_pin = Pin(17, Pin.IN, Pin.PULL_UP)
ir_receiver = NEC_8(ir_pin, ir_callback)
ir_receiver.error_function(print_error)

try:
    while True:
        sleep_ms(100)
finally:
    enableA.value(0)
    enableB.value(0)
    ir_receiver.close()
