import os 
import shutil 
import datetime
import time

directory = "/home/alex_player/Python/"
backup_directory = "/home/alex_player/Python/backup"
files = os.listdir(directory)

def perform_backup():

    for file in files:

        file_extension = os.path.splitext(file)[1]
        backup_file = os.path.join(backup_directory,file)

        if os.path.exists(backup_file):
            print(f'{file} already exists in backup, skipping file.')

        elif file_extension == ".py":
            file_path = os.path.join(directory,file)
            shutil.copy(file_path,backup_directory)

        else:
            pass

    backup_contents = os.listdir("/home/alex_player/Python/backup")
    print(f' Python files found {files}')
    print(f'Contents of backup directory {backup_contents}')

while True:

    current_time = datetime.datetime.now()

    if current_time.hour == 16 and current_time.minute == 20:
        perform_backup()
        time.sleep(86400)

    else:
        time.sleep(60)


 