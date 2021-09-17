import pyrebase
class Firebase:
    firebaseConfig = {
        "apiKey": "AIzaSyD5-FOcfZTu_FeyMaZioPEz7MLpjSTYSfk",
        "authDomain": "atujobportal-33aba.firebaseapp.com",
        "projectId": "atujobportal-33aba",
        "storageBucket": "atujobportal-33aba.appspot.com",
        "messagingSenderId": "501965329940",
        "appId": "1:501965329940:web:3f8bd58f8e0427a2c9b901",
        "measurementId": "G-J9BRLQTB9R",
        "serviceAccount": "static/firebase/atujobportal-33aba-firebase-adminsdk-wcge9-31d51b269e.json",
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    authe = firebase.auth()
    db = firebase.database()
