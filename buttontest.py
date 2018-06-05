import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN, pull_up_down = GPIO.PUD_UP)
#initialise a previous input variable to 0 (assume button is set high/up/true)
prev_input = 1
while True:
  #take a reading
  input = GPIO.input(23)
  #if the last reading was high/up/ture and this one low/down/false, print
  if ((not prev_input) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
