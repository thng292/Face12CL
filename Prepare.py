import cv2
import numpy as np
import os
import mediapipe as mp
import datetime
cnt = 0
faceDect = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)

for i in range(1,34) :
    for id,filename in enumerate(os.listdir("./Dat"+"/"+str(i))):
        img = cv2.imread(os.path.join("Dat"+"/"+str(i),filename))
        #img = cv2.imread("E:/vlcsnap-2021-12-13-18h27m14s586.png")
        #cv2.imshow("test",img)
        if img is not None:
            #crop here
            procframe = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            results = faceDect.process(procframe)
            h,w,d = img.shape
            #print(h,w)
            if results.detections :
                for face in results.detections:
                    box = face.location_data.relative_bounding_box
                    #center base
                    xl = int(box.xmin*w)-20
                    yl = int(box.ymin*h)-20
                    iw = int(box.width*w)+40
                    ih = int(box.height*h)+40
                    #cv2.rectangle(img,bbox,(255,0,255),2)
                    #print(min(xl,yl),max(xl,yl), min(xr,yr),max(xr,yr))
                    cropimg = img[max(yl,0):min(yl+ih,h),max(0,xl):min(xl+iw,w)]
                    #print(cropimg)
                    #cv2.imshow("test",cropimg)
                    cv2.imwrite(str(cnt)+'.png',cropimg)
                    cnt+=1
                    cv2.waitKey(0)

cv2.destroyAllWindows()