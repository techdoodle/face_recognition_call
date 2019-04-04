# import the libraries
import os
import face_recognition
import datasetCreator



# make a list of all the available images
images = os.listdir('dataSet')

# load your image
image_to_be_matched = face_recognition.load_image_file('lavika.jpg')
#print(len(image_to_be_matched))

# encoded the loaded image into a feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

print(image_to_be_matched_encoded)
# iterate over each image
for image in images:
    # load the image
    current_image = face_recognition.load_image_file("dataSet/" + image)
    # encode the loaded image into a feature vector
    try:
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
    
        # match your image with the image and check if it matches
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded)
        print(result)
        # check if it was a match
        if result[0] == True:
            print ("Matched: " + image)
        else:
            print ("Not matched: " + image)
    except:
        pass
