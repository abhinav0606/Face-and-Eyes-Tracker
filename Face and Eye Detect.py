import cv2
faces=cv2.CascadeClassifier("face.xml")
eyes=cv2.CascadeClassifier("eye.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=faces.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=3)
        gray_face=gray[y:y+h,x:x+w]
        color_face=frame[y:y+h,x:x+w]
        eye=eyes.detectMultiScale(gray_face,1.3,5)
        for (a,b,c,d) in eye:
            cv2.rectangle(color_face,(a,b),(a+c,b+d),(100,100,100),thickness=3)
    cv2.imshow("Abhinav's Frame",frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()