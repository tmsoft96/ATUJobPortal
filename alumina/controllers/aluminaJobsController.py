from alumina.config.userModel import AluminaUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect


def aluminaJobsController(request):
    auth = Authentication(request)

    msg = None
    errorMessage = None
    userDetails = None
    jobList = []
    status = None
    noJob = True
    sort = None
    

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]

        userDetails = AluminaUserModel.userModel(userId)
        print(userDetails)
        jobList = userDetails.get("jobList")
            
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        sort = request.GET.get("sort")

         # checking for no job
        if sort is None:
            sort = "unapprove"
            status = False
       
        if sort == "approve":
            status = True
            for job in jobList:
                if job.get("status"):
                    noJob = False
                    break
        elif sort == "unapprove":
            status = False
            for job in jobList:
                if not job.get("status"):
                    noJob = False
                    break


    return render(request,
                  'aluminaJobs.html',
                  {"heading": "Alumina View Jobs | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "jobs": jobList if len(jobList) > 0 else None,
                   "status": status,
                   "noJob": noJob,
                   "sort": sort,
                   "tabName": "jobs"})
