# import socket
# import struct
# import RPi.GPIO as GPIO

# # Define GPIO pin number
# GPIO_PIN = 18

# # Initialize GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(GPIO_PIN, GPIO.OUT)

# # Function to handle XCP commands
# def handle_xcp_command(command, data):
#     if command == 0x2F:  # Command to set GPIO pin state
#         pin, state = struct.unpack('BB', data)  # Unpack pin number and state
        
#         # Ensure that the pin is set up as an output
#         GPIO.setup(pin, GPIO.OUT)
        
#         # Check if pin state is different than current state
#         if GPIO.input(pin) != state:
#             GPIO.output(pin, state)
            
#         return b'\xFF'  # Positive response
#     elif command == 0x3F:  # Command to read GPIO pin state
#         pin = struct.unpack('B', data)[0]  # Unpack pin number
#         state = GPIO.input(pin)
#         return bytes([state])  # Respond with the state of the GPIO pin
#     else:
#         return b'\xFE'  # Negative response for unsupported commands

# # Main function to listen for XCP requests
# def main():
#     # Create a TCP/IP socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
#     # Bind the socket to the address
#     server_socket.bind(('0.0.0.0', 9000))  # Adjust port as needed
    
#     # Listen for incoming connections
#     server_socket.listen(1)
    
#     print("XCP server listening on port 9000...")
    
#     while True:
#         # Accept a connection
#         client_socket, client_address = server_socket.accept()
#         print("Connection from:", client_address)
        
#         try:
#             # Receive XCP command and data
#             command = client_socket.recv(1)
#             if not command:  # Check if data is empty
#                 break
#             command = command[0]
#             data_size = client_socket.recv(1)
#             if not data_size:  # Check if data is empty
#                 break
#             data_size = data_size[0]
#             data = client_socket.recv(data_size)
#             if not data:  # Check if data is empty
#                 break

#             # Handle the received XCP command
#             response = handle_xcp_command(command, data)
            
#             # Send response
#             client_socket.sendall(response)
#         finally:
#             # Clean up the connection
#             client_socket.close()

# if __name__ == "__main__":
#     main()

######################################################################
######################################################################



import socket
import struct
import RPi.GPIO as GPIO

# Define GPIO pin number
GPIO_PIN = 18

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

# Function to handle XCP commands
# Function to handle XCP commands
def handle_xcp_command(command, data):
    if command == 0x2F:  # Command to set GPIO pin state
        pin, state = struct.unpack('BB', data)  # Unpack pin number and state
        
        # Ensure that the pin is set up as an output
        GPIO.setup(pin, GPIO.OUT)
        
        # Check if pin state is different than current state
        if GPIO.input(pin) != state:
            GPIO.output(pin, state)
            
        return b'\xFF'  # Positive response
    elif command == 0x3F:  # Command to read GPIO pin state
        pin = struct.unpack('B', data)[0]  # Unpack pin number
        
        # Ensure that the pin is set up as an input
        GPIO.setup(pin, GPIO.IN)
        
        state = GPIO.input(pin)
        return bytes([state])  # Respond with the state of the GPIO pin
    else:
        return b'\xFE'  # Negative response for unsupported commands

# Main function to listen for XCP requests
def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the address
    server_socket.bind(('0.0.0.0', 9000))  # Adjust port as needed
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    print("XCP server listening on port 9000...")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)
        
        try:
            # Receive XCP command and data
            command = client_socket.recv(1)
            if not command:  # Check if data is empty
                break
            command = command[0]
            data_size = client_socket.recv(1)
            if not data_size:  # Check if data is empty
                break
            data_size = data_size[0]
            data = client_socket.recv(data_size)
            if not data:  # Check if data is empty
                break

            # Handle the received XCP command
            response = handle_xcp_command(command, data)
            
            # Send response
            client_socket.sendall(response)
        finally:
            # Clean up the connection
            client_socket.close()

if __name__ == "__main__":
    main()
