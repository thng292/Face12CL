import cv2
import numpy as np
import os
import mediapipe as mp
import datetime
cnt = 0
faceDect = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.4)
for i in range(1,19) :
    img = cv2.imread("E:/Thong/FaceDect/Face12CL/Original/ALL/" + str(i) + ".jpg")
    if img :
        procframe = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = faceDect.process(procframe)
        h,w,d = img.shape
        if results.detections :
            for id,face in enumerate(results.detections) :
                box = face.location_data.relative_bounding_box
                xl = int(box.xmin*w)
                yl = int(box.ymin*h)
                iw = int(box.width*w)
                ih = int(box.height*h)
                cropimg = img[max(yl,0):min(yl+ih,h),max(0,xl):min(xl+iw,w)]
                cv2.imwrite("u"+str(cnt)+".jpg",cv2.resize(cropimg,(200,200)))
                cnt+=1