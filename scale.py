import os
import cv2

for i in range(1,34) :
    for id,filename in enumerate(os.listdir("./Faces"+"/"+str(i))):
        img = cv2.imread(os.path.join("Faces"+"/"+str(i),filename))
        if img is not None:
            img = cv2.resize(img,(200,200))
            cv2.imwrite(str(i) + "_" +str(id)+".png",img)