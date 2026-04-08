# Q) Write a python program to print the directory using the OS module Seach Online for the function which Does That .
# Q) Label the comment .
import os

# specify path (you can change this)
path = "."

# get list of files and directories
files = os.listdir(path)

# print each item
for file in files:
    print(file)