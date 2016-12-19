import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    frame = cap.read()[1]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('original',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('hsv',hsv)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
