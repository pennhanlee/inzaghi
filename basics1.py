import cv2

img = cv2.imread('./assets/face.png', 1) # opencv loads images in BGR (Blue Green Red)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  #Resize by a scale
# img = cv2.resize(img, (400, 400))  #Resize to 400px x 400px
# img = cv2.rotate(img, cv2.cv2.ROTATE_180)  #Rotate by 180. 

cv2.imwrite('new_img.png', img) # To save an image

'''
cv2.imread({path to file}, {render mode (-1, 0, 1)})
 -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. This is the default flag
 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

'''

cv2.imshow("face", img)  #cv2.imshow({Name of window}, {Image object})
cv2.waitKey(0)           #cv2.waitKey({Wait for a duration of time, 0 is infinite})
cv2.destroyAllWindows()