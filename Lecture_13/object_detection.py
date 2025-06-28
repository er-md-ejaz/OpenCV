import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("tracking")
cv.createTrackbar("LH", "tracking", 0, 255, nothing)
cv.createTrackbar("LS", "tracking", 0, 255, nothing)
cv.createTrackbar("LV", "tracking", 0, 255, nothing)
cv.createTrackbar("UH", "tracking", 255, 255, nothing)
cv.createTrackbar("US", "tracking", 255, 255, nothing)
cv.createTrackbar("UV", "tracking", 255, 255, nothing)

while True:
    # frame = cv.imread('smarties.png')
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # l_b = np.array([110,50,50])
    # u_b = np.array([130,255,255])
    # mask = cv.inRange(hsv, l_b, u_b)

    l_h = cv.getTrackbarPos("LH", "tracking")
    l_s = cv.getTrackbarPos("LS", "tracking")
    l_v = cv.getTrackbarPos("LV", "tracking")
    u_h = cv.getTrackbarPos("UH", "tracking")
    u_s = cv.getTrackbarPos("US", "tracking")
    u_v = cv.getTrackbarPos("UV", "tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv.inRange(hsv, l_b, u_b)


    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('tracking', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)



    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break


cap.release()
cv.destroyAllWindows()