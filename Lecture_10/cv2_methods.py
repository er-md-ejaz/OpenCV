import cv2
import numpy as np


img = cv2.imread('messi5.jpg')
img2 = cv2.imread('lena.jpg')
# cv2.imshow('image', img)
# print(img.shape)
# print(img.size)
# print(img.dtype)
# print(img.astype)

b, g, r = cv2.split(img)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)

img = cv2.merge((b, g, r))
# cv2.imshow('merged', img)

# ball = img[280:340, 330:390]
# print(ball.shape)
# img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .8, img2, .2, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()