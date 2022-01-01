import cv2
import numpy as np
import mediapipe as mp
import time

cv2.namedWindow("test",cv2.WINDOW_AUTOSIZE)
cam  = "http://192.168.1.4:8080/?action=stream"
vid = "C:/Users/thong/Downloads/Video/video-1633574519.mp4"
cap = cv2.VideoCapture(cam)
mp_draw = mp.solutions.drawing_utils
faceDect = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7)
ctime =0
ptime = time.time()
while cap.isOpened() :
    suc,img = cap.read()
    if suc :
        procframe = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = faceDect.process(procframe)
        h,w,d = img.shape
        if results.detections :
            for face in results.detections:
                box = face.location_data.relative_bounding_box
                bbox = int(box.xmin*w)-20, int(box.ymin*h)-20,\
                    int(box.width*w)+40, int(box.height*h)+40
                cv2.circle(img,(bbox[0],bbox[1]),5,(255,0,255),5)
                cv2.putText(img,(str(bbox[0])+', '+str(bbox[1])),(bbox[0],bbox[1]),cv2.FONT_HERSHEY_PLAIN,2,(254,254,254))
                cv2.rectangle(img,bbox,(255,0,255),2)
                #mp_draw.draw_detection(img, face)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        #img = cv2.flip(img,1)
        cv2.putText(img,str(int(fps)),(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)
    cv2.imshow("test",img)
    cv2.waitKey(1)

#cv2.imshow("test",img)
cap.release()
cv2.destroyAllWindows()