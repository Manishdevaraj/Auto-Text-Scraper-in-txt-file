import keyboard
import pyautogui
import time
import os

FILE_PATH = None
str_file = ""
typing_enabled = False # Variable to control typing
def open_notepad_file(file_n):
    file_name = f"{file_n}.txt"
    file_path = os.path.join(FILE_PATH, file_name)
    if os.path.exists(file_path):
        write(file_path)
    else:    
     print(f"File {file_name} not found in the folder.")


def write(file_path):
    if file_path is not None:
        with open(file_path, "r") as file:
            for line in file:   
                cleaned_line = line.strip()  
                pyautogui.typewrite(cleaned_line)
                pyautogui.press("enter")            
    else:
        print("FILE_PATH is not set. Please set the file path first.")

def keypress():
    def on_key_event(e):
        global str_file
        print(str_file)
        global typing_enabled
        key = e.name
        print(f"Key pressed: {key}")
        if key=='home':
           open_notepad_file(str_file)
           str_file=""
        if key == 'insert':
            typing_enabled = not typing_enabled  # Toggle typing state
        elif typing_enabled:
            str_file += key  # Store the key in str_file
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
        print("FILE NOT FOUND. RECHECK YOUR PATH AND PASTE IT CORRECTLY.")
        main()

if __name__ == "__main__":
    PATH = input("ENTER THE CORRECT FILE PATH : ")
    FILE_PATH = PATH.strip('"')
    main(FILE_PATH)
