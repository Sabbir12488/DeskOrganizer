import colorama
from colorama import Back, Fore, Style
import os
import pathlib
from pathlib import Path
import re
import shutil
import pyfiglet
import preloaded


#default directories
    #source = "C:/Users/User/Desktop"
    #photo_dir = "C:/Users/User/Pictures/From desktop"
    #scr_dir = "C:/Users/User/Pictures/Screenshots"
    #video_dir = "C:/Users/User/Videos/From desktop"
    #txt_dir = "X:/PDFs"
    #gimp_dir = "D:/Gimp saves"

#sets of file extentions
img = {".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".PNG", ".JPG",
       ".gif", ".webp", ".svg", ".avif",".raw",".RAW",".HEIC", ".tif"}

vdo = {".webm", ".MTS", ".M2TS", ".TS", ".mov",".mp4",
       ".m4p", ".m4v", ".mxf", ".avi"}

txt = {".docx", ".doc",".pdf"} ##I did IT!!

saved = {".xcf", ".ai"}

files_moved = 0

item_count = 0

img_count = 0
scr_count = 0
vdo_count = 0
txt_count = 0
save_file_count = 0

colorama.init(autoreset=True)

with open('configurations/header.txt') as Header_txt:
    text = Header_txt.read()
    contents = pyfiglet.figlet_format(text = "DeskOrg", font = "graffiti")
    print(Fore.CYAN + contents)
    print(Fore.BLUE+text)

#oppeing the text file for directory
text_file = open('configurations/directories.txt')
#reading each line in the text
directories = text_file.readlines()
#assigning the veriable
source = directories[2].split('=')
photo_dir = directories[3].split('=')
scr_dir = directories[4].split('=')
video_dir = directories[5].split('=')
txt_dir = directories[6].split('=')
gimp_dir = directories[7].split('=')
dwn_dir = "C:/Users/User/Downloads"
text_file.close()  #closing the text file

#taking permission to oparate
permission = False

# comparing all the files with the file extentions
def is_img(file):
    return os.path.splitext(file)[1] in img
def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in str(name).lower()
def is_vdo(file):
    return os.path.splitext(file)[1] in vdo
def is_txt(file):
    return os.path.splitext(file)[1] in txt
def is_save_files(file):
    return os.path.splitext(file)[1] in saved

os.chdir(source[1].strip())

for file in os.listdir():
    if is_vdo(file) or is_txt(file) or is_img(file) or is_save_files(file) or is_screenshot(file):
       item_count += 1

os.chdir(dwn_dir)

for file in os.listdir():
    if is_vdo(file) or is_txt(file) or is_img(file) or is_save_files(file) or is_screenshot(file):
       item_count += 1

if item_count > 0:
    permission_command = input("Do you want to organize?" + Fore.YELLOW + "[y/n]: " + Fore.RESET)

    if "y" in permission_command.lower():
        permission = True
    elif "n" in permission_command.lower():
        permission = False
    else:
        permission = False




#The actual oparation
if permission == True:

    dsk_dwn = True
    dsk_dwn_command = input(
        "Do you want to organize your Downloads folder?" + Fore.YELLOW + "[y/n]: "+Fore.RESET)
    if "y".lower() in dsk_dwn_command:
        dsk_dwn = False
    else:
        dsk_dwn = True
        os.chdir(source[1].strip())
    if not dsk_dwn:
        source = dwn_dir
        os.chdir(source)

    for file in os.listdir():

        # Moving images
        # checking if the same file exists for screenshot
        if is_screenshot(file):
            if not os.path.exists(os.path.join(scr_dir[1].strip(), file)):
                shutil.move(file, scr_dir[1].strip())
                files_moved += 1
                scr_count += 1
            else:
                print(str(file) + " already exists")
                continue

        elif is_img(file):
            # checking if the same file exists for photos
            if not os.path.exists(os.path.join(photo_dir[1].strip(),file)):
                shutil.move(file, photo_dir[1].strip())
                files_moved += 1
                img_count += 1
            else:
                print(str(file)+" already exists")
                continue

        # Moving videos
        elif is_vdo(file):
            #cheching if duplicate exists
            if not os.path.exists(os.path.join(video_dir[1].strip(), file)):
                shutil.move(file, video_dir[1].strip())
                files_moved += 1
                vdo_count += 1
            else:
                print(str(file)+" already exists")
                continue
        #moving word documents or pdfs
        elif is_txt(file):
            if not os.path.exists(os.path.join(txt_dir[1].strip(), file)):
                shutil.move(file,txt_dir[1].strip())
                files_moved += 1
                txt_count += 1
            else:
                print(str(file) + " already exists")
                continue
        #moving gimp saves (photoshop saves will be added soon)
        elif is_save_files(file):
            if not os.path.exists(os.path.join(gimp_dir[1].strip(), file)):
                shutil.move(file, gimp_dir[1].strip())
                files_moved += 1
                save_file_count += 1
            else:
                print(str(file) + " already exists")
                continue

    if not files_moved == 0:
        print()
        print(Back.MAGENTA + str(files_moved)+f" file(s) moved:"+Back.RESET+" Image: "+Fore.YELLOW+f"{str(img_count)} "+Fore.RESET+ "|| Screenshot: "+Fore.YELLOW+f"{str(scr_count)} "+Fore.RESET+
                                              "|| Video: "+Fore.YELLOW+f"{str(vdo_count)} "+Fore.RESET+"|| Docs: "+Fore.YELLOW+f"{str(txt_count)} "+Fore.RESET+"|| Saves: "+Fore.YELLOW+f"{str(save_file_count)}")
    else:
        print(Back.RED+"There is nothing to move")

    input("Press ENTER to exit")



#for file in os.listdir():
#    count += 1
#    name,ext = os.path.splitext(file)
#
#    name = re.sub(r'[0-9]','', name)
#
#    new_name = f"{count}_{name}{ext}"
#    print(new_name)
#    os.rename(file, new_name)




