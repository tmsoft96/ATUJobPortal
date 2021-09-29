from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.firebase import Firebase
from employers.config.userModel import EmployerUserModel
from employers.config.applicationModel import ApplicationModel
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from employers.config.jobModel import JobModel
from datetime import datetime
from django.core.mail import send_mail


def customerJobAppliedDetialController(request):
    auth = Authentication(request)
    firebase = Firebase()
    constants = Constants()

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
            applicationDict = ApplicationModel.paticularApplication(
                auth.authMap["userId"], key)

            allowAppointment = True
            # checking if applicant has been accepted or declined
            if request.GET.get("sort") == constants.jobstatus[2] or request.GET.get("sort") == constants.jobstatus[3]:
                allowAppointment = False
                errorMessage = "Applicant has been attended to already"

            return render(request, 'customerJobAppliedDetails.html',
                          {'heading': "Job Applied Details",
                           "auth": auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": key,
                           "errorMessage": errorMessage,
                           "applicationDict": applicationDict,
                           "fromExtra": True,
                           "allowAppointment": allowAppointment})

    if request.method == "POST":
        if request.POST.get("button") == "complete":
            customerId = request.POST.get("customerId")
            jobId = request.POST.get("jobId")
            status = request.POST.get("status")
            application = {
                "status": status,
                "note": request.POST.get("note"),
                "jobId": jobId,
                "date": request.POST.get("date"),
                "time": request.POST.get("time"),
                "venue": request.POST.get("venue"),
                "customerId": customerId,
                "createdDate": str(datetime.now()),
                "editDate": str(datetime.now()),
                "delete": False,
            }
            firebase.db.child("Appointments").child(
                auth.authMap["userId"]).child(customerId).set(application)

            # updating status field in all tables it occurs
            firebase.db.child("Application").child(
                auth.authMap["userId"]).child(jobId).update({"status": status})
            firebase.db.child("Users").child(customerId).child(
                "appliedJob").child(jobId).update({"status": status})

            # sending appointment email
            # Hi Michael, Gitplus as approved your application. Details below
            # date ...
            customerFName = request.POST.get("customerFname")
            costomerEmail = request.POST.get("costomerEmail")
            companyName = request.POST.get("companyName")

            emailBody = None
            if status == constants.jobstatus[2]:
                emailBody = "Dear " + customerFName + ".\n\n" + companyName + " has " + \
                    constants.jobstatus[2] + " your application. Below are the appointment details:" + \
                    "\n\n\n" + request.POST.get("note") + "\n\nDate:  " + request.POST.get("date") + "\nTime:   " + \
                    request.POST.get("time") + "\nVenue:    " + \
                    request.POST.get("venue")
            else:
                emailBody = "Hi " + customerFName + ", " + companyName + " has " + \
                    constants.jobstatus[2] + " your application. Below are the appointment details:" + \
                    "\n" + request.POST.get("note")
            send_mail("Job Application", emailBody,
                      "noreply@atujobportal.com", [costomerEmail])

            return HttpResponseRedirect("/employer/dashboard?action=applicationSuccess")
