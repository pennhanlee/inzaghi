import cv2
from imutils import paths
import face_recognition
import pickle
import os
from datetime import datetime

name = "recognised"

cam = cv2.VideoCapture(0)

cv2.namedWindow("Please press spacebar to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Please press spacebar to take a photo", 500, 300)

img_counter = 0
date = str(datetime.now)

while True:
    ret_val, video = cam.read()
    if not ret_val:
        print("An error occurred while taking your picture, please try again")
        break
    cv2.imshow("Please press spacebar to take a photo", video)

    if cv2.waitKey(1) == ord("q"):
        print("Q hit, closing program")
        break
    elif cv2.waitKey(1) == ord(" "):
        img_name = "faces/" + name + f"/image_{img_counter}_{date}.jpg"
        cv2.imwrite(img_name, video)
        print(f"Picture {img_counter} Taken")
        img_counter += 1

cam.release()
cv2.destroyAllWindows

imagePaths = list(paths.list_images("faces/recognised"))
knownEncodings = []
# face_encodings = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface.xml")

for (i, imagePath) in enumerate(imagePaths):
    print(f"[INFO] processing image {i + 1} / {len(imagePaths)}")
    name = "recognised"

    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Training with pure cv2 is a work in progress. use face_recognition with HoG first
    # gray = cv2.cvtColr(image, cv2.COLOR_BGR2GRAY)
    # face = face_encodings.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    face = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, face)
    knownEncodings.extend(encodings)

print("[INFO] serializing encoding into pickle file")
data = {"encodings": knownEncodings}
f = open('encodings.pickle', "wb")
f.write(pickle.dumps(data))
f.close()
