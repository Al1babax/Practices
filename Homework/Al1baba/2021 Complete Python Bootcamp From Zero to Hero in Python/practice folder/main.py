import os
import shutil
import send2trash

"""print(os.getcwd())
print(os.listdir("C:\\users\\"))
# shutil.move("practice.txt", "C:\\Users\\Alibaba\\PycharmProjects\\ekaharjotus")
print(os.listdir("C:\\Users\\Alibaba\\PycharmProjects\\ekaharjotus"))"""
print(os.listdir())
for folder, sub_folders, files in os.walk("C://Users//Alibaba//PycharmProjects//ekaharjotus//Homework//Al1baba"):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\tSubfolder: {sub_fold}")
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"\tFile: {f}")
    print("\n")




