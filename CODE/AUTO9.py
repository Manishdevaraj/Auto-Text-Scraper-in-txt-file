import keyboard
import pyautogui
import time
import os

FILE_PATH = None

typing_enabled = True  # Variable to control typing

def write(file_path):
    typing_enabled=True
    if file_path is not None:
        # time.sleep(0.5)
        with open(file_path, "r") as file:
            for line in file:
                if typing_enabled:
                    pyautogui.typewrite(line)
                    pyautogui.press("enter")
                else:
                    break
    else:
        print("FILE_PATH is not set. Please set the file path first.")

def keypress():
    def on_key_event(e):
        global typing_enabled
        key = e.name
        print(f"Key pressed: {key}")
        if key == 'home':
            write(FILE_PATH)
        elif key == 'ctrl':
            typing_enabled = not typing_enabled  # Toggle typing state

    keyboard.on_press(on_key_event)

    keyboard.wait('end')

def main(file_path):
    if os.path.exists(file_path):
        print("FILE FOUND")
        print("\n\n\033[5;91m                              YOUR GUI IS PREPARING TO Begin.......\033[0m")
        time.sleep(2)
        print("                                     PRESS ANY KEY TO CHECK......")
        print("                                     BE CONSCIOUS AFTER CLICKING END BUTTON THE WHOLE FILE WILL BE DELETED")
        keypress()
    else:
        print("FILE NOT FOUND RECHECK YOUR PATH! AND PASTE IT CORRECTLY")
        main()

if __name__ == "__main__":
    PATH = input("ENTER THE CORRECT FILE PATH : ")
    FILE_PATH = PATH.strip('"')
    main(FILE_PATH)
