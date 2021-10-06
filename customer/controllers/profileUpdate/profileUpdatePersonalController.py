from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render
from ATUJobPortal.config.firebase import Firebase

from customer.config.userModel import CustomerUserModel


def profileUpdatePersonalController(request):
    dictionary = Dictionary()
    firebase = Firebase()
    auth = Authentication(request)
    
    dayList = []
    yearList = []
    yearExperienceList = []

    msg = None
    errorMessage = None

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

    userDetails = None
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

        userDetails = CustomerUserModel.userModel(userId)
        print(userDetails)
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

    if request.method == "POST":
        userId = auth.authMap["userId"]
        dob = request.POST.get(
                "day") + "/" + request.POST.get("month") + "/" + request.POST.get("year")
        profile = {
            "lname": request.POST.get("lname"),
            "fname": request.POST.get("fname"),
            "gender": request.POST.get("gender"),
            "dob": dob,
            "nationality": request.POST.get("nationality"),
        }
        firebase.db.child("Users").child(userId).update(profile)
        return HttpResponseRedirect("/customer/profile?action=updateSuccess")

    return render(request,
                  'customerProfileUpdate_personal.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "dob": dobMap,
                   "nationalities": dictionary.nationalitiesList,
                   "auth": auth.authMap,
                   "userDetails": userDetails,
                   "msg": msg,
                   "errorMessage": errorMessage,})