Define constants for the project.
open define_constants.py file.
	define the ROOT_PATH to your working directory



create a folder named train_images if not present in the working directory

this folder will contain folders named 0, 1, 2, 3 ... which will represent the labels


Creating dataset: you can create dataset from webcam, or saved video.

run create_dataset_from_video.py.
	look at the image count in the terminal (or command prompt), take atleast 300 images per label(person)
	press q to stop
	if you run it again (for another person), 'labels' variable will be updated and the images will be stored in that directory


open define_constants.py file.
	in labels dictionary, define the names of labels(person) with key as the label, and value as the name


run detect_faces_for_test_img.py.
	it will only 'detect' the face(s), in the 'test_img'
	you can also store other images in test_imgs directory and detect faces off of that image


Training the model
run train_model.py file.
	it will train the model. The model will be saved as face_recognizer.yml file in the working directory



Predicting for single image.
run predict_for_test_img.py to predict for 'test_img'
	it will predict the person, and recognize face and eyes.
	Press any key to exit. Dont close the window as it will freze the terminal, (or command prompt).

Predicting for Video: Yoy can predict for saved video or off of the webcam
run predict_for_video.py
	it will predict the person, also detect face, and eyes
	it will also show a message if eyes are closed (or not detected)
	press q to exit
