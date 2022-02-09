### Find the jpg images with txt files (the YOLO format of label files)
### Use image labling tools to label images
### Or go to app.roboflow.com to upload images and label them

### example

### input_folder:
### 1.jpg
### 2.jpg
### 2.txt
### 3.jpg
### 4.jpg
### 4.txt
### 5.jpg
### 6.jpg
### 7.jpg

### output_folder:
### 2.jpg
### 2.txt
### 4.jpg
### 4.txt

from PIL import Image, ImageFile
import os, os.path
import fnmatch

ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "./temple_resized/"
des_path = "./temple_resized_labeled/"
dirs = os.listdir(path)

def txt2jpg(item):
    tar = 'tx'
    temp = ''
    for i in item:
        if i not in tar:
            temp += i
    return(temp + 'jpg')

def rename():
    for idx, item in enumerate(dirs):
        if fnmatch.fnmatch(item, '*.txt'):
            itemjpg = txt2jpg(item)
            os.rename(path + item, des_path + item)
            if os.path.isfile(path + itemjpg):
                os.rename(path + itemjpg, des_path + itemjpg)

rename()