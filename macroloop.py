from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
file_name = "positions.txt"

import time
import random

mouse = mouse_controller()
keyboard = keyboard_controller()

def macro():
  with open(file_name, "r") as file:
    content = file.read()

  content = content.split("\n")
  content = [content for content in content if content]

  entries = []
  for item in content:
      x, y = map(int, item.strip("()").split(","))
      entries.append((x, y))

  ring = entries.pop()

  def foodAndSpell():
    randomNumber = random.randint(-2, 2)
    for i in entries:

      randomisedPosition = (i[0] + randomNumber, i[1] + randomNumber )
      mouse.position = randomisedPosition
      time.sleep(0.5)

      mouse.press(Button.left)
      mouse.release(Button.left)
      time.sleep(0.5)
      print (randomisedPosition)
    

  def lifeRing():
    print('Equipping ring')
    randomNumber = random.randint(-2, 2)
      
    randomisedPosition = (ring[0] + randomNumber, ring[1] + randomNumber )
    mouse.position = randomisedPosition
    time.sleep(0.5)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    print (randomisedPosition)

  while True:
    for i in range (101):
      foodAndSpell()
      time.sleep(10)
    lifeRing()
    