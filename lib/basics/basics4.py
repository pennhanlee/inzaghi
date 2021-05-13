import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #CV2 0,0 coordinate is at top left. Increase X go Right, Increase Y go Down
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)  # line(frame, xy coor, xy coor, BGR colour code, thickness)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5) #Making another line to make an X across the screen
    img = cv2.rectangle(img, (100, 100), (200,200), (128,128,128), 5) # rectangle(frame, Top Left Coor, Bottom Right Coor, Color, Thickness)
    img = cv2.circle(img, (350,350), 60, (0, 0, 255), -1) # circle(frame, Center coor, radius, Colour, Fill or not)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # putText(frame, "What you wanna say", BottomLEFT!!! coor, font, scale, color, thickness, cv2.LINE_AA (make it nicer according to doc.))
    img = cv2.putText(img, 'INZAGHI', (200, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)  
    

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()