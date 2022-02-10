### command usage:
### python draw_boundingbox.py -g [input gray file] -c [input colorful file] -o [output file]

### command expamples:
### python draw_boundingbox.py -g ./img/LB_04_EDGE_example.jpg -c ./img/LB_04.jpg -o ./img/LB_04_BD_example.jpg

import cv2
import math
import argparse

# img_path_gray = './img/LB_04_EDGE_example.jpg'
# img_path_color =  './img/LB_04.jpg'
# img_out_path = './img/LB_04_BD_example.jpg'

### img_path_gray => the img that is processed by canny edge detection
### img_path_color => the original img that we draw bounding box on
### img_out_path => the img path(name) that we store the img in

def drawBoundingBox(img_path_gray, img_path_color, img_out_path):

    img = cv2.imread(img_path_gray, cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(img_path_color)
    # cv2.imshow('img', img)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    height, width = img.shape
    # print(height, width)
    line = math.floor(height*width/600000)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w * h > (height * width / 36) and w * h < (height * width / 1.1) and max(w/h, h/w) < 8:
            cv2.rectangle(img_color,(x,y),(x+w,y+h),(100,100,100), line)

    # cv2.imshow('img2', img_color)
    # cv2.waitKey(0)

    cv2.imwrite(img_out_path, img_color)


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Canny')

    parser.add_argument('-g', metavar = 'input gray file', required = True, type = str,
                        help = 'input gray file')
    parser.add_argument('-c', metavar = 'input colorful file', required = True, type = str,
                        help = 'input colorful file')
    parser.add_argument('-o', metavar = 'output file', required = True, type = str,
                        help = 'output file')

    args = parser.parse_args()
    drawBoundingBox(args.g, args.c, args.o)