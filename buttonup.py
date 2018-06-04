import time
import RPi.GPIO as GPIO

#initialise a previous input variable to 1 (assume button is set high)
class Box():

  def __init__(self):
    self.buttonpin = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.IN, GPIO.PUD_UP)
    self.buttonpress = GPIO.input(23)
    GPIO.setup(25,GPIO.OUT)
    print(self.buttonpress)
    
  def is_button_up(self):
      #take a reading
      self.led = GPIO.output(25, 0)
      old_state = self.buttonpress
      self.buttonpress = GPIO.input(23)
      try:
        #if the last reading was high and this one low, print
        if ((not old_state) and self.buttonpress):
          time.sleep(1.0)
          self.buttonpress = GPIO.input(23)
          if self.buttonpress == True:
            self.led = GPIO.output(25, 1)
            time.sleep(1.0)
            return True
        return False

      except (KeyboardInterrupt, SystemExit):
         GPIO.cleanup()
      
