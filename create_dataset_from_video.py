import cv2
import os
import define_constants as def_const

img_count = 0
labels = 0;

# Set label count
while True:
	train_images_path = def_const.ROOT_PATH + "train_images/" + str(labels)
	if(os.path.exists(train_images_path)):
		labels += 1
	else:
		os.mkdir(train_images_path)
		break

# Capture video
cap=cv2.VideoCapture(0)
# 0 indicates 1st webcam in system
# 0 can be replaced by saved video path

while True:
    ret, frame = cap.read() # Returns return-code and frame
    cv2.imshow("Read Images For Training, Press q to stop", frame) # Display the frame
    cv2.imwrite(train_images_path+"/"+"image%04i.jpg" %img_count, frame) # Save the frame
    print("Current Count : ",img_count, end='\r')
    img_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f"Stopped at count - {img_count-1}")
