import cv2
import time

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id = input('enter your id')
sampleNum = 0
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # incrementing sample number
        sampleNum = sampleNum + 1
        # saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('face', img)
    # wait for 100 miliseconds
    k = cv2.waitKey(100) # Press 'ESC' for exiting video
    if k == 27:
        break
    #if cv2.waitKey(100) & 0xFF == ord('q'):
       # break
    # break if the sample number is morethan
    elif sampleNum > 29:
        break
cam.release()
cv2.destroyAllWindows()