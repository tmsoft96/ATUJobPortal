from customer.config.userModel import CustomerUserModel
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def dashboardController(request):
    auth = Authentication(request)
    userDetails = None
    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = CustomerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap,
                   "userDetails": userDetails})
