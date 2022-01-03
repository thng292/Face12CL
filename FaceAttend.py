import cv2
import numpy as np
import mediapipe as mp
import time
import tensorflow as tf
from keras.models import load_model


cl = [
'Nguyễn Hoàng Minh Anh',
'Trần Chương Anh',
'Phạm Dương Gia Bảo',
'Phan Phát Duy Bình',
'Trương Trí Dũng',
'Hà Minh Dũng',
'Nguyễn Minh Duy',
'Lê Thị Mỹ Duyên',
'Trương Tiến Đạt',
'Tô Thị Ngọc Hiền',
'Hà Minh Hiếu',
'Đặng Ngọc Hoàng',
'Nguyễn Huỳnh Tấn Khải',
'Vương Khang',
'Nguyễn Đăng Khoa',
'Bùi Đức Mạnh',
'Nguyễn Hà Hùng Minh',
'Huỳnh Giáng My',
'Phạm Hoàng Gia Nghi',
'Nguyễn Duy Ngọc',
'Phan Hồng Ngọc',
'Nguyễn Cao Đức Nguyên',
'Hà Quyền Nhân',
'Nguyễn Huỳnh Thảo Như',
'Nguyễn Thạch Thiên Phúc',
'Nguyễn Minh Quang',
'Đặng Ngọc Quyên',
'Hồ Trần Nhật Quyền',
'Đặng Minh Thiện',
'Nguyễn Quang Thông',
'Nguyễn Minh Tiến',
'Nguyễn Thanh Tuấn',
'Nguyễn Minh Triết'
]

model = load_model('./model/keras_model.h5',compile=False)
cv2.namedWindow("test",cv2.WINDOW_NORMAL)
cam  = "http://192.168.1.4:8080/?action=stream"
vid = "C:/Users/thong/Downloads/Video/video-1633574519.mp4"
cap = cv2.VideoCapture(cam)
mp_draw = mp.solutions.drawing_utils
faceDect = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.4)
ctime =0
ptime = time.time()
while cap.isOpened() :
    suc,img = cap.read()
    if suc :
        procframe = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #procframe = cv2.resize(procframe,(1280,720))
        results = faceDect.process(procframe)
        h,w,d = procframe.shape
        if results.detections :
            for face in results.detections:
                data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
                box = face.location_data.relative_bounding_box
                bbox = int(box.xmin*w)-20, int(box.ymin*h)-20,\
                    int(box.width*w)+40, int(box.height*h)+40
                #cv2.circle(img,(bbox[0],bbox[1]),5,(255,0,255),5)
                #cv2.putText(img,(str(bbox[0])+', '+str(bbox[1])),(bbox[0],bbox[1]),cv2.FONT_HERSHEY_PLAIN,2,(254,254,254))
                #mp_draw.draw_detection(img, face)
                cv2.rectangle(img,bbox,(255,0,255),2)
                xl = int(box.xmin*w)
                yl = int(box.ymin*h)
                iw = int(box.width*w)
                ih = int(box.height*h)
                cropimg = img[max(yl,0):min(yl+ih,h),max(0,xl):min(xl+iw,w)]
                image_array = np.asarray(cv2.resize(cropimg,(224,224)))
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)
                # mid = 0
                # mcon = 0
                # for id,con in enumerate(prediction[0]) :
                #     if (con>mcon) :
                #         mid = id
                #         mcon = con
                score = tf.nn.softmax(prediction[0])
                cv2.putText(img,(str(np.argmax(score))+": "+str(100 * np.max(score))),(bbox[0],bbox[1]),cv2.FONT_HERSHEY_PLAIN,2,(254,254,254))
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

"""

import numpy as np

# Load the model


# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.

# Replace this with the path to your image
image = Image.open('<IMAGE_PATH>')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array

# Normalize the image

# Load the image into the array


# run the inference

"""