# import os

# # Specify the directory you want to list
# directory_path = "/"  # "." refers to the current directory

# try:
#     # List all contents in the specified directory
#     contents = os.listdir(directory_path)
#     print("Contents of the directory:")
#     for item in contents:
#         print(item)
# except FileNotFoundError:
#     print("The specified directory does not exist.")
# except PermissionError:
#     print("You do not have permission to access this directory.")

import os
directory_path = '/'


content = os.listdir(directory_path)

for item in content:
    print(item)