import cv2
img1 = cv2.imread('lena.jpg', -1)
# img2 = cv2.imread('lena.jpg', 1)

cv2.imshow('image1', img1)
# cv2.imshow('image2', img2)
k = cv2.waitKey(0) & 0xFF
# print(k)
# cv2.destroyAllWindows()

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img1)
    cv2.destroyAllWindows()




