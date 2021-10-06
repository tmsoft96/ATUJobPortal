from ATUJobPortal.config.constant import Constants
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
    constants = Constants()

    msg = None
    errorMessage = None
    userDetails = None
    jobList = []
    applicationList = []

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        idToken = auth.authMap["idToken"]

        # checking if email has been verify
        try:
            accountDetailsDict = dict(firebase.authe.get_account_info(idToken))
            request.session["verifyEmail"] = accountDetailsDict.get("users")[
                0].get("emailVerified")
        except:
            return HttpResponseRedirect("/account/logout")

        userDetails = EmployerUserModel.userModel(userId)
        applications = ApplicationModel.allCompanyApplication(userId)
        print(userDetails)
        jobs = JobModel.allJob()

        for job in jobs:
            if not job.get("delete") and job.get("companyId") == userId:
                jobList.append(job)

        for application in applications:
            if application.get("status") == constants.jobstatus[0]:
                applicationList.append(application)

    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "resend":
            try:
                firebase.authe.send_email_verification(auth.authMap["idToken"])
                msg = "Verification send successfully to " + \
                    userDetails.get("email")
            except:
                errorMessage = "Error occured while trying to send verification code\nIf this continue please re-login"

        elif request.GET.get("action") == "jobSuccess":
            msg = "Job posted successfully"

        elif request.GET.get("action") == "jobEditSuccess":
            msg = "Job updated successfully"

        elif request.GET.get("action") == "deleteSuccess":
            msg = "Job deleted successfully"

        elif request.GET.get("action") == "applicationSuccess":
            msg = "Application completed successfully"

    if request.method == "POST":
        if request.POST.get("button") == "testimony":
            model = EmployerUserModel.userModel(userId)
            profilePicture = model.get("logo")
            name = model.get("companyName")
            testimony = {
                "testimony": request.POST.get("note"),
                "id": auth.authMap["userId"],
                "name": name,
                "profilePicture": profilePicture,
            }
            firebase.db.child("Testimony").child(userId).set(testimony)
            msg = "Testimony added successfully"

    return render(request,
                  'employerDashboard.html',
                  {"heading": "Welcome | ATU Job Portal",
                   'auth': auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "jobs": jobList if len(jobList) > 0 else None,
                   "applications": applicationList if len(applicationList) > 0 else None,
                   "showTestimonyButton": True})
