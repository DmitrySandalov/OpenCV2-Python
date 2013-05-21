#!/usr/bin/python
import cv2
import sys

if len(sys.argv) != 2:  # Check for error in usage syntax
    print "Usage : python open_video.py <video_file>"
else:
    videoCapture = cv2.VideoCapture(sys.argv[1])
    cv2.namedWindow('Display Window')
    while cv2.waitKey(1) == -1:
        f, img = videoCapture.read()
        cv2.imshow("Display Window", img)
    cv2.destroyAllWindows()  # Destroy all windows
