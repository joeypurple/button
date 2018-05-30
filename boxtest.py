import buttonup
import time

if __name__ == '__main__':
  box = buttonup.Box()
  print("waiting for button press")
  while True:
    if box.is_button_up():
      if not True:
        print ("box is locked")
      else:
        print ("box is unlocked")
        
