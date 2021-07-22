from students.controllers.jobDetials import jobDetailsController
from students.controllers.jobListing import jobListingController
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'heading': 'Home'})


def jobListing(request):
    return jobListingController(request)

def jobDetails(request):
    return jobDetailsController(request)