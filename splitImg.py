### Spliting images into 2 (train, val)
### Or go to app.roboflow.com to build your own dataset and split them with ease (recommended)

import os
import fnmatch
import random
from shutil import copyfile

input_path = "./temple_resized_labeled/"
dirs = os.listdir(input_path)

output_train_path = "./custom_dataset/train/"
output_val_path = "./custom_dataset/val/"

split = 0.2

def jpg2txt(item):
    tar = 'jpg'
    temp = ''
    for i in item:
        if i not in tar:
            temp += i
    return(temp + 'txt')

def txt2jpg(item):
    tar = 'tx'
    temp = ''
    for i in item:
        if i not in tar:
            temp += i
    return(temp + 'jpg')

def splitImg():

    if os.path.isdir(output_train_path) == False:
        os.makedirs(output_train_path)
    if os.path.isdir(output_val_path) == False:
        os.makedirs(output_val_path)

    img_num = (len(dirs) - 2) / 2

    train_num = int(img_num * (1 - split))
    val_num = img_num - train_num
    print("img count : {0}, train img : {1}, val img : {2}".format(img_num, train_num, val_num))

    train_count = 0
    val_count = 0

    for img in dirs:
        if fnmatch.fnmatch(img, '*.jpg'):
            img_txt = jpg2txt(img)
            if((random.randrange(5) < 4 and train_count < train_num) or (val_count >= val_num)):
                copyfile(input_path + img, output_train_path + img)
                copyfile(input_path + img_txt, output_train_path + img_txt)
                train_count += 1
            else:
                copyfile(input_path + img, output_val_path + img)
                copyfile(input_path + img_txt, output_val_path + img_txt)
                val_count += 1


    print("operation done!!! training img : {0}, validation img : {1}".format(len(os.listdir(output_train_path))/2, len(os.listdir(output_val_path))/2))

splitImg()