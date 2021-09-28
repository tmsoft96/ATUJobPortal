from employers.config.applicationModel import ApplicationModel
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from employers.config.userModel import EmployerUserModel
from django.shortcuts import render


def employerViewAllApplicationController(request):
    auth = Authentication(request)

    msg = None

    userDetails = None
    applications = None
    sort = None
    noApplication = True

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(userId)
        applications = ApplicationModel.allCompanyApplication(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        sort = request.GET.get("sort")
        if sort is None:
            sort = "pending"


    for application in applications:
        if application.get("status") == sort:
            noApplication = False
            break

    return render(request,
                  'employerViewAllAppication.html',
                  {"heading": "View All Application | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "applications": applications,
                   "sort": sort,
                   "noApplication": noApplication})
