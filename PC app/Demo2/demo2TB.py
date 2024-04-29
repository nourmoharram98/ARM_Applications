####################################################################################
    # import socket
    # import struct

    # # Function to send XCP command
    # def send_xcp_command(pin, state):
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Prepare XCP command data
    #         data = struct.pack('BB', pin, state)
            
    #         # Send XCP command and data
    #         client_socket.sendall(bytes([0x2F]))  # Command to set GPIO pin state
    #         client_socket.sendall(bytes([len(data)]))  # Data size
    #         client_socket.sendall(data)  # Pin number and state
            
    #         # Receive response
    #         response = client_socket.recv(1)
    #         if response == b'\xFF':
    #             print("Command executed successfully.")
    #         else:
    #             print("Command execution failed.")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to send command to read GPIO pin state
    # def read_gpio(pin):
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Send command to read GPIO pin state
    #         client_socket.sendall(bytes([0x3F]))  # Command to read GPIO pin state
    #         client_socket.sendall(bytes([1]))     # Data size
    #         client_socket.sendall(bytes([pin]))   # Pin number
            
    #         # Receive GPIO state
    #         state = client_socket.recv(1)[0]
    #         print("GPIO pin", pin, "is", "High" if state else "Low")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # def main():
    #     while True:
    #         try:
    #             choice = input("Enter 's' to set GPIO pin state, 'r' to read GPIO pin state: ")
    #             if choice == 's':  # Set GPIO pin state
    #                 pin = int(input("Enter GPIO pin number: "))
    #                 state_str = input("Enter GPIO state (High/Low): ").strip().lower()
    #                 state = 1 if state_str == "high" else 0
    #                 if state_str not in ["high", "low"]:
    #                     raise ValueError("Invalid GPIO state. Please enter 'High' or 'Low'.")
                    
    #                 # Send XCP command to set GPIO state
    #                 send_xcp_command(pin, state)
    #             elif choice == 'r':  # Read GPIO pin state
    #                 pin = int(input("Enter GPIO pin to read: "))
    #                 read_gpio(pin)
    #         except KeyboardInterrupt:
    #             print("\nExiting...")
    #             break
    #         except ValueError as e:
    #             print(e)
    #         except Exception as e:
    #             print("An error occurred:", e)

    # if __name__ == "__main__":
    #     main()



    ################################################################
    ################################################################

    # import socket
    # import struct
    # import time
    # import os

    # # Function to set GPIO pin state
    # def set_gpio(pin, state, log_file):
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Prepare XCP command data
    #         data = struct.pack('BB', pin, state)
            
    #         # Send XCP command and data
    #         client_socket.sendall(bytes([0x2F]))  # Command to set GPIO pin state
    #         client_socket.sendall(bytes([len(data)]))  # Data size
    #         client_socket.sendall(data)  # Pin number and state
            
    #         # Receive response
    #         response = client_socket.recv(1)
    #         if response == b'\xFF':
    #             log_file.write(f"{get_timestamp()} - Test 1 by karim: GPIO pin {pin} set to {'High' if state else 'Low'} successfully.\n")
    #         else:
    #             log_file.write(f"{get_timestamp()} - Test 1 by karim: Failed to set GPIO pin state.\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to send command to read GPIO pin state
    # def read_gpio(pin, log_file):
    #     # Validate the pin number
    #     if not (0 <= pin <= 27):  # Adjust pin range as per your GPIO setup
    #         log_file.write(f"{get_timestamp()} - Test 1 by karim: Invalid pin number.\n")
    #         return
        
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Send command to read GPIO pin state
    #         client_socket.sendall(bytes([0x3F]))  # Command to read GPIO pin state
    #         client_socket.sendall(bytes([1]))     # Data size
    #         client_socket.sendall(bytes([pin]))   # Pin number
            
    #         # Receive GPIO state
    #         state = client_socket.recv(1)[0]
    #         log_file.write(f"{get_timestamp()} - Test 1 by karim: Read pin {pin} = {'High' if state else 'Low'}\n")
    #     except Exception as e:
    #         log_file.write(f"{get_timestamp()} - Test 1 by karim: An error occurred during GPIO read: {e}\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to get current timestamp
    # def get_timestamp():
    #     return time.strftime("%Y-%m-%d %H:%M:%S")

    # # Function to wait for a specified duration in milliseconds
    # def wait_ms(milliseconds):
    #     time.sleep(milliseconds / 1000.0)

    # # Function to run the test
    # def test():
    #     script_dir = os.path.dirname(os.path.abspath(__file__))
    #     log_file_path = os.path.join(script_dir, "test_log.txt")
        
    #     with open(log_file_path, "a") as log_file:
    #         log_file.write(f"{get_timestamp()} - Test 9 by Team1: Starting test...\n")
    #         try:
    #             set_gpio(17, 0, log_file)  # Set pin 17 Low
    #             wait_ms(10)
    #             read_gpio(27, log_file)  # Read pin 27
    #             wait_ms(250)
    #             set_gpio(17, 1, log_file)  # Set pin 17 High
    #             wait_ms(10)
    #             read_gpio(27, log_file)  # Read pin 27
    #         except Exception as e:
    #             log_file.write(f"{get_timestamp()} - Test 1 by Team1: An error occurred during test: {e}\n")
    #         finally:
    #             log_file.write(f"{get_timestamp()} - Test 1 by Team1: Test completed.\n")

    # if __name__ == "__main__":
    #     input("To run the test, press Enter...")
    #     test()

    ##################################################################



    # import socket
    # import struct
    # import time
    # import os

    # # Function to set GPIO pin state
    # def set_gpio(pin, state, log_file):
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Prepare XCP command data
    #         data = struct.pack('BB', pin, state)
            
    #         # Send XCP command and data
    #         client_socket.sendall(bytes([0x2F]))  # Command to set GPIO pin state
    #         client_socket.sendall(bytes([len(data)]))  # Data size
    #         client_socket.sendall(data)  # Pin number and state
            
    #         # Receive response
    #         response = client_socket.recv(1)
    #         if response == b'\xFF':
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: GPIO pin {pin} set to {'High' if state else 'Low'} successfully.\n")
    #         else:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Failed to set GPIO pin state.\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to send command to read GPIO pin state
    # def read_gpio(pin, log_file):
    #     # Validate the pin number
    #     if not (0 <= pin <= 27):  # Adjust pin range as per your GPIO setup
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Invalid pin number.\n")
    #         return
        
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Send command to read GPIO pin state
    #         client_socket.sendall(bytes([0x3F]))  # Command to read GPIO pin state
    #         client_socket.sendall(bytes([1]))     # Data size
    #         client_socket.sendall(bytes([pin]))   # Pin number
            
    #         # Receive GPIO state
    #         state = client_socket.recv(1)[0]
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Read pin {pin} = {'High' if state else 'Low'}\n")
    #         return state
    #     except Exception as e:
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during GPIO read: {e}\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to get current timestamp
    # def get_timestamp():
    #     return time.strftime("%Y-%m-%d %H:%M:%S")

    # # Function to wait for a specified duration in milliseconds
    # def wait_ms(milliseconds):
    #     time.sleep(milliseconds / 1000.0)

    # # Function to run the test
    # def test():
    #     global test_number
    #     global tester_name
    #     test_number = 1
    #     tester_name = "Team1"
    #     script_dir = os.path.dirname(os.path.abspath(__file__))
    #     log_file_path = os.path.join(script_dir, "test_log.txt")
        
    #     with open(log_file_path, "a") as log_file:
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Starting test...\n")
    #         try:
    #             # Set pin 17 Low
    #             set_gpio(17, 0, log_file)
    #             wait_ms(10)
                
    #             # Read pin 27
    #             pin_27_state_low = read_gpio(27, log_file)
    #             wait_ms(250)
                
    #             # Set pin 17 High
    #             set_gpio(17, 1, log_file)
    #             wait_ms(10)
                
    #             # Read pin 27
    #             pin_27_state_high = read_gpio(27, log_file)
                
    #             # Test condition
    #             if pin_27_state_low and not pin_27_state_high:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
    #             elif not pin_27_state_low and pin_27_state_high:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
    #             else:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test failed. Conditions not met.\n")
    #         except Exception as e:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during test: {e}\n")
    #         finally:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test completed.\n")

    # if __name__ == "__main__":
    #     input("To run the test, press Enter...")
    #     test()



    ########################################################



    # import socket
    # import struct
    # import time
    # import os
    # import tkinter as tk

    # # Function to set GPIO pin state
    # def set_gpio(pin, state, log_file):
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Prepare XCP command data
    #         data = struct.pack('BB', pin, state)
            
    #         # Send XCP command and data
    #         client_socket.sendall(bytes([0x2F]))  # Command to set GPIO pin state
    #         client_socket.sendall(bytes([len(data)]))  # Data size
    #         client_socket.sendall(data)  # Pin number and state
            
    #         # Receive response
    #         response = client_socket.recv(1)
    #         if response == b'\xFF':
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: GPIO pin {pin} set to {'High' if state else 'Low'} successfully.\n")
    #         else:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Failed to set GPIO pin state.\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to send command to read GPIO pin state
    # def read_gpio(pin, log_file):
    #     # Validate the pin number
    #     if not (0 <= pin <= 27):  # Adjust pin range as per your GPIO setup
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Invalid pin number.\n")
    #         return
        
    #     # Create a TCP/IP socket
    #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    #     try:
    #         # Connect to the server
    #         client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
            
    #         # Send command to read GPIO pin state
    #         client_socket.sendall(bytes([0x3F]))  # Command to read GPIO pin state
    #         client_socket.sendall(bytes([1]))     # Data size
    #         client_socket.sendall(bytes([pin]))   # Pin number
            
    #         # Receive GPIO state
    #         state = client_socket.recv(1)[0]
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Read pin {pin} = {'High' if state else 'Low'}\n")
    #         return state
    #     except Exception as e:
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during GPIO read: {e}\n")
    #     finally:
    #         # Clean up the connection
    #         client_socket.close()

    # # Function to get current timestamp
    # def get_timestamp():
    #     return time.strftime("%Y-%m-%d %H:%M:%S")

    # # Function to wait for a specified duration in milliseconds
    # def wait_ms(milliseconds):
    #     time.sleep(milliseconds / 1000.0)

    # # Function to run the test
    # def run_test():
    #     global test_number
    #     global tester_name
    #     test_number = 1
    #     tester_name = "Team1"
    #     script_dir = os.path.dirname(os.path.abspath(__file__))
    #     log_file_path = os.path.join(script_dir, "test_log.txt")
        
    #     with open(log_file_path, "a") as log_file:
    #         log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Starting test...\n")
    #         try:
    #             # Set pin 17 Low
    #             set_gpio(17, 0, log_file)
    #             wait_ms(10)
                
    #             # Read pin 27
    #             pin_27_state_low = read_gpio(27, log_file)
    #             wait_ms(250)
                
    #             # Set pin 17 High
    #             set_gpio(17, 1, log_file)
    #             wait_ms(10)
                
    #             # Read pin 27
    #             pin_27_state_high = read_gpio(27, log_file)
                
    #             # Test condition
    #             if pin_27_state_low and not pin_27_state_high:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
    #                 result_label.config(text="Test Passed", fg="green")
    #             elif not pin_27_state_low and pin_27_state_high:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
    #                 result_label.config(text="Test Passed", fg="green")
    #             else:
    #                 log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test failed. Conditions not met.\n")
    #                 result_label.config(text="Test Failed", fg="red")
    #         except Exception as e:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during test: {e}\n")
    #             result_label.config(text="Test Failed", fg="red")
    #         finally:
    #             log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test completed.\n")

    # # Create GUI
    # root = tk.Tk()
    # root.title("Test GUI")

    # test_button = tk.Button(root, text="Run Test", command=run_test)
    # test_button.pack(pady=10)

    # result_label = tk.Label(root, text="", fg="black")
    # result_label.pack()

    # root.mainloop()
####################################################################################


import socket
import struct
import time
import os
import tkinter as tk

# Function to set GPIO pin state
def set_gpio(pin, state, log_file):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
        
        # Prepare XCP command data
        data = struct.pack('BB', pin, state)
        
        # Send XCP command and data
        client_socket.sendall(bytes([0x2F]))  # Command to set GPIO pin state
        client_socket.sendall(bytes([len(data)]))  # Data size
        client_socket.sendall(data)  # Pin number and state
        
        # Receive response
        response = client_socket.recv(1)
        if response == b'\xFF':
            log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: GPIO pin {pin} set to {'High' if state else 'Low'} successfully.\n")
        else:
            log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Failed to set GPIO pin state.\n")
    finally:
        # Clean up the connection
        client_socket.close()

# Function to send command to read GPIO pin state
def read_gpio(pin, log_file):
    # Validate the pin number
    if not (0 <= pin <= 27):  # Adjust pin range as per your GPIO setup
        log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Invalid pin number.\n")
        return
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect(('169.254.226.50', 9000))  # Adjust IP address and port
        
        # Send command to read GPIO pin state
        client_socket.sendall(bytes([0x3F]))  # Command to read GPIO pin state
        client_socket.sendall(bytes([1]))     # Data size
        client_socket.sendall(bytes([pin]))   # Pin number
        
        # Receive GPIO state
        state = client_socket.recv(1)[0]
        log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Read pin {pin} = {'High' if state else 'Low'}\n")
        return state
    except Exception as e:
        log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during GPIO read: {e}\n")
    finally:
        # Clean up the connection
        client_socket.close()

# Function to get current timestamp
def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

# Function to wait for a specified duration in milliseconds
def wait_ms(milliseconds):
    time.sleep(milliseconds / 1000.0)

# Function to run the test
def run_test():
    global test_number
    global tester_name
    test_number = 1
    tester_name = "Team1"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, "test_log.txt")
    
    input_pin = int(input_pin_entry.get())
    output_pin = int(output_pin_entry.get())
    
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Starting test...\n")
        try:
            # Set output pin Low
            set_gpio(output_pin, 0, log_file) #press
            wait_ms(10)
            
            # Read input pin
            input_pin_state = read_gpio(input_pin, log_file) #read led pin
            wait_ms(250)
            
            # Set output pin High
            set_gpio(output_pin, 1, log_file)       #release
            wait_ms(10)
            
            # Read input pin
            input_pin_state_2 = read_gpio(input_pin, log_file)
            
            # Test condition
            if input_pin_state and not input_pin_state_2:
                log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
                result_label.config(text="Test Passed", fg="green")
            elif not input_pin_state and input_pin_state_2:
                log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test passed.\n")
                result_label.config(text="Test Passed", fg="green")
            else:
                log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test failed. Conditions not met.\n")
                result_label.config(text="Test Failed", fg="red")
        except Exception as e:
            log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: An error occurred during test: {e}\n")
            result_label.config(text="Test Failed", fg="red")
        finally:
            log_file.write(f"{get_timestamp()} - Test {test_number} by {tester_name}: Test completed.\n")

# Create GUI
root = tk.Tk()
root.title("Test GUI")

input_pin_label = tk.Label(root, text="Input Pin:")
input_pin_label.pack()
input_pin_entry = tk.Entry(root)
input_pin_entry.pack()

output_pin_label = tk.Label(root, text="Output Pin:")
output_pin_label.pack()
output_pin_entry = tk.Entry(root)
output_pin_entry.pack()

test_button = tk.Button(root, text="Run Test", command=run_test)
test_button.pack(pady=10)

result_label = tk.Label(root, text="", fg="black")
result_label.pack()

root.mainloop()

