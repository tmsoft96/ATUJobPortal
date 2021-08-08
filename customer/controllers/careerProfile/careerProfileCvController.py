from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileCvController(request):
    auth = Authentication(request)

    return render(request,
                  'customerCareerProfile_cv.html',
                  {"heading": "Create a new Job Seeker CV | ATU Job Portal",
                   "auth": auth.authMap})
