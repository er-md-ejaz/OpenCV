import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0), (256, 290), (150, 251, 31), 5)
img = cv2.arrowedLine(img, (0,15), (256, 290), (150, 251, 31), 5)
img = cv2.rectangle(img, (315, 0), (125, 546), (125, 153, 78), 5)
img = cv2.rectangle(img, (315, 0), (125, 546), (125, 153, 78), -1)
img = cv2.circle(img, (255, 255), 120, (255, 154, 34), -1)
font = cv2.FONT_HERSHEY_TRIPLEX
img = cv2.putText(img, 'lena', (10,500), font, 5, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
