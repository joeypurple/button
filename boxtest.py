import buttonup
import time

if __name__ == '__main__':
  box = buttonup.Box()
  print("waiting for button press")
  print(box.buttonpress)
  while True:
    if box.is_button_up():
        print ("box is unlocked")
