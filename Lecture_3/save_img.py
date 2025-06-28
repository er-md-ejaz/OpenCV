import cv2

image_path = "lena.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Cannot read image at {image_path}")
    exit()


cv2.imshow('My Image', img)


key = cv2.waitKey(0) & 0xFF  

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('image_copy.png', img)  
    print("Image saved as image_copy.png")
    cv2.destroyAllWindows()
