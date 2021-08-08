from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileAboutMeController(request):
    auth = Authentication(request)

    return render(request,
                  'customerCareerProfile_aboutMe.html',
                  {"heading": "About Me | ATU Job Portal",
                   "auth": auth.authMap})
