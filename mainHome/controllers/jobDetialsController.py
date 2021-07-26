from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def jobDetailsController(request):
    auth = Authentication(request)
    return render(request, 'jobDetails.html',
                  {'heading': "Job Details",
                   "auth": auth.authMap})
