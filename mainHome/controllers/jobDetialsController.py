from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.firebase import Firebase
from customer.config.userModel import CustomerUserModel
from ATUJobPortal.config.constant import Constants
from django.http.response import HttpResponseRedirect
from employers.config.jobModel import JobModel
from employers.config.userModel import EmployerUserModel
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail


def jobDetailsController(request):
    auth = Authentication(request)
    constants = Constants()
    firebase = Firebase()
    dictionary = Dictionary()

    userDetails = None
    errorMessage = None

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    else:
        errorMessage = "Login to apply"

    if request.method == "POST":
        if request.POST.get("button") == "apply":
            key = request.POST.get("key")
            companyId = request.POST.get("companyId")
            userId = auth.authMap["userId"]
            createdDate = str(datetime.now())
            apply = {
                "jobId": key,
                "customerId": userId,
                "companyId": companyId,
                "fname": request.POST.get("fname"),
                "lname": request.POST.get("lname"),
                "phone": request.POST.get("phone"),
                "qualification": request.POST.get("qualification"),
                "yearExperience": request.POST.get("yearExperience"),
                "note": request.POST.get("note"),
                "cv": "null",
                "status": constants.jobstatus[0],
                "timestamp": datetime.now().timestamp(),
                "createdDate": createdDate,
                "editDate": str(datetime.now()),
                "delete": False,
            }
            print(apply)
            firebase.db.child("Application").child(
                companyId).child(key).set(apply)

            # sending email to employer
            send_mail("Job Application", "Job Application from Michael",
                      "noreply@atujobportal.com", ["micaheltamakloe18.mt@gmail.com"])

            # add no of apply job to user profile
            noOfApplication = firebase.db.child("Users").child(
                companyId).child("noOfApplication").get().val()
            firebase.db.child("Users").child(companyId).update(
                {"noOfApplication": noOfApplication + 1})

            # updating user profile with job apply key
            info = {
                "companyId": companyId,
                "jobId": key,
                "status": constants.jobstatus[0],
                "createdDate": createdDate,
            }
            firebase.db.child("Users").child(userId).child(
                "appliedJob").child(key).set(info)

            return HttpResponseRedirect("/customer/dashboard?action=applySuccess")

    if request.method == "GET":
        if request.GET.get("action") == "job":
            key = request.GET.get("key")
            jobDict = JobModel.particularJob(key)
            print(jobDict)

            # checking for if job is already applied for customers only and
            # allow for declined applicants
            allowApplication = True
            if auth.authMap["userType"] == constants.userType[0]:
                for value in userDetails.get("appliedJobList"):
                    if value.get("jobId") == key and value.get("status") != constants.jobstatus[3]:
                        allowApplication = False
                        errorMessage = "You already applied for this job"
                        break

            if allowApplication:
                # Adding post view count if user type is customer
                if auth.authMap["userType"] == constants.userType[0]:
                    noOfViews = firebase.db.child("Users").child(
                        jobDict.get("companyId")).child("noOfViews").get().val()
                    firebase.db.child("Users").child(jobDict.get("companyId")).update(
                        {"noOfViews": noOfViews + 1})

            return render(request, 'jobDetails.html',
                          {'heading': "Job Details",
                           "auth": auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": key,
                           "qualifications": dictionary.qualificationsList,
                           "yearExperiences": yearExperienceList,
                           "allowApplication": allowApplication,
                           "errorMessage": errorMessage})

        elif request.GET.get("action") == "delete":
            key = request.GET.get("key")
            firebase.db.child("Jobs").child(key).update({"delete": True})

            # subtruct no of add job to user profile
            noOfJobs = userDetails.get("noOfJobs")
            firebase.db.child("Users").child(
                userId).update({"noOfJobs": noOfJobs - 1})

            return HttpResponseRedirect("/employer/dashboard?action=deleteSuccess")

    return HttpResponseRedirect("/")
