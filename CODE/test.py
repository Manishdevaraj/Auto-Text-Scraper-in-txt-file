import os
def run(path):
    path = path.strip('"')  # Remove surrounding double quotes if present
    new_path = os.path.join(path, "auto")
    new_path = f'"{new_path}"'  # Add double quotes around the updated path
    print(f"Updated path: {new_path}")

if __name__ == "__main__":
    path = input("Enter a path: ")
    run(path)

