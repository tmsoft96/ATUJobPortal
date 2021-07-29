from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication

def careerProfileEmploymentController(request):
    auth = Authentication(request)
    return render(request,
                  'customerCareerProfile_employment.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap})