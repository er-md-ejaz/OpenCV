import cv2
import numpy as np

# events = [i for i in dir(cv2) if "EVENT" in i]
# for event in events:
#     print(event)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []

def click_event(event, x, y, flags, parameters):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x) + ", " + str(y)
        # cv2.putText(img, strXY, (x,y), font, 1, (255, 0, 255), 2, cv2.LINE_AA)
        # cv2.imshow('image', img)

        # printing line using two circles 

        # cv2.circle(img, (x,y), 1, (0, 255, 255), 2)
        # points.append((x, y))
        # if len(points) >= 2:
        #     cv2.line(img, points[-1], points[-2], (0, 255, 0), 2)
        # cv2.imshow('image', img)

        # displaying color in other window
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        img2 = np.zeros((512,512,3), np.uint8)
        img2[:] = [blue, green, red]
        cv2.imshow('image2', img2)


    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[x, y, 0]
    #     green = img[x, y, 1]
    #     red = img[x, y, 2]
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strXY = str(blue) + ", " + str(green) + ", " + str(red)
    #     cv2.putText(img, strXY, (x,y), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    #     cv2.imshow('image', img)



        
    
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
    