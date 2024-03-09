import subprocess
import os
import shutil

def run_file(path):  
    new_path = os.path.join(path, "Auto.exe") 
    print(new_path)
    executable_file = new_path
# "C:\Users\manis\OneDrive\Desktop\dist\Auto7.exe"
    try:
        subprocess.run([executable_file])
    except FileNotFoundError:
        print(f"Error: {executable_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def ex_file_rm(path):
    directory_path = path 
    print(path)
    try:
        shutil.rmtree(directory_path)
        print(f"{directory_path} and its contents have been successfully deleted.")
    except FileNotFoundError:
        print(f"{directory_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    FILE_PATH=input("ENTER THE FILE PATH")
    path=FILE_PATH.strip('"')
    run_file(path)
    # ex_file_rm(path)
