#!/usr/bin/python
import cv2
import sys

if len(sys.argv) != 2:  # Check for error in usage syntax
    print "Usage : python open_img.py <image_file>"
else:
    img = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)  # Read image file
    if img is None:  # Check for invalid input
        print "Could not open or find the image"
    else:
        cv2.namedWindow('Display Window')  # create window for display
        cv2.imshow('Display Window', img)  # Show image in the window
        print "size of image: ", img.shape  # print size of image
        print "\nPress any key to close..."
        cv2.waitKey(0)  # Wait for keystroke
        cv2.destroyAllWindows()  # Destroy all windows
