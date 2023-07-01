import cv2
import time
import numpy as np
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

capture = cv2.VideoCapture(0)

tracker = htm.HandTracker(detectConf=0.9)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volBar = 600
percent = 0

while True:
    success, img = capture.read()

    scale_percent = 150 
    width = int(img.shape[1] * scale_percent / 100) 
    height = int(img.shape[0] * scale_percent / 100) 
    dim = (width, height) 
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
    
    img = tracker.trackHands(img)
    lmList = tracker.getPosition(img, draw=True, index=[4,8])
    
    if len(lmList) != 0:

        thumbX, thumbY = lmList[4][1], lmList[4][2]
        indexX, indexY = lmList[8][1], lmList[8][2]

        line = cv2.line(img, (thumbX, thumbY), (indexX, indexY), (255,0,0), 2)
        lengthOfLine = math.hypot(indexX-thumbX, indexY-thumbY)
        volLevel = np.interp(lengthOfLine, [0, 326.25], [-65.25, 0])
        volume.SetMasterVolumeLevel(volLevel, None)

        cx, cy = int((indexX+thumbX)/2), int((indexY+thumbY)/2)
        cv2.circle(img, (cx, cy), 5, (0,255,0), 5)

        volBar = np.interp(volLevel, [-65.25, 0], [600, 200])
        percent = np.interp(volLevel, [-65.25, 0], [0, 100])
    
    cv2.putText(img, str(int(percent)), (50, 180), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,255,0), 2)
    cv2.rectangle(img, (50, 200), (100, 600), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (100, 600), (255, 0, 0), cv2.FILLED)

    cv2.imshow("Hand Gesture Volume Control", img)
    cv2.waitKey(1)
