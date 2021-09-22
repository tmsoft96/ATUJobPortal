from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.firebase import Firebase
from customer.config.userModel import CustomerUserModel
from ATUJobPortal.config.constant import Constants
from django.http.response import HttpResponseRedirect
from employers.config.jobModel import JobModel
from employers.config.userModel import EmployerUserModel
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def jobDetailsController(request):
    auth = Authentication(request)
    constants = Constants()
    firebase = Firebase()
    dictionary = Dictionary()

    userDetails = None

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    if request.method == "GET":
        if request.GET.get("action") == "job":
            key = request.GET.get("key")
            jobDict = JobModel.particularJob(key)
            print(jobDict)
            return render(request, 'jobDetails.html',
                          {'heading': "Job Details",
                           "auth": auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": key,
                           "qualifications": dictionary.qualificationsList,
                           "yearExperiences": yearExperienceList})

        elif request.GET.get("action") == "delete":
            key = request.GET.get("key")
            firebase.db.child("Jobs").child(key).update({"delete": True})

            # subtruct no of add job to user profile
            noOfJobs = userDetails.get("noOfJobs")
            firebase.db.child("Users").child(
                userId).update({"noOfJobs": noOfJobs - 1})

            return HttpResponseRedirect("/employer/dashboard?action=deleteSuccess")

    if request.method == "POST":
        if request.POST.get("action") == "apply":
            key = request.POST.get("key")
            apply = {
                "jobId": key,
                "customerId": auth.authMap["userId"],
                "fname": request.POST.get("fname"),
                "lname": request.POST.get("lname"),
                "phone": request.POST.get("phone"),
                "qualification": request.POST.get("qualification"),
                "yearExperience": request.POST.get("yearExperience"),
                "note": request.POST.get("saveNote"),
                "cv": "null",
            }
            firebase.db.child("Application").child(key).push(apply)

            # add no of apply job to user profile
            # noOfJobs = userDetails.get("noOfJobs")
            # firebase.db.child("Users").child(
            #     userId).update({"noOfJobs": noOfJobs - 1})

            return HttpResponseRedirect("/customer/dashboard?action=applySuccess")


    return HttpResponseRedirect("/")
