import time
from machine import Pin, I2C
from ir_tx.nec import NEC

# ---- Configuration ----
DEVICE_ADDR = 0x01

CMD_FORWARD  = 0x01
CMD_BACKWARD = 0x02
CMD_LEFT     = 0x03
CMD_RIGHT    = 0x04
CMD_STOP     = 0x00   # Extra command sent on release so the SumoBot halts

IR_PIN       = 17     # GP17 (physical pin 22), free on this wiring
I2C_SDA_PIN  = 12     # GP12 (physical pin 16)
I2C_SCL_PIN  = 13     # GP13 (physical pin 17)
GAMEPAD_ADDR = 0x50   # Default I2C address for the STEMMA QT gamepad
CENTER       = 512    # Analog center (10-bit ADC, 0-1023)
DEADZONE     = 200    # Ignore small stick movements
REPEAT_MS    = 100    # Resend the current command this often while held
INVERT_Y     = False  # Set True if pushing the stick up drives backward

# ---- Hardware setup ----
tx = NEC(Pin(IR_PIN, Pin.OUT, value=0))
i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=100000)

# seesaw (gamepad firmware) register bases
SS_ADC_BASE       = 0x09
SS_ADC_CH_OFFSET  = 0x07
JOY_X_PIN         = 14
JOY_Y_PIN         = 15

def ss_read(base, reg, nbytes, delay_us=1000):
    i2c.writeto(GAMEPAD_ADDR, bytes([base, reg]))
    time.sleep_us(delay_us)
    return i2c.readfrom(GAMEPAD_ADDR, nbytes)

def read_axis(pin):
    buf = ss_read(SS_ADC_BASE, SS_ADC_CH_OFFSET + pin, 2)
    return (buf[0] << 8) | buf[1]

def pick_command(x, y):
    dx = x - CENTER
    dy = y - CENTER
    if INVERT_Y:
        dy = -dy
    if abs(dx) < DEADZONE and abs(dy) < DEADZONE:
        return None                      # Stick centered
    if abs(dy) >= abs(dx):               # Dominant axis wins
        return CMD_BACKWARD if dy > 0 else CMD_FORWARD
    return CMD_RIGHT if dx > 0 else CMD_LEFT

# ---- Main loop ----
if __name__ == "__main__":
    last_cmd = None
    last_sent = 0
    print("Joystick IR controller ready.")

    while True:
        x = read_axis(JOY_X_PIN)
        y = read_axis(JOY_Y_PIN)
        cmd = pick_command(x, y)
        now = time.ticks_ms()

        if cmd is None:
            if last_cmd is not None:     # Just released: send stop once
                tx.transmit(DEVICE_ADDR, CMD_STOP)
                print("STOP TRANSMITTED.  x=", x, "y=", y)
            last_cmd = None
        elif cmd != last_cmd or time.ticks_diff(now, last_sent) >= REPEAT_MS:
            tx.transmit(DEVICE_ADDR, cmd)
            print("COMMAND", hex(cmd), "TRANSMITTED.  x=", x, "y=", y)
            last_sent = now
            last_cmd = cmd

        time.sleep_ms(20)
