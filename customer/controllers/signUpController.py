from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render


def signUpController(request):
    dictionary = Dictionary()
    auth = Authentication(request)

    dayList = []
    yearList = []
    yearExperienceList = []

    for day in range(1, 32):
        dayList.append(day)

    for year in range(1900, 2015):
        yearList.append(year)

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    yearList.reverse()
    dobMap = {
        "day": dayList,
        "month": dictionary.monthsList,
        "year": yearList,
    }

    return render(request,
                  'customerSignUp.html',
                  {"heading": "Create a Job Seeker Account | ATU Job Portal",
                   "dob": dobMap,
                   "nationalities": dictionary.nationalitiesList,
                   "qualifications": dictionary.qualificationsList,
                   "currentJobs": dictionary.currentJobsFunctionList,
                   "yearExperiences": yearExperienceList,
                   'auth': auth.authMap})
