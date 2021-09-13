from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

def employerPostJobController(request):
    auth = Authentication(request)
    dictionary = Dictionary()
    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    return render(request,
                  'employerPostJob.html',
                  {"heading": "Post A Job | ATU Job Portal",
                  "industries": dictionary.industriesList,
                  "jobFunctions": dictionary.currentJobsFunctionList,
                  "workTypes": dictionary.workTypeList,
                  "regions": dictionary.regionList,
                  "yearExperiences": yearExperienceList,
                  "qualifications": dictionary.qualificationsList,
                  "jobLevels": dictionary.jobLevelList,
                  "currencies": dictionary.currencyList,
                  "salaries": dictionary.salaryList,
                   'auth': auth.authMap})