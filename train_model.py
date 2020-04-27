import faceRecognition as fr
import define_constants as def_const

print("Training Images ...")
faces,faceID=fr.labels_for_training_data(def_const.ROOT_PATH + r'train_images') #Path to the train-images folder
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save(def_const.ROOT_PATH + r'face_recognizer.yml') # Path to save model as trainingData.yml
print('Model saved...')
