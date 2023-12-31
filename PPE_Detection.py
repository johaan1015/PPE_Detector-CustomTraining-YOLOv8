from ultralytics import YOLO
import cv2
import cvzone
import numpy as np

#cap=cv2.VideoCapture(0)#for webcam capture
#cap.set(3,1280)
#cap.set(4,720)
cap=cv2.VideoCapture("../Videos/ppe-3.mp4")#for Videos
model=YOLO("best.pt")
class_names=['Helmet', 'Person', 'Vest']

while True:
    success,img=cap.read()
    results=model(img,stream=True)
    for r in results:
        for box in r.boxes:
            #BOUNDING BOX
             #Using cv2
            #x1,y1,x2,y2=box.xyxy[0]
            #x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
              #Using cvzone
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)
            w = x2 - x1
            h = y2 - y1
            cvzone.cornerRect(img,(x1,y1,w,h))

            #CONFIDENCE SCORE AND CLASS NAME
            cls_id = box.cls[0].item()
            cls_name=class_names[int(cls_id)]
            conf=np.round(box.conf[0].item(),2)
            cvzone.putTextRect(img,f"{cls_name}{conf}",(max(0,x1),max(20,y1)),scale=0.7,thickness=1)

    cv2.imshow("WebLive",img)
    cv2.waitKey(1)