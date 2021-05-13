import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  #This will return a frame (numpy array of the frame), ret = return status (True or False)
    width = int(cap.get(3))  #get(3) gets width. 
    height = int(cap.get(4)) #get(4) gets height. Need to read documentation. Returns a floating point value

    '''
    Establishing an image of Frame Size, then putting it as a numpy array of zeros for a black screen
    in preparation of being changed to other screens
    '''

    img = np.zeros(frame.shape, np.uint8)  #Empty numpy area, make the exact same shape as the frame to make it fit. np.uint8 refers to unsigned integer 8 bit
    
    ''' 
    Shrinking the window to quarter size, then fitting 4 of these into the window
    '''
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    img[height//2:, :width//2] = smaller_frame
    img[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    img[height//2:, width//2:] = smaller_frame


    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):  #waitKey(1) will wait for 1 millisec. If 'q' is pressed, it will break
        break

cap.release() #Release the camera
cv2.destroyAllWindows()