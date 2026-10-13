from machine import Pin
from time import sleep

# Motor A
phaseA = Pin(20, Pin.OUT, value=0)
enableA = Pin(21, Pin.OUT, value=0)

# Motor B
phaseB = Pin(26, Pin.OUT, value=0)
enableB = Pin(27, Pin.OUT, value=0)


def stop():
    enableA.value(0)
    enableB.value(0)


def test_motor(label, direction, run_a, run_b):
    stop()
    sleep(2)

    phaseA.value(direction)
    phaseB.value(direction)

    print(label)
    enableA.value(run_a)
    enableB.value(run_b)
    sleep(5)

    stop()
    print("Motors stopped")


try:
    print("Test 5 starting")

    test_motor("Motor A: direction 1", 0, 1, 0)
    test_motor("Motor A: direction 2", 1, 1, 0)

    test_motor("Motor B: direction 1", 0, 0, 1)
    test_motor("Motor B: direction 2", 1, 0, 1)

    test_motor("Both motors: direction 1", 0, 1, 1)
    test_motor("Both motors: direction 2", 1, 1, 1)

    print("Test 5 complete")

finally:
    stop()
