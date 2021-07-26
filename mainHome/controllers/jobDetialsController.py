from ATUJobPortal.config.auth import Auth
from django.shortcuts import render


def jobDetailsController(request):
    auth = Auth(request)
    return render(request, 'jobDetails.html',
                  {'heading': "Job Details",
                   "auth": auth.authMap})
