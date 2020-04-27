import numpy as np
import cv2
import os


def face_detection(test_img):
    gray_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY) # Convert to grayscale

    # Define haarcascade Classifier
    cascPath = "haarcascade_frontalface_default.xml"
    face_haar = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)

    # detectMultiScale - general function to detect objects
    # If it finds a face, it returns a list of positions of said face in the form “Rect(x,y,w,h).”, if not, then returns “None”.
    # Arguements:
    # image - should be grayscale
    # scaleFactor - This function compensates a false perception in size that occurs when one face appears to be bigger than the other simply because it is closer to the camera
    # minNeighbors - This is a detection algorithm that uses a moving window to detect objects, it does so by defining how many objects are found near the current one before it can declare the face found.
    #                Parameter specifying how many neighbors each candidate rectangle should have to retain it
    faces = face_haar.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

    return faces,gray_img

def eyes_detection(test_img):
    cascPath = "haarcascade_eye.xml"
    eyes_haar = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
    eyes = eyes_haar.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 5)
    return eyes

def labels_for_training_data(directory):
    faces = []
    faceID = []

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping system file")
                continue
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("img_path : ", img_path)
            print("id: ", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print ("Imgaes are not loaded properly...")
                continue

            faces_rect,gray_img = face_detection(test_img)
            if len(faces_rect) != 1:
                continue
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h] # roi - region of interest
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID

def train_classifier(faces,faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms (LBPH)
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

def draw_rect(test_img,face):
    (x,y,w,h) = face
    # cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.rectangle(test_img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

def draw_circle(test_img, eye, face):
    (x,y,w,h) = face
    (x2,y2,w2,h2) = eye
    eye_center = (x + x2 + w2//2, y + y2 + h2//2)
    radius = int(round((w2 + h2)*0.25))
    # cv2.circle(image, center_coordinates, radius, color, thickness)
    cv2.circle(test_img, eye_center, radius, (255, 0, 0 ), thickness=2)

def draw_elipse(test_img, eye, face):
    (x,y,w,h) = face
    (x2,y2,w2,h2) = eye
    eye_center = (x + x2 + w2//2, y + y2 + h2//2)
    radius = int(round((w2 + h2)*0.25))
    axesLength = (w2//2, h2//2 -10)
    # cv2.ellipse(image, center_coordinates, axesLength,angle, startAngle, endAngle, color, thickness)
    cv2.ellipse(test_img, eye_center, axesLength, 0, 0, 360, (0,255,0), thickness=2)

def put_text(test_img, text, x, y):
    # cv2.putText(image, text, org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(test_img, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 2.5, (255,0,0), 2, cv2.LINE_AA)
