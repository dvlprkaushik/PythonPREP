import os

dir_path = '/Users'
dir_contents = os.listdir(dir_path)
for item in dir_contents:
    print(item)