from cv2 import cv2
import time
# import numpy as np
import os
import HandTrackModule as htm
import math

wCam, hCam = 1280,720
pTime = 0
cTime =0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon = 0.75)

while True:
    success, img = cap.read()

    img = detector.findhands(img)
    lmList = detector.findPos(img,draw= False)
    if len(lmList) != 0:
        # print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 =lmList[8][1],lmList[8][2]
        cx,cty = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1) , 15, (255,255,0), cv2.FILLED)
        cv2.circle(img, (x2,y2) , 15, (255,255,0), cv2.FILLED)
        length = math.hypot(x2-x1,y2-y1)
        print(length)
        if length<30:
            # os.system('wget -q --spider 192.168.0.141:9117/LOFF')
            # os.system('wget -q --spider 192.168.0.141:9117/FOFF')
            os.system('explorer https://www.amazon.in')
            time.sleep(1)

            cv2.circle(img, (x1,y1) , 15, (0,255,0), cv2.FILLED)
            cv2.circle(img, (x2,y2) , 15, (0,255,0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)