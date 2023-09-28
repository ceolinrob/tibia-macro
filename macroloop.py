from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
file_name = "positions.txt"

import time
import random
import json


mouse = mouse_controller()
keyboard = keyboard_controller()

with open(file_name, "r") as file:
  content = file.read()

content = content.split("\n")
content = [content for content in content if content]

entries = []

for item in content:
    x, y = map(int, item.strip("()").split(","))
    entries.append((x, y))

def magicLevel():
  ring = entries[2]

  def foodAndSpell():
    randomNumber = random.randint(-2, 2)
    for i in entries[:-2]:

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

def distance():
  food = entries[0]
  ammo = entries[3]
  def useFood():
    randomNumber = random.randint(-2, 2)
    randomisedPosition = (food[0] + randomNumber, food[1] + randomNumber )
    mouse.position = randomisedPosition
    time.sleep(0.5)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    print (randomisedPosition)

  def equipAmmo():
    randomNumber = random.randint(-2, 2)
      
    randomisedPosition = (ammo[0] + randomNumber, ammo[1] + randomNumber )
    mouse.position = randomisedPosition
    time.sleep(0.5)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    print (randomisedPosition)

  while True:
    for i in range (5):
      useFood()
      time.sleep(1)
    for i in range (5):
      equipAmmo()
      time.sleep(1)
    time.sleep(10)
    