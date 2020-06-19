import string
import os

pd_names = string.ascii_uppercase


valid_drives = list()


req_file = input("Enter the filename: ")


for each_drive in pd_names:
    if(os.path.exists(each_drive+":\\")):
        valid_drives.append(each_drive+":\\")


for each_drive in valid_drives:
    for r,d,f in os.walk(each_drive):
        for each_file in f:
            if each_file == req_file:
                print(os.path.join(r,each_file))
