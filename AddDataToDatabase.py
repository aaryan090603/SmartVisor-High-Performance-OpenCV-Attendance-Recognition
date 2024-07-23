import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://facerecognitionsystem-eb51e-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "amrit":
        {
            "name": "Amritanshu",
            "major": "AIML",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    'aaryan':
        {
            "name": "Aaryan Barde",
            "major": "AIML",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-10-14 00:54:34"
        },


    # 'burcu':
    #     {
    #         "name": "Burcu Ozberg",
    #         "major": "Physics",
    #         "starting_year": 2021,
    #         "total_attendance": 7,
    #         "standing": "G",
    #         "year": 2,
    #         "last_attendance_time": "2023-10-11 00:54:34"
    #     }
}
for key, value in data.items():
    ref.child(key).set(value)
