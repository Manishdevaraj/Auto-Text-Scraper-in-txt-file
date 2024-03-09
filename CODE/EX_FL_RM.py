import os

file_path = "C:\\Users\\manis\\OneDrive\\Desktop\\dist.zip"

try:
    os.remove(file_path)
    print(f"{file_path} has been successfully deleted.")
except FileNotFoundError:
    print(f"{file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
