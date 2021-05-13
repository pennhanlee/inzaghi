import numpy as np
import cv2
import random

img = cv2.imread('./assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#goodFeaturesToTrack(Frame, Nth best corners, tolerance (0 -> 1 where 1 is the best), euclidean distance of between corners)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners) #turn the corners array elements into integers

for corner in corners: 
    x, y = corner.ravel() #flatten 3D array
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])  #can just use 0 because there is only 1 coordinate per array
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))  #making a tuple of 3 digits that correspond to a BGR color, typecast to 8 bit int
        cv2.line(img, corner1, corner2, color, 1)
        

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()