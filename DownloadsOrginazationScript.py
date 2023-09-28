# This is a sample Python script that will organize the Downloads folder based on type of extension of the file
# Just replace *username* with your username to use. Written in Pycharm and on Windows 11. 
import os
import shutil

path = "C://Users/*username*/Downloads/"
otherFolder = "C://Users/*username*/Downloads/Other"
imagesFolder = "C://Users/*username*/Downloads/Images"
executablesFolder = "C://Users/*username*/Downloads/Executables"
pdfsFolder = "C://Users/*username*/Downloads/PDFs"
textfilesFolder = "C://Users/*username*/Downloads/TextFiles"
dir_list = os.listdir(path)
files = [f for f in dir_list if os.path.isfile(path+'/'+f)]


if __name__ == '__main__':
    print("Files in '", path, "' :")
    print(files)

for x in files:
    print(x + "file being moved")
    if x.endswith(".txt"):
        shutil.move(path+x, textfilesFolder)
    elif x.endswith(".pdf"):
        shutil.move(path+x, pdfsFolder)
    elif x.endswith(".exe"):
        shutil.move(path+x, executablesFolder)
    elif x.endswith(".jpg"):
        shutil.move(path+x, imagesFolder)
    elif x.endswith(".JPEG"):
        shutil.move(path + x, imagesFolder)
    else:
        shutil.move(path+x, otherFolder)