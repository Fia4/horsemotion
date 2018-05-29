import cv2
import numpy as np

#cap = cv2.VideoCapture('video1.mp4')
cap = cv2.VideoCapture(0)


while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    blue = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)

    blue = cv2.dilate(blue, kernel)
    res = cv2.bitwise_and(frame, frame, mask=blue)

    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    cv2.imshow("Color Tracking", frame)
    cv2.imshow("Color Tracking 2", blue)
    cv2.imshow("Color Tracking 3", res)
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()