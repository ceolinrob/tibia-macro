from fetchposition import run
from macroloop import macro
file_name = "positions.txt"
import time



def show_menu():
  print("Tibia macro")
  print("1. Run macro")
  print("2. Define mouse positions")
  print("3. Exit")

def option_1():
  macro()


def option_2():
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

def main():
  while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
      option_1()
    elif choice == '2':
      option_2()
    elif choice == '3':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()