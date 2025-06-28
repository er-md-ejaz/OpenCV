import cv2
import datetime

cap = cv2.VideoCapture(0)


# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    # cv2.imshow('frames', frame)


    if ret == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = frame

        width = (cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        date_time = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Height: " + str(height) + " Width: " + str(width)
        gray = cv2.putText(gray, text, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        gray = cv2.putText(gray, date_time, (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()