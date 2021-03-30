import cv2
img = cv2.imread('tamim.jpg')
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img3.jpg')


#Draw a Line
img = cv2.line(img, (8,40), (157,112),(0,0,255), 6)
#Draw Arrowline
arrow = cv2.arrowedLine(img, (0,0), (157,112), (0,255,0), 5)

#Draw a Rectangle
img1 = cv2.rectangle(img1, (10,14),(211,190),(0,255,0),3)

#Fill a Rectangle
img1 = cv2.rectangle(img1, (10,14),(211,190),(255,133,0),-1)

#Draw a Circle
img2 = cv2.circle(img2, (133,150), 35,(255,123,147),4)
img2 = cv2.circle(img2, (133,150), 34,(24,46,125),-1)

cv2.imshow("Image", img2)

cv2.waitKey(0)