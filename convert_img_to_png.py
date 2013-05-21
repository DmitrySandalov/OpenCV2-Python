#!/usr/bin/python
import cv2
import sys

if len(sys.argv) != 2:  # Check for error in usage syntax
    print "Usage : python convert_img_to_png.py <image_file>"
else:
    image = cv2.imread(sys.argv[1])
    cv2.imwrite(sys.argv[1] + '.png', image)
