from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'heading': 'Home'})


def jobListing(request):
    return render(request, 'jobListing.html', {'heading': "Job Listing"})

def jobDetails(request):
    return render(request, 'jobDetails.html', {'heading': "Job Details"})