import cv2
import numpy as np
import os
import mediapipe as mp
import datetime

faceDect = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.7)
cv2.namedWindow("test",cv2.WINDOW_AUTOSIZE)
img = cv2.imread("E:/Thong/FaceDect/Face12CL/Original/16/269115182_249968220576190_2392040812908850549_n.jpg")
#cv2.imshow("test",img)
#crop here
procframe = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
results = faceDect.process(procframe)
h,w,d = img.shape
print(h,w)
if results.detections :
    for face in results.detections:
        box = face.location_data.relative_bounding_box
        bbox = int(box.xmin*w), int(box.ymin*h),\
                int(box.width*w), int(box.height*h)
        cv2.circle(img,(bbox[0],bbox[1]),5,(255,0,255),5)
        cv2.rectangle(img,bbox,(255,0,255),2)
cv2.imshow("test",img)
cv2.waitKey(0)

cv2.destroyAllWindows()