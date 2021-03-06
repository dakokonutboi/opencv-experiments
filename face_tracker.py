import numpy as np
import cv2
import time

cv = cv2



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

font = cv2.FONT_HERSHEY_SIMPLEX


capture  = cv.VideoCapture(0)

while True:
    ret, frame = capture.read ()
    frame = cv.cvtColor (frame,  cv.COLOR_BGR2BGRA) 
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    mouths = mouth_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,'Face',(x,y), font, 1,(255,255,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        for (mx,my,mw,mh) in mouths:
            cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
    cv2.imshow('img',img)
    if cv.waitKey(10) & 0xFF == ord ('q'):
        break

capture.release()

cv2.destroyAllWindows()

