import cv2
import random
import numpy as np
from face_recognition_multipics import face_rec

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)

sampleNum=0;
id=random.randint(1,101)
print("in dataset")
while(True):
    print("in dataset while")
    try:
        ret,img=cam.read();
        print("in datasetimg read")
    
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces :
            print("in dataset read in for loop")
           
            sampleNum = sampleNum+1;
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            print(str(id)+"."+str(sampleNum))
         
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
       
       # cv2.imshow('face',img)
        face_rec(img)     
        print("in dataset called face rec")
    except:
        pass
         
cam.release();
cv2.destroyAllWindows()
