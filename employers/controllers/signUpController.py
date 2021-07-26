from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render


def signUpController(request):
    dictionary = Dictionary()
    auth = Authentication(request)
    return render(request,
                  'employerSignUp.html',
                  {"heading": "Create an Employer Account | ATU Job Portal",
                   "positions": dictionary.positionList,
                   "industries": dictionary.industriesList,
                   "employeesNumbers": dictionary.employeesNumberList,
                   "employerTypes": dictionary.employerTypeList,
                   'auth': auth.authMap})
