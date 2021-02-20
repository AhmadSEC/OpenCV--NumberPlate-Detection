import numpy as np
import cv2

frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)


cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count =0




while(True):
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberplates = nPlateCascade.detectMultiScale(imgGray, 1.1,10)
    for (x,y,w,h) in numberplates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgRoi)

            cv2.imshow("Result", img)

    # Display the resulting frame
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()