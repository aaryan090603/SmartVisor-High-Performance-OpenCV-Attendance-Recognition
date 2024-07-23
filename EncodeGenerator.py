import os.path
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facerecognitionsystem-eb51e-default-rtdb.firebaseio.com/',
    'storageBucket': "facerecognitionsystem-eb51e.appspot.com"
})

# importing student images

folderPath = 'images'
pathList = os.listdir(folderPath)
print(pathList)

imgList = []
studentIDs = []

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    student_id = os.path.splitext(path)[0]
    imgList.append(img)
    studentIDs.append(student_id)
    # imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # studentIDs.append(os.path.splitext(path)[0])
    #
    # fileName = f'{folderPath}/{path}'
    # bucket = storage.bucket()
    # blob = bucket.blob(fileName)
    # blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIDs)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img)

        if face_encodings:  # Check if face_encodings is not empty
            encode = face_encodings[0]
            encodeList.append(encode)
        else:
            print(f"No face detected in one of the images: {img}")
    return encodeList
    # for img in imagesList:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     encode = face_recognition.face_encodings(img)[0]
    #     encodeList.append(encode)
    #
    # return encodeList

print ("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIDs]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

