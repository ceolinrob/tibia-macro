from pynput.mouse import Button, Controller, Listener
import time
file_name = "positions.txt"
mouse = Controller()

def run(): 
  def click(x, y, button, pressed):

      with open(file_name, "a") as file:
        file.write(format(mouse.position))
        file.write('\n')

      listener.stop()

  with Listener(on_click=click) as listener:
      listener.join()