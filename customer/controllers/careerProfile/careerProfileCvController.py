from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.uploadFIle import uploadFile
from customer.config.userModel import CustomerUserModel
from django.http.response import HttpResponseRedirect


def careerProfileCvController(request):
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

    if request.method == "POST":
        if request.POST.get("button") == "save":
            cvURL = "None"
            try:
                file = request.FILES["cvFile"]
                cvURL = uploadFile(request, file,  "cv")
            except:
                pass

            profile = {
                "cv": cvURL,
            }
            # updating the profile 
            firebase.db.child("Users").child(userId).update(profile)
            return HttpResponseRedirect("/customer/profile?action=cvSuccess")

    return render(request,
                  'customerCareerProfile_cv.html',
                  {"heading": "Create a new Job Seeker CV | ATU Job Portal",
                   "auth": auth.authMap,
                   "userDetails": userDetails})
