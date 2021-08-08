from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileEducationController(request):
    auth = Authentication(request)
    dictionary = Dictionary()

    yearList = []

    for year in range(1900, 2021):
        yearList.append(year)
    yearList.reverse()

    dateMap = {
        "month": dictionary.monthsList,
        "year": yearList,
    }

    return render(request,
                  'customerCareerProfile_education.html',
                  {"heading": "Create a new Job Seeker Education | ATU Job Portal",
                   "auth": auth.authMap,
                   "qualifications": dictionary.qualificationsList,
                   "date": dateMap, })
