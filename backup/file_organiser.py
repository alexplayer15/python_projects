import os
import shutil

directory = '/home/alex_player/Python/organised_files/'
files = os.listdir(directory)

extension_list = []

for file in files:
        
    file_extension = os.path.splitext(file)[1]
    extension_list.append(file_extension)

    if file_extension == ".txt":
        file_path = os.path.join(directory,file)
        shutil.move(file_path,'/home/alex_player/Python/organised_files/text_files')

    elif file_extension == ".jpeg":
        file_path = os.path.join(directory,file)
        shutil.move(file_path,'/home/alex_player/Python/organised_files/picture_files')
    
    elif file_extension == ".zip":
        file_path = os.path.join(directory,file)
        shutil.move(file_path,'/home/alex_player/Python/organised_files/zip_files')

    else:
        pass

text_directory = os.listdir('/home/alex_player/Python/organised_files/text_files')
picture_directory = os.listdir('/home/alex_player/Python/organised_files/picture_files')
zip_directory = os.listdir('/home/alex_player/Python/organised_files/zip_files')

print(f' file extensions in organised files {extension_list}')
print(f' current files in {files}')
print(f' files now in text folder {text_directory}')
print(f' files now in picture folder {picture_directory}')
print(f' files now in zip folder {zip_directory}')