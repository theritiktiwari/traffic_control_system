
import cv2

cap= cv2.VideoCapture('traffic.mp4')
car_cascade = cv2.CascadeClassifier('vehicle.xml')

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)
    for (x,y,w,h) in cars:
            plate = frame[y:y + h, x:x + w]
            cv2.rectangle(frame,(x,y),(x + w, y + h) ,(255 , 0, 0),2)
            cv2.rectangle(frame, (x, y - 30), (x + w, y), (255, 0, 0), -2)
            cv2.putText(frame, 'Vehicle', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow('Vehicle',plate)
    frames = cv2.resize(frame,(1920,1080))
    cv2.imshow('Vehicle Detection System', frames)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
