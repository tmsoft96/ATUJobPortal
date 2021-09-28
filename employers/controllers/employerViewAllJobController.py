from employers.config.jobModel import JobModel
from django.http.response import HttpResponseRedirect
from employers.config.userModel import EmployerUserModel
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

def employerViewAllJobController(request):
    auth = Authentication(request)
    jobs = JobModel.allJob()
   
    msg = None
    errorMessage = None
    userDetails = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

 
    return render(request,
                  'employerViewAllJobs.html',
                  {"heading": "View All Jobs | ATU Job Portal",
                   'auth': auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "jobs": jobs})