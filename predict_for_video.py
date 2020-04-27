import numpy as np
import cv2
import faceRecognition as fr
import define_constants as def_const

# Load model
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(def_const.ROOT_PATH + r'face_recognizer.yml') # Path for trainingData.yml

# Capture video
cap=cv2.VideoCapture(0)
# 0 indicates 1st webcam in system
# 0 can be replaced by saved video path

while True:
    ret,test_img=cap.read()
    faces_detected,gray_img=fr.face_detection(test_img)
    print("Face Detected at:\n",faces_detected)
    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+h,x:x+h] # roi - region of interest
        label,confidence=face_recognizer.predict(roi_gray)
        print ("Confidence :",confidence)
        print(f"Label-{label}, {def_const.labels[label]}")
        predicted_name=def_const.labels[label]

        # Eyes detection
        eyes_detected = fr.eyes_detection(roi_gray)
        for eyes in eyes_detected:
            fr.draw_elipse(test_img, eyes, face)
            # fr.draw_circle(test_img, eyes, face)

        disp_text = f"{predicted_name},{str(int(confidence))}"
        fr.draw_rect(test_img,face)
        fr.put_text(test_img,disp_text,x,y)

        # Open your eyes
        if eyes_detected == ():
            cv2.putText(test_img, "Open your eyes", (x,y+h+30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,0), 2, cv2.LINE_AA)

    resized_img = cv2.resize(test_img,(1000,700))

    cv2.imshow("Face Detection with confidence, Press q ro exit", resized_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
