import os

#path = r"E:\demos\files\reports\\"
path = r"C:\$WINDOWS.~BT\Sources\\"
for file_name in os.listdir(path):
# construct full file path
    file = path + file_name
    if os.path.isfile(file):
        print('Deleting file:', file)
        os.remove(file)
