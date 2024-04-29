import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://169.254.226.50:5555")  # Replace with the IP address of your Raspberry Pi

# Function to send GPIO command
def send_gpio_command(gpioNo, status):
    socket.send_string("{},{}".format(gpioNo, status))
    response = socket.recv_string()
    print(response)

# Main function to get user input and send GPIO command
def main():
    while True:
        try:
            gpioNo = int(input("Enter GPIO pin number: "))
            status_str = input("Enter status (High/Low): ").strip().lower()
            status = 1 if status_str == "high" else 0
            if status_str not in ["high", "low"]:
                raise ValueError("Invalid status. Please enter 'High' or 'Low'.")
            send_gpio_command(gpioNo, status)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
