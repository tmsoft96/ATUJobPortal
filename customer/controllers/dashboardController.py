from ATUJobPortal.config.firebase import Firebase
from customer.config.userModel import CustomerUserModel
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def dashboardController(request):
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

    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage})
