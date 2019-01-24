import cv2
import os
import tkinter



def Add_User(face_id, face_name):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    # Frontal faces pattern
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    print("\n Inicializando a captura da face. Olhe para a camera e aguarde ...")

    count = 0
    while True:

        # Capture frame-by-frame
        ret, frame = cam.read()
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        #Draw a rectangle around the faces
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w, y+h), (0, 255, 0), 2)
            count +=1

            #Save the image in Dataset
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        #Display the resulting frame
            cv2.imshow('Video',frame)

        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break
        elif count >= 50:
            break

    print("\n Exiting camera")

    cam.release()
    cv2.destroyAllWindows()



#Al. Bonifacio de Oliveira - UEA

'''
Useful Links:

https://realpython.com/face-detection-in-python-using-a-webcam/
https://realpython.com/face-recognition-with-python/
https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
https://www.superdatascience.com/opencv-face-recognition/

'''

