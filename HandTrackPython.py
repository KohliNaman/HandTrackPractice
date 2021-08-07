import HandTrackModule as htm
from cv2 import cv2
import mediapipe as mp
import time
import serial

pTime = 0
cTime =0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector()
while True:
    
    success,img = cap.read()
    img = detector.findhands(img)

    lmList = detector.findPos(img)
    if len(lmList) != 0:
        print(lmList[4])
        # print(lmList[4] - lmList[8])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


