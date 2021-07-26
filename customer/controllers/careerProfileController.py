from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def careerProfileController(request):
    auth = Authentication(request)
    return render(request,
                  'customerCareerProfile.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap})
