from mainHome.controllers.contactController import contactUsController
from mainHome.controllers.aboutController import aboutController
from mainHome.controllers.jobDetialsController import jobDetailsController
from mainHome.controllers.jobListingController import jobListingController
from mainHome.controllers.studentRegisterFormController import studentRegisterFormController
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'heading': 'Home'})


def jobListing(request):
    return jobListingController(request)

def jobDetails(request):
    return jobDetailsController(request)

def aboutUs(request):
    return aboutController(request)

def contactUs(request):
    return contactUsController(request)

def studentRegisterForm(request):
    return studentRegisterFormController(request)