# Write a python program to print the contents of a directory using the os module. Search online for the function which does that?

# Import the os module
import os

# Specify the directory path
directory = "/"

# Get the list of files and folders in the directory
contents = os.listdir(directory)

# Print heading
print("Contents of the directory are:")

# Print each file/folder name
for item in contents:
    print(item)