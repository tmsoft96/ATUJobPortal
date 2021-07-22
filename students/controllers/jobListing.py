from django.shortcuts import render

def jobListingController(request):
    return render(request, 'jobListing.html', {'heading': "Job Listing"})