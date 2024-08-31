import os

# Replace this path with the actual path to your image file
file_path = 'test_image.png'

try:
    # Get the file permissions
    permissions = os.stat(file_path).st_mode
    # Print permissions in octal format
    print(f"Permissions for {file_path}: {oct(permissions)}")
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")