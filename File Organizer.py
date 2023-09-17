




import os
import shutil

x = "hello \n"
folder_path = r"C:\Users\Talha Sohail\Downloads"

files = os.listdir(folder_path)
print(files)

paths = [r"C:\Users\Talha Sohail\Downloads\Documents",
         r"C:\Users\Talha Sohail\Downloads\Pictures",
         r"C:\Users\Talha Sohail\Downloads\Audio",
         r"C:\Users\Talha Sohail\Downloads\Other",
         r"C:\Users\Talha Sohail\Downloads\Executables",
         r"C:\Users\Talha Sohail\Downloads\Gif"]



for path in paths: 
   
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(folder_path)

for file in files:
    ext = file.split(".")[-1]


    if ext in ["pdf", "docx", "doc"]:
        shutil.move(folder_path + "\\" + file, paths[0])
    elif ext in ["PNG", "jpg", "jpeg"]:
        shutil.move(folder_path + "\\" + file, paths[1])
    elif ext in ["wav", "MP4"]:
        shutil.move(folder_path + "\\" + file, paths[2])
    elif ext in ["exe", "msi"]:
        shutil.move(folder_path + "\\" + file, paths [3])
    elif ext in ["exe", "msi", "JSON"]:
        shutil.move(folder_path + "\\" + file, paths [4])
    elif ext in ["gif"]:
        shutil.move(folder_path + "\\" + file, paths [5])


print("Files organized")