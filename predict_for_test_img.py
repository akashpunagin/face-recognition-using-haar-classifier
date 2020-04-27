import numpy as np
import matplotlib.pyplot as plt
import cv2
import define_constants as def_const
import faceRecognition as fr

# Load model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(def_const.ROOT_PATH + r'face_recognizer.yml') # Path for trainingData.yml

# Load test image
test_img=cv2.imread(def_const.ROOT_PATH + r'test_imgs/<Image to test>.jpg')  # Path to the image to be tested

# Detect faces and predict
faces_detected,gray_img = fr.face_detection(test_img)
print("Face Detected:\n",faces_detected)

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print ("Confidence :",confidence)
    print(f"Label-{label}, {def_const.labels[label]}")
    predicted_name=def_const.labels[label]

    eyes_detected = fr.eyes_detection(roi_gray)
    for eyes in eyes_detected:
        fr.draw_elipse(test_img, eyes, face)
        # fr.draw_circle(test_img, eyes, face)

    fr.draw_rect(test_img,face)
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(1000,700))

cv2.imshow("Face Detection. Press any key to exit", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
