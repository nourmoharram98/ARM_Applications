import RPi.GPIO as GPIO
import zmq

GPIO.setmode(GPIO.BCM)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def set_gpio_pin(gpioNo, status):
    GPIO.setup(gpioNo, GPIO.OUT)
    GPIO.output(gpioNo, status)
    return "GPIO {} set to {}".format(gpioNo, "High" if status else "Low")

while True:
    message = socket.recv_string()
    gpioNo, status = message.split(',')
    gpioNo = int(gpioNo)
    status = int(status)
    response = set_gpio_pin(gpioNo, status)
    socket.send_string(response)
