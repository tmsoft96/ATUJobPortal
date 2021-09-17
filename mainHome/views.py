import pyrebase
from ATUJobPortal.config.firebase import Firebase
from mainHome.controllers.indexController import indexController
from mainHome.controllers.contactController import contactUsController
from mainHome.controllers.aboutController import aboutController
from mainHome.controllers.jobDetialsController import jobDetailsController
from mainHome.controllers.jobListingController import jobListingController

firebaseConfig = {
        "apiKey": "AIzaSyD5-FOcfZTu_FeyMaZioPEz7MLpjSTYSfk",
        "authDomain": "atujobportal-33aba.firebaseapp.com",
        "databaseURL": "",
        "projectId": "atujobportal-33aba",
        "storageBucket": "atujobportal-33aba.appspot.com",
        "messagingSenderId": "501965329940",
        "appId": "1:501965329940:web:3f8bd58f8e0427a2c9b901",
        "measurementId": "G-J9BRLQTB9R",
        "serviceAccount": "static/firebase/atujobportal-33aba-firebase-adminsdk-wcge9-31d51b269e.json",
    }

firebase = pyrebase.initialize_app(firebaseConfig)


def index(request):
    return indexController(request)


def jobListing(request):
    return jobListingController(request)

def jobDetails(request):
    return jobDetailsController(request)

def aboutUs(request):
    return aboutController(request)

def contactUs(request):
    return contactUsController(request)
