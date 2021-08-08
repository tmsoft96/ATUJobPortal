from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def careerProfileLanguageController(request):
    auth = Authentication(request)
    dictionary = Dictionary()

    return render(request,
                  'customerCareerProfile_language.html',
                  {"heading": "Create a new Job Seeker Language | ATU Job Portal",
                   "auth": auth.authMap,
                   "languages": dictionary.languageList,
                   "proficiencies": dictionary.proficiencyList, })
