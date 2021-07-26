from ATUJobPortal.config.auth import Auth
from django.shortcuts import render


def jobListingController(request):
    auth = Auth(request)
    return render(request, 'jobListing.html',
                  {'heading': "Job Listing",
                   "auth": auth.authMap})
