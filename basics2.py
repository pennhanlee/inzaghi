import cv2
import random

'''
This code will show how to manipulate images

Images are presented as a 3D numpy array

[
    [[0,0,0], [255,255,255], [255,255,0], [255,0,0]]
    [[1,2,3], [255,0,0], [123,123,123], [80,12,12]]
]

print(img.shape) # To see the number of row and columns

img.shape will give you (1329, 1851, 3) which corresponds to Height, Width and Channels
Height is the number of pixels that make up the Height
Width is the number of pixels that make up the Width
Channels is the Number of pixels that represent (3 corresponds to Blue Green & Red)

'''

img = cv2.imread("./assets/face.png", -1)

# This is to change the pixels colour of an area
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]  #Basically randomly changing the colour of each pixel (B, G, R)

#This is to copy some area and putting it at another area.
tag = img[500:700, 600:900]
img[100:300, 700:1000] = tag #Note the dimensions must be the same


cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()