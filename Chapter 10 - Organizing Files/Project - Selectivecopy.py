import os
from shutil import copy
for folderName, subfolders, filenames in os.walk('/home/ash/amfoss-tasks'):
    for filename in filenames:
        if filename[-4:] == ".png" or filename[-4:] ==".jpg":
            path = folderName+"/"+filename
            copy(path, '/home/ash/backup')

            
