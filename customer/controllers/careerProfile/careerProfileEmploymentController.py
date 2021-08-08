from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileEmploymentController(request):
    auth = Authentication(request)
    dictionary = Dictionary()

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    return render(request,
                  'customerCareerProfile_employment.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap,
                   "qualifications": dictionary.qualificationsList, 
                   "currentJobs": dictionary.currentJobsFunctionList,
                   "yearExperiences": yearExperienceList,
                   "workTypes": dictionary.workTypeList,})
