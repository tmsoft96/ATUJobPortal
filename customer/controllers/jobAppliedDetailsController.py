from employers.config.applicationModel import ApplicationModel
from django.http.response import HttpResponseRedirect
from customer.config.userModel import CustomerUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from employers.config.jobModel import JobModel


def jobAppliedDetailsController(request):
    auth = Authentication(request)

    userDetails = None
    errorMessage = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = CustomerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "job":
            jobId = request.GET.get("jobId")
            companyId = request.GET.get("companyId")
            jobDict = JobModel.particularJob(jobId)
            applicationDict = ApplicationModel.paticularApplication(companyId, jobId)

            hideButton = False
            try:
                hideButton = True if request.GET.get("fromAdmin") == "1"  else False
            except:
                pass

            return render(request, 'jobAppliedDetails.html',
                          {'heading': "Job Applied Details",
                           "auth": auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": jobId,
                           "errorMessage": errorMessage,
                           "applicationDict": applicationDict,
                           "fromExtra": True,
                           "hideButton": hideButton})
