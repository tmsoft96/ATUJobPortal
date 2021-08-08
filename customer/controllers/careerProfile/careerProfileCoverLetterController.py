from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileCoverLetterController(request):
    auth = Authentication(request)

    return render(request,
                  'customerCareerProfile_coverLetter.html',
                  {"heading": "Create a new Job Seeker Cover Letter | ATU Job Portal",
                   "auth": auth.authMap})
