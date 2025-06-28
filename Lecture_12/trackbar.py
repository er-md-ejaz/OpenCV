import cv2 as cv
import numpy as np

def tracker(x):
    print(x)

# img = np.zeros((300, 512, 3), np.uint8)
img = cv.imread('lena.jpg')
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 10, 400, tracker)
cv.createTrackbar('G', 'image', 0, 255, tracker)
cv.createTrackbar('R', 'image', 0, 255, tracker)
switch = 'gray:0 \n color:1'
cv.createTrackbar(switch, 'image', 0, 1, tracker)

while(1):
    cv.imshow('image', img)

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s==0:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('image', gray)
    else:
        cv.imshow('image', img)


    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break



cv.destroyAllWindows()