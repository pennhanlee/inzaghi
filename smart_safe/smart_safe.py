import cv2
import face_recognition
from imutils.video import VideoStream
from imutils.video import FPS
from datetime import datetime
from gpiozero import AngularServo
import imutils
import pickle
import time


current_name = "Unrecognised"
match_threshold = 16
minimum_count = 5
encodings_file = "encodings.pickle"
encoding_data = pickle.loads(open(encodings_file, "rb").read())
pause = False
# cam = cv2.VideoCapture(0)  #0 means the default camera.
face_encoding = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# servo = AngularServo(pin=18, initial_angle=0, min_angle=0, max_angle=90, min_pulse_width=1/1000, max_pulse_width=2/1000)
# eyes_encoding = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cam = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()


while True:
    video = cam.read()
    video = imutils.resize(video, width=500)
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
    faces = face_encoding.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    faces_rect = []
    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 2) #This is the red box around face
        faces_rect.append((y, x + w, y + h, x))

        #Detect Eye Region
        # roi_gray = gray[y: y+h, x: x+w]
        # roi_color = rgb[y: y+h, x: x+w]

    encodings = face_recognition.face_encodings(rgb)
    success_count = 0
    for (y1, x2, y2, x1), encoding in zip(faces_rect, encodings):
        matches = face_recognition.compare_faces(encoding_data["encodings"], encoding)
        current_name = "unrecognised"
        
        if True in matches:
            matchedIdx = [i for (i, match) in enumerate(matches) if match]
            print(str(len(matchedIdx)) + "/" + str(match_threshold))
            if len(matchedIdx) >= match_threshold:
                current_name = "recognised"
                timestamp = datetime.now()
                timestamp = timestamp.strftime("%d_%m_%Y %H_%M_%S")
                # cv2.imwrite(f"accessed_image/{timestamp}.jpg", video)
                cv2.rectangle(video, (x1, y1), (x2, y2), (0, 255, 0), 2) #Change box to green
                cv2.putText(video, current_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 5, cv2.LINE_AA)
                success_count += 1
            else:
                success_count = 0
                # servo.angle = -90

            if success_count > minimum_count:
                #Add servo unlock code here
                # servo.angle = 90
                # time.sleep(5.0)
                # servo.angle = -90
                print("Recognised User, Box Unlocked")

        else:
            # servo.angle = -90
            continue

        
    cv2.imshow("camera", video)
    if cv2.waitKey(1) == ord("q"):
        break

cam.stop() # use release() for RPI
cv2.destroyAllWindows