from django.http.response import HttpResponseRedirect
from customer.config.__pycache__.userModel import CustomerUserModel
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def dashboardController(request):
    auth = Authentication(request)

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetail = CustomerUserModel.userModel(userId)
        print(userDetail)
    else:
        return HttpResponseRedirect("/logout")

    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap})
