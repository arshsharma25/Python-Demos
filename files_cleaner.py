import os
import sys


location = input("Enter the path needed for cleaning data: ")


if os.path.exists(location):
    for r,d,f in os.walk(location):
        if os.path.isdir(r):
            for file in os.listdir(r):
                print(file)
else:
    print("Incorrect path")
    exit



