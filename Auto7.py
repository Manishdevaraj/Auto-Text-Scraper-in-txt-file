import keyboard
import pyautogui
import time
import os
import shutil
import sys

FILE_PATH=None

def delete_current_directory(dir_path):
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    # Delete the directory, including all its contents
    try:
        shutil.rmtree(script_dir)
        shutil.rmtree(dir_path)
        print(f"The current directory '{script_dir}' has been deleted.")
    except Exception as e:
        print(f"Failed to delete the directory: {e}")


def write(file_path):
    if file_path is not None:
        time.sleep(0.5)
        for line in open(file_path, "r"):
            pyautogui.typewrite(line)
            pyautogui.press("enter")
    else:
        print("FILE_PATH is not set. Please set the file path first.")
    

def keypress():
    def on_key_event(e):
        key = e.name
        print(f"Key pressed: {key}")
        if key == 'home':
            write(FILE_PATH)
 
    keyboard.on_press(on_key_event)

    keyboard.wait('end')  

def main(file_path):
    
    if os.path.exists(file_path):
        print("FILE FOUND")
        

        print("\n\n\033[5;91m                              YOUR GUI IS PREPARING TO Begin.......\033[0m")
        time.sleep(2)
        print("                                     PRESS ANY KEY TO CHECK......")
        print("                                     BE CONCSIOUS AFTER CLICKING END BUTTON THE WHOLE FILE WILL BE DELETED")

        keypress()

    else:
        print("FILE NOT FOUND RECHECK YOUR PATH! AND PASTE IT CORRECTLY") 
        main()

if __name__ == "__main__":
    # print("ENTER THE CORRECT PATH")
    PATH=input("ENTER THE CORRECT FILE PATH : ")
    path=input("ENTER THE CORRECT DIR PATH : ")
    FILE_PATH=PATH.strip('"')
    dir_path=path.strip('"')
    main(FILE_PATH)
    sys.exit()
    delete_current_directory(dir_path)
