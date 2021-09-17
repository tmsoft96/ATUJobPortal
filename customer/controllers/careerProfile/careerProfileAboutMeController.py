from django.http.response import HttpResponseRedirect
from customer.config.userModel import CustomerUserModel
from ATUJobPortal.config.firebase import Firebase
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from datetime import datetime


def careerProfileAboutMeController(request):
    auth = Authentication(request)
    firebase = Firebase()

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
                "note": request.POST.get("note"),
                "editDate": str(datetime.now()),
            }

            # updating the profile
            firebase.db.child("Users").child(userId).update(profile)
            return HttpResponseRedirect("/customer/profile") 


    return render(request,
                  'customerCareerProfile_aboutMe.html',
                  {"heading": "About Me | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage})
