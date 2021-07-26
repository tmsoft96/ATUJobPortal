from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render


def dashboardController(request):
    dictionary = Dictionary()
    print(dictionary.currentJobsFunctionList)
    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal"})
