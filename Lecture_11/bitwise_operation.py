import cv2
import numpy as np

img1 = np.zeros((300, 400, 3), np.uint8)
img1 = cv2.rectangle(img1, (150, 0), (250, 100), (255, 255, 255), -1)
cv2.imshow("img1", img1)


width = 400
height = 300
black_half = np.zeros((height, width // 2, 3), dtype=np.uint8)
white_half = np.ones((height, width // 2, 3), dtype=np.uint8) * 255
img2 = np.concatenate((black_half, white_half), axis=1)
cv2.imshow("img2", img2)

bitAnd = cv2.bitwise_and(img1, img2)
cv2.imshow('bitwise_and', bitAnd)

# print(img1.shape)
# print(img1.size)
# print(img2.shape)
# print(img2.size)

bit_or = cv2.bitwise_or(img1, img2)
cv2.imshow('bitwise or', bit_or)

bit_xor = cv2.bitwise_xor(img1, img2)
cv2.imshow('bitwise xor', bit_xor)


cv2.waitKey(0)
cv2.destroyAllWindows()