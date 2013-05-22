#!/usr/bin/python
import cv2

videoCapture = cv2.VideoCapture(0)
cv2.namedWindow('Display Window')
while cv2.waitKey(1) == -1:
    f, img = videoCapture.read()
    cv2.imshow("Display Window", img)
cv2.destroyAllWindows()  # Destroy all windows
