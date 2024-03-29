from alumina.config.userModel import AluminaUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect


def aluminaDashboardController(request):
    auth = Authentication(request)

    msg = None
    errorMessage = None
    userDetails = None
    jobList = []
    

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]

        userDetails = AluminaUserModel.userModel(userId)
        print(userDetails)
        jobList = userDetails.get("jobList")
            
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "deleteSuccess":
            msg = "Job deleted successfully"
        elif request.GET.get("action") == "approveSuccess":
            msg = "Job approved successfully"
        elif request.GET.get("action") == "disapproveSuccess":
            msg = "Job disapproved successfully"

    return render(request,
                  'aluminaDashboard.html',
                  {"heading": "Alumina Dashboard | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "jobs": jobList if len(jobList) > 0 else None, 
                   "tabName": "dashboard"})
