import os
import datetime
import sys


file_path = input("Enter the file path: ")
age_of_files = int(input("Enter the files to look for before certain number of days: "))
today = datetime.datetime.now()

if os.path.exists(file_path):
    if os.path.isdir(file_path):
        for each_file in os.listdir(file_path):
            each_file_path = os.path.join(file_path,each_file)
            if os.path.isfile(each_file_path):
                # The getctime gives seconds so we need to convert it to a date and time using fromtimestamp module
                file_create_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
                diff_days = (today - file_create_date).days
                if diff_days > age_of_files:
                    print(each_file_path, diff_days)
    else:
        print(f"The path {file_path} is not a directory")
        sys.exit(3)
else:
    print(f"The path {file_path} does not exist")
    sys.exit(1)

    
        
