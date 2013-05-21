#!/usr/bin/python
import cv2
import sys

if len(sys.argv) != 2:  # Check for error in usage syntax
    print "Usage : python convert_img_to_grayscale.py <image_file>"
else:
    image = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_GRAYSCALE)
    cv2.imwrite('gray_' + sys.argv[1], image)
