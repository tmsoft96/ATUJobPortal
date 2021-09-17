from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from customer.config.userModel import CustomerUserModel
from datetime import datetime



def careerProfileEmploymentController(request):
    auth = Authentication(request)
    dictionary = Dictionary()

    firebase = Firebase()

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    msg = None
    errorMessage = None

    userDetails = None
    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = CustomerUserModel.userModel(userId)
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

    if request.method == "POST":
        if request.POST.get("button") == "save":
            profile = {
                "profilePicture": request.POST.get("profilePicture"),
                "professionalHeadline": request.POST.get("professionalHeadline"),
                "qualification": request.POST.get("qualification"),
                "currentJobFunction": request.POST.get("currentJobFunction"),
                "preferredJobFunction": request.POST.get("preferredJobFunction"),
                "yearExperience": request.POST.get("yearExperience"),
                "workType": request.POST.get("workType"),
                "salaryExpectation": request.POST.get("salaryExpectation"),
                "tipsAlert": True if request.POST.get("tipsAlert") == "on" else False,
                "jobAlerts": True if request.POST.get("jobAlert") == "on" else False,
                "editDate": str(datetime.now()),
            }

            # updating the profile
            firebase.db.child("Users").child(userId).update(profile)
            return HttpResponseRedirect("/customer/profile") 

    return render(request,
                  'customerCareerProfile_employment.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap,
                   "qualifications": dictionary.qualificationsList, 
                   "currentJobs": dictionary.currentJobsFunctionList,
                   "yearExperiences": yearExperienceList,
                   "workTypes": dictionary.workTypeList,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage})
