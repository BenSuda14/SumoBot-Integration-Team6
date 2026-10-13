# RECEIVER CODE
import machine
from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging
# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
   print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring


ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)
# Main loop to keep the script running
while True:
   pass # Execution is interrupt-driven, so just keep the script alive


# TRANSMITTER CODE
import ir_tx
import time
import machine
from ir_tx.nec import NEC
from machine import Pin
# Set up IR Transmitter
tx_pin = Pin(17,Pin.OUT,value=0)
device_addr = 0x01
transmitter = NEC(tx_pin)
# List of Commands
commands = [0x01,0x02,0x03,0x04]
if __name__ == "__main__":
 while True:
    # Loop that goes through the commands and transmits them
    for command in commands:
     transmitter.transmit(device_addr,command)
     print("COMMANDS",hex(command),"TRANSMITTED.")
     time.sleep_ms(200)
    time.sleep(3)
