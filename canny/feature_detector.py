### command usage:
### python feature_detector.py -i1 [image 1] -i2 [image 2]

### command expamples:
### python feature_detector.py -i1 ./img/LB_03 -i2 ./img/LB_01

### ERROR NOT FIXED:
### AttributeError: module 'cv2' has no attribute 'xfeatures2d'

import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt
# from object_detection import canny_edge_detection

def featureDetector(img_path1, img_path2):

    # img1 = cv2.imread('/Users/tasiyuchien/Downloads/Polly meeting/object_detection/img/LB_05_EDGE.jpg',0)
    # img2 = cv2.imread('/Users/tasiyuchien/Downloads/Polly meeting/object_detection/img/LB_04_EDGE.jpg',0)

    img1 = cv2.imread(img_path1, 0)
    img2 = cv2.imread(img_path2, 0)

    # Initiate STAR detector
    orb = cv2.ORB_create(100000)

    # find the keypoints with ORB
    kp1 = orb.detect(img1, None)
    kp2 = orb.detect(img2, None)

    descriptor = cv2.xfeatures2d.BEBLID_create(0.75)
    # compute the descriptors with ORB
    kp1, des1 = descriptor.compute(img1, kp1)
    kp2, des2 = descriptor.compute(img2, kp2)

    # kp1, des1 = orb.detectAndCompute(img1, None)
    # kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING)
    # matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)

    # Match descriptors.
    # matches = bf.match(des1, des2)
    nn_matches = matcher.knnMatch(des1, des2, 2)

    # Sort them in the order of their distance.
    # matches = sorted(matches, key = lambda x:x.distance)
    good_matches = []
    nn_match_ratio = 0.8  # Nearest neighbor matching ratio
    for m, n in nn_matches:
        if m.distance < nn_match_ratio * n.distance:
            good_matches.append(m)

    # # draw only keypoints location,not size and orientation
    # img3 = cv2.drawKeypoints(img1, kp1, img1, color=(0,255,0), flags=0)

    # Draw first 10 matches.
    # img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], flags=2, outImg=None)
    img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
    cv2.drawMatches(img1, kp1, img2, kp2, good_matches, img_matches, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    plt.imshow(img_matches),plt.show()


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Canny')

    parser.add_argument('-i1', metavar = 'image 1', required = True, type = str,
                        help = 'image 1')
    parser.add_argument('-i2', metavar = 'image 2', required = True, type = str,
                        help = 'image 2')

    args = parser.parse_args()
    featureDetector(args.i1, args.i2)