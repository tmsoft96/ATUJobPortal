import pyrebase
from ATUJobPortal.config.firebase import Firebase
from mainHome.controllers.indexController import indexController
from mainHome.controllers.contactController import contactUsController
from mainHome.controllers.aboutController import aboutController
from mainHome.controllers.jobDetialsController import jobDetailsController
from mainHome.controllers.jobListingController import jobListingController


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
