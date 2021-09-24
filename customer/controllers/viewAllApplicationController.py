from customer.config.userModel import CustomerUserModel
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def ViewAllApplicationController(request):
    auth = Authentication(request)

    msg = None

    userDetails = None
    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = CustomerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    return render(request,
                  'viewAllAppication.html',
                  {"heading": "Job All Application | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails})
