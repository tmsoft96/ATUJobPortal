from alumina.config.userModel import AluminaUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect


def aluminaEmployerController(request):
    auth = Authentication(request)

    msg = None
    errorMessage = None
    userDetails = None
    

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]

        userDetails = AluminaUserModel.userModel(userId)
        print(userDetails)
            
    else:
        return HttpResponseRedirect("/account/logout")

    return render(request,
                  'aluminaEmployer.html',
                  {"heading": "Alumina All Employer | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "tabName": "employers"})
