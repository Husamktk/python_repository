import os
# specify the directory you want to list
directory_path = '/' #put directory name herre



# list all files and directories in specified paths
content = os.listdir(directory_path)



# print each file and directory name
for item in content:
    print(item)