from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileWorkExperienceController(request):
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
                  'customerCareerProfile_workExperience.html',
                  {"heading": "Create a new Job Seeker Experience | ATU Job Portal",
                   "auth": auth.authMap,
                   "jobLevels": dictionary.jobLevelList,
                   "countries": dictionary.countryList,
                   "industries": dictionary.industriesList,
                   "currentJobs": dictionary.currentJobsFunctionList,
                   "workTypes": dictionary.workTypeList,
                   "date": dateMap, })
