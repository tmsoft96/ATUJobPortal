from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def jobListingController(request):
    auth = Authentication(request)
    return render(request, 'jobListing.html',
                  {'heading': "Job Listing",
                   "auth": auth.authMap})
