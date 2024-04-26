import serial
import threading
import time

# Global variables
data_buffer = bytearray()  # Buffer to store data bytes
receiving_data = False  # Flag to indicate if currently receiving data

def reset_buffers():
    global data_buffer, receiving_data
    data_buffer.clear()
    receiving_data = False

def process_received_data(data):
    # Here you can implement logic to parse and handle the received data
    if data == b'\x12':
        print("LED turned ON")
    elif data == b'\x15':
        print("LED turned OFF")
    else:
        print("Unknown command:", data.hex())

def RPC_Send_Request(data):
    # Construct frame
    header = b'\xAA'  # Unique header byte
    end_pattern = b'\x55'  # Unique end pattern byte
    
    # Open serial port
    ser = serial.Serial(
        port='COM1',  # Change 'COM1' to the appropriate serial port on your laptop
        baudrate=9600,  # Set baud rate as required
        parity=serial.PARITY_NONE,  # No parity
        stopbits=serial.STOPBITS_ONE,  # One stop bit
        bytesize=serial.EIGHTBITS  # 8 data bits
    )
    ser.open()

    # Send header
    ser.write(header)
    time.sleep(0.1)  # Time delimiter

    # Send data
    ser.write(data)
    time.sleep(0.1)  # Time delimiter

    # Send end pattern
    ser.write(end_pattern)
    time.sleep(0.1)  # Time delimiter

    # Close serial port
    ser.close()

def listener_thread():
    global data_buffer, receiving_data

    # Open serial port
    ser = serial.Serial(
        port='COM1',  # Change 'COM1' to the appropriate serial port on your laptop
        baudrate=9600,  # Set baud rate as required
        parity=serial.PARITY_NONE,  # No parity
        stopbits=serial.STOPBITS_ONE,  # One stop bit
        bytesize=serial.EIGHTBITS,  # 8 data bits
        timeout=1  # Set timeout for reading
    )
    ser.open()

    while True:
        # Read data from serial port
        data = ser.read(1)  # Read one byte at a time
        if data:
            # Check if the received byte represents the header byte
            if data[0] == 0xAA:  # Header byte
                reset_buffers()  # Reset data buffer when starting to receive new data
                receiving_data = True
            elif data[0] == 0x55 and receiving_data:  # End pattern byte
                # Stop receiving data when end pattern is received
                receiving_data = False
                # Process received data buffer
                process_received_data(data_buffer)
                reset_buffers()  # Reset data buffer after processing
            elif receiving_data:
                # If currently receiving data, append the byte to the data buffer
                data_buffer.append(data[0])

    # Close serial port
    ser.close()

# Start listener thread
listener = threading.Thread(target=listener_thread, daemon=True)
listener.start()

# Example usage of RPC_Send_Request function
data_to_send = b'\x12'  # Example data to send
RPC_Send_Request(data_to_send)
