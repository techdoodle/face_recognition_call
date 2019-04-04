# import the libraries
import os
import face_recognition
import sys


def face_rec(current_image):
    
# make a list of all the available images


# load your image
    image_to_be_matched = face_recognition.load_image_file('lavika1.jpg')


# encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(
       image_to_be_matched)[0]


# iterate over each image

    # load the image
   #  = face_recognition.load_image_file(image)
    # encode the loaded image into a feature vector
    print("in face rec")
    try:
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
    
        # match your image with the image and check if it matches
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded,tolerance=0.50)
        print(result)
        # check if it was a match
        if result[0] == True:
            print ("Matched: " )
            
            quit()            
        else:
            print ("Not matched: ")
            
            return
    except:
        pass
