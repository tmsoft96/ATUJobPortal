from ATUJobPortal.config.constant import Constants
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from datetime import datetime


def signUpController(request):
    dictionary = Dictionary()
    auth = Authentication(request)
    firebase = Firebase()
    constants = Constants()

    dayList = []
    yearList = []
    yearExperienceList = []

    for day in range(1, 32):
        dayList.append(day)

    for year in range(1900, 2015):
        yearList.append(year)

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    yearList.reverse()
    dobMap = {
        "day": dayList,
        "month": dictionary.monthsList,
        "year": yearList,
    }

    if request.method == "POST":
        if request.POST.get("button") == "signUp":
            email = request.POST.get("email")
            password = request.POST.get("password")

            # creating user account with email and password
            user = None
            try:
                user = firebase.authe.create_user_with_email_and_password(
                    email, password)
            except:
                return render(request,
                              'customerSignUp.html',
                              {"heading": "Create a Job Seeker Account | ATU Job Portal",
                               "dob": dobMap,
                               "nationalities": dictionary.nationalitiesList,
                               "qualifications": dictionary.qualificationsList,
                               "currentJobs": dictionary.currentJobsFunctionList,
                               "yearExperiences": yearExperienceList,
                               'auth': auth.authMap,
                               "errorMessage": "Email Already exit"})

            print(user)
            userId = user["localId"]
            idToken = user["idToken"]
            request.session["userId"] = str(userId)
            request.session["idToken"] = str(idToken)
            request.session["email"] = str(user["email"])

            dob = request.POST.get(
                "day") + "/" + request.POST.get("month") + "/" + request.POST.get("year")

            # add user detials to table user
            profile = {
                "id": userId,
                "userType": constants.userType[0],
                "lname": request.POST.get("lname"),
                "fname": request.POST.get("fname"),
                "gender": request.POST.get("gender"),
                "email": user["email"],
                "dob": dob,
                "nationality": request.POST.get("nationality"),
                "location": request.POST.get("location"),
                "phone": request.POST.get("phone"),
                "qualification": request.POST.get("qualification"),
                "currentJobFunction": request.POST.get("currentJobFunction"),
                "yearExperience": request.POST.get("yearExperience"),
                "cv": request.POST.get("email"),
                "tipsAlert": True if request.POST.get("tipsAlert") == "on" else False,
                "jobAlerts": True if request.POST.get("jobAlerts") == "on" else False,
                "lastLoginDate": str(datetime.now()),
                "createdDate": str(datetime.now()),
                "editDate": str(datetime.now()),
                "delete": False,
                "profilePicture": "None",
            }
            firebase.db.child("Users").child(userId).set(profile)

            # send email verification
            firebase.authe.send_email_verification(idToken)
            request.session["verifyEmail"] = False
            request.session["fromSignUp"] = True

            return HttpResponseRedirect("/account/login")

    return render(request,
                  'customerSignUp.html',
                  {"heading": "Create a Job Seeker Account | ATU Job Portal",
                   "dob": dobMap,
                   "nationalities": dictionary.nationalitiesList,
                   "qualifications": dictionary.qualificationsList,
                   "currentJobs": dictionary.currentJobsFunctionList,
                   "yearExperiences": yearExperienceList,
                   'auth': auth.authMap})
