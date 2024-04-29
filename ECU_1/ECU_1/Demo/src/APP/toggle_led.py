import serial
import time

# Define serial port and baud rate
serial_port = '/dev/ttyUSB0'  # Change this to match your serial port
baud_rate = 9600

# Open serial port
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Read switch state from user input
        switch_state = input("Enter switch state (0 for off, 1 for on): ")
        
        # Send switch state to microcontroller
        ser.write(bytes([int(switch_state)]))
        
        # Wait for a moment
        time.sleep(0.1)

finally:
    # Close serial port
    ser.close()
