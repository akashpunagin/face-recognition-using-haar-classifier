import matplotlib.pyplot as plt
import cv2
import faceRecognition as fr
import define_constants as def_const

# Read image
test_img = cv2.imread(def_const.ROOT_PATH + r'test_imgs/test_img2.jpg')  #Give path to the image which you want to test

faces_detected,gray_img=fr.face_detection(test_img)
print("Face Detected:\n",faces_detected)

# Visuaizing the face detection
# Draw rectangle around faces
for face in faces_detected:
    fr.draw_rect(test_img,face)

plt.imshow(cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB))
plt.yticks([])
plt.xticks([])
plt.title(f"Face detection for test_img\nNo of faces detected - {len(faces_detected)}", fontsize=8)
plt.show()
