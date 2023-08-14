from fetchposition import run
from macroloop import magicLevel
from macroloop import distance
file_name = "positions.txt"
import time



def show_menu():
  print("Tibia macro")
  print("1. Magic Level")
  print("2. Distance")
  print("3. Define mouse positions")
  print("3. Exit")

def option_1():
  magicLevel()

def option_2():
  distance()


def option_3():
  #clears the file
  with open(file_name, "w"):
    pass

  print("Click on food.")
  run()
  time.sleep(0.1)
  print("Click on your spell.")
  run()
  time.sleep(0.1)
  print("Click on your life ring.")
  run()
  time.sleep(0.1)
  print("Click on your ammo / used for distance skill training.")
  run()
  time.sleep(0.1)

def main():
  while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
      option_1()
    elif choice == '2':
      option_2()
    elif choice == '3':
      option_3()
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()