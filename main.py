import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  #3 is the hardcoded enumerator for width, 640px
cap.set(4, 480)  #4 is the hardcoded enumerator for height, 480px
threshold = 0.575


classNames = []
classFile = "./data/coco.names"

with open(classFile, "r") as f:
    classNames = f.read().rsplit("\n")

f.close()

configPath = "./data/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightPath = "./data/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    ret, frame = cap.read()
    classIds, confidences, bbox = net.detect(frame, confThreshold=threshold)

    if (len(classIds) > 0):
        for classId, confidence, box in zip(classIds.flatten(), confidences.flatten(), bbox):
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness = 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = classNames[(classId - 1)] + " " + str(round(confidence * 100, 3)) + "%"
            cv2.putText(frame, text, (box[0] + 10, box[1] + 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
