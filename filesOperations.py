import os

# C:\Users\Damian\Desktop C:\Users\Damian\PycharmProjects\pythonProjectPractice\test.txt

# path = "C:\\Users\\Damian\\Desktop\\test.txt"
# path = "C:\\Users\\Damian\\Desktop"

# lacal path
path = "test.txt"

# FILE DETECTION

if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a folder")
else:
    print("That location doesn't exist")
    with open(path, "x") as file: # CREATE A FILE
        file.write("something\n")

# # COPY FILES
# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile(path, 'test_copy.txt')

# READ A FILE

try:
# with open will automatically close a file
    with open(path) as file:
        print(file.closed)
        print(file.read())
except FileNotFoundError:
    print("File not found.")

print(file.closed)

# WRITE/APPEND TO A FILE

text = "Yooooooooooo\nThis is added text"

# this will overwrite a file
with open(path, 'w') as file:
    file.write(text)

# this will append to a file
text2 = "\nThis will be appended to a file"
with open(path, 'a') as file:
    file.write(text2)




# MOVING FILES

source = path
destination = os.path.curdir + "\\test\\test_moved.txt"
print (destination)

try:
    if os.path.exists(destination):
        print("There is alreay a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(e)
    print(source + " was not found")

# DELETE A FILE
try:
    os.remove("test_copy.txt")
    os.remove("test.txt")
except FileNotFoundError as e:
    print(e)




