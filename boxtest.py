import buttonup
import time

if __name__ == '__main__':
  box = buttonup.Box()
  print("waiting for button press")
  print(box.is_button_up())
  while True:
    if box.is_button_up():
      if not True:
        print ("box is locked")
        print(box.is_button_up())
      else:
        print ("box is unlocked")
        print(box.is_button_up())
        
