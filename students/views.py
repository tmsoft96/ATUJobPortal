from students.controllers.aboutController import aboutController
from students.controllers.jobDetialsController import jobDetailsController
from students.controllers.jobListingController import jobListingController
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'heading': 'Home'})


def jobListing(request):
    return jobListingController(request)

def jobDetails(request):
    return jobDetailsController(request)

def aboutUs(request):
    return aboutController(request)