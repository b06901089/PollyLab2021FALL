### command usage:
### python canny_edge_detection.py -i [input file] -o [output file]

### command expamples:
### python canny_edge_detection.py -i ./img/BL_01.jpg -o ./img/BL_01_EDGE_01.jpg
### output expamples:
### ../
###   canny_edge_detection.py
###   img/
###     BL_01.jpg
###     BL_01_EDGE_01.jpg

### Reference:
### https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123


import numpy as np
import cv2
from scipy import signal
from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt
import argparse

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

def sobel_filters(img):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    
    Ix = ndimage.filters.convolve(img, Kx)
    Iy = ndimage.filters.convolve(img, Ky)
    
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)
    
    return (G, theta)

def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
                #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z

def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)

def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img

def canny(img_path, img_out_path):

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    grad = signal.convolve2d(img, gaussian_kernel(5, 1.4), boundary='symm')
    grad = cv2.normalize(grad.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    print("convolution done")

    #####   OpenCV stores images in BGR order instead of RGB                             
    #####   But this img is grayscale so it is fine to use plt without transmformation   
    #####   still not sure why cv2.imshow() here fails                                   

    #####   (Update)                                                                     
    #####   I know why cv2.imshow() here fails                                           
    #####   plz refer to https://www.mathworks.com/matlabcentral/answers/88934-images-don-t-show-with-imshow-after-converting-them-to-double for more 

    # gaussian = cv2.GaussianBlur(img,(5,5),1)
    #####  There is default gaussian blur in CV module                                  


    G, theta = sobel_filters(grad)
    # print(np.shape(G))
    # print(np.shape(theta))
    #####   G is the magnitude of the gradient
    #####   theta is the slope of the gradient

    img3 = non_max_suppression(G, theta)
    img_res, img_weak, img_strong = threshold(img3, 0.7, 0.2)
    img7 = hysteresis(img_res, img_weak, img_strong)

    # print(img)
    # print(grad)
    # print(gaussian)

    # cv2.imshow('My Image Grayscale guassain blur', grad)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print("start drawing")

    # plt.subplot(221), plt.imshow(img,cmap='gray'), plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222), plt.imshow(grad,cmap='gray'), plt.title('Blurred')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223), plt.imshow(G,cmap='gray'), plt.title('G')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(224), plt.imshow(theta,cmap='gray'), plt.title('theta')
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    # plt.subplot(221), plt.imshow(img4,cmap='gray'), plt.title('0.1, 0.35')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222), plt.imshow(img5,cmap='gray'), plt.title('0.3, 0.35')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223), plt.imshow(img6,cmap='gray'), plt.title('0.5, 0.35')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(224), plt.imshow(img7,cmap='gray'), plt.title('0.7, 0.35')
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    # cv2.imwrite(img_out_path1, img4)
    # cv2.imwrite(img_out_path2, img5)
    # cv2.imwrite(img_out_path3, img6)
    
    cv2.imwrite(img_out_path, img7)


# canny('./img/LB_05.jpg', './img/LB_05_EDGE_01.jpg')
# canny('./img/BL_01.jpg', './img/BL_01_EDGE_01.jpg')
# canny('./img/BL_02.jpg', './img/BL_02_EDGE_01.jpg')

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Canny')

    parser.add_argument('-i', metavar = 'input file name', required = True, type = str,
                        help = 'input directory')
    parser.add_argument('-o', metavar = 'output file name', required = True, type = str,
                        help = 'output directory')

    args = parser.parse_args()
    canny(args.i, args.o)