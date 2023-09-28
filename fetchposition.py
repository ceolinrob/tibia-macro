from pynput.mouse import Button, Controller, Listener
import time
file_name = "positions.json"
mouse = Controller()

def run(data, attr): 
  def click(x, y, button, pressed):

    data[attr] = format(mouse.position)
    with open(file_name, "w") as file:
      json.dump(data, file, indent=4)

    listener.stop()

  with Listener(on_click=click) as listener:
      listener.join()