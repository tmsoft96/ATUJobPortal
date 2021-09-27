from employers.config.applicationModel import ApplicationModel
from employers.config.jobModel import JobModel
from ATUJobPortal.config.firebase import Firebase
from django.http.response import HttpResponseRedirect
from employers.config.userModel import EmployerUserModel
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

def employerDashboardController(request):
    auth = Authentication(request)
    firebase = Firebase()
    jobs = JobModel.allJob()
   
    msg = None
    errorMessage = None

    userDetails = None
    applications = None
    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(userId)
        applications = ApplicationModel.allCompanyApplication(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "resend":
            try:
                firebase.authe.send_email_verification(auth.authMap["idToken"])
                msg = "Verification send successfully to " + userDetails.get("email")
            except:
                errorMessage = "Error occured while trying to send verification code"

        elif request.GET.get("action") == "jobSuccess":
            msg = "Job posted successfully"

        elif request.GET.get("action") == "jobEditSuccess":
            msg = "Job updated successfully"

        elif request.GET.get("action") == "deleteSuccess":
            msg = "Job deleted successfully"

        elif request.GET.get("action") == "applicationSuccess":
            msg = "Application completed successfully"


    return render(request,
                  'employerDashboard.html',
                  {"heading": "Welcome | ATU Job Portal",
                   'auth': auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "jobs": jobs,
                   "applications": applications,
                   "noApplication": len(applications) == 0})