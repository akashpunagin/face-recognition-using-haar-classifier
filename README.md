1. Define ROOT_PATH for the project.
* Open define_constants.py file.
  - Define the ROOT_PATH to your working directory

2. Create a folder named train_images if not present in the working directory
* This folder will contain folders named 0, 1, 2, 3 ... which will represent the labels

3. Creating dataset: **You can create dataset from webcam, or saved video**
* Run create_dataset_from_video.py.
  - Look at the image count in the terminal (or command prompt), take atleast 300 images per label(person)
  - Press q to stop
  - If you run it again (for another person), 'labels' variable will be updated and the images will be stored in that directory

4. Define labels variable
* Open define_constants.py file.
 - In labels dictionary, define the names of labels(person) with key as the label, and value as the name

5. Detect faces
* Run detect_faces_for_test_img.py.
  - It will only 'detect' the face(s), in the 'test_img'
  - You can also store other images in test_imgs directory and detect faces off of that image

6. Training the model
* Run train_model.py file.
	- It will train the model. The model will be saved as face_recognizer.yml file in the working directory

7. Predicting for single image.
* Run predict_for_test_img.py to predict for 'test_img'
	- It will predict the person, and recognize face and eyes.
	- Press any key to exit. **Dont close the window as it will freze the terminal, (or command prompt)**

8. Predicting for Video: You can predict for saved video or off of the webcam
* Run predict_for_video.py
	- It will predict the person, also detect face, and eyes
	- It will also show a message if eyes are closed (or not detected)
	- Press q to exit
