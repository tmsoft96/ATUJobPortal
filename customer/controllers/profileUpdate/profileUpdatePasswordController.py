from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

from ATUJobPortal.config.firebase import Firebase
from customer.config.userModel import CustomerUserModel


def profileUpdatePasswordController(request):
    auth = Authentication(request)
    firebase = Firebase()

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
        passwordOld = request.POST.get("oldPassword")
        passwordNew =  request.POST.get("newPassword")

       
        return HttpResponseRedirect("/customer/profile?action=updateSuccess")


    return render(request,
                  'customerProfileUpdate_password.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "auth": auth.authMap})