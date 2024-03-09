
#include <iostream>
import keyboard

import pyautogui
import time
import os

# Define the folder where your Notepad files are located
FOLDER_PATH = "C:\\Users\\manis\\OneDrive\\Desktop\\testing"

def open_notepad_file(file_number):
    file_name = f"{file_number}.txt"
    file_path = os.path.join(FOLDER_PATH, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                pyautogui.typewrite(cleaned_line)
                pyautogui.press("enter")
    else:
        print(f"File {file_name} not found in the folder.")

def keypress():
    def on_key_event(e):
        key = e.name
        if key.isdigit():
            open_notepad_file(key)

    keyboard.on_press(on_key_event)

    keyboard.wait('end')

def main():
    if os.path.exists(FOLDER_PATH):
        print("FILES FOUND")
        print("Press a numeric key (0-9) to open the corresponding Notepad file.")
        keypress()
    else:
        print("Folder not found. Please set the correct folder path.")
        
if __name__ == "__main__":
    main()
