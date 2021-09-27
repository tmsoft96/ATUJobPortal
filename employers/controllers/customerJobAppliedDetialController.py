from employers.config.userModel import EmployerUserModel
from employers.config.applicationModel import ApplicationModel
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from employers.config.jobModel import JobModel


def customerJobAppliedDetialController(request):
    auth = Authentication(request)

    userDetails = None
    errorMessage = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "job":
            key = request.GET.get("key")
            jobDict = JobModel.particularJob(key)
            applicationDict = ApplicationModel.paticularApplication(auth.authMap["userId"], key)

            return render(request, 'customerJobAppliedDetails.html',
                          {'heading': "Job Applied Details",
                           "auth": auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": key,
                           "errorMessage": errorMessage,
                           "applicationDict": applicationDict,
                           "fromExtra": True})
