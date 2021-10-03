from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime


def loginController(request):
    constants = Constants()
    firebase = Firebase()

    # checking if user sign in already
    auth = Authentication(request)
    if auth.authMap.get("authorize"):
        if auth.authMap.get("userType") == constants.userType[0]:
            return HttpResponseRedirect("/customer/dashboard")
        elif auth.authMap.get("userType") == constants.userType[1]:
            return HttpResponseRedirect("/employer/dashboard")
        elif auth.authMap.get("userType") == constants.userType[2]:
            return HttpResponseRedirect("/alumina/dashboard")

    
    if request.method == "GET":
        if request.GET.get("action") == "emailVerify":
            return render(request, 'login.html',
                        {"heading": "login",
                        "emailVerify": True,
                        "email": request.session["email"],
                        'auth': auth.authMap})


    if request.method == "POST":
        if request.POST.get("button") == "logIn":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = None

            # loging user in with email and password
            try:
                user = firebase.authe.sign_in_with_email_and_password(
                    email, password)
                firebase.db.child("Users").child(user["localId"]).update(
                    {"lastLoginDate": str(datetime.now())})
            except:
                return render(request, 'login.html',
                              {"heading": "login",
                               'auth': auth.authMap,
                               "errorMessage": "Incorrect email and password"})

            userId = user["localId"]
            idToken = user["idToken"]
            request.session["userId"] = str(userId)
            request.session["idToken"] = str(idToken)

            # checking if email has been verify
            accountDetailsDict = dict(firebase.authe.get_account_info(idToken))
            request.session["verifyEmail"] = accountDetailsDict.get("users")[
                0].get("emailVerified")

            # checking user type
            userType = firebase.db.child("Users").child(
                userId).child("userType").get().val()
            print(userType)
            if userType == constants.userType[0]:
                request.session["userType"] = constants.userType[0]
                request.session["authorize"] = True
                return HttpResponseRedirect("/customer/dashboard")
            elif userType == constants.userType[1]:
                request.session["userType"] = constants.userType[1]
                request.session["authorize"] = True
                return HttpResponseRedirect("/employer/dashboard")
            elif userType == constants.userType[2]:
                request.session["userType"] = constants.userType[2]
                request.session["authorize"] = True
                return HttpResponseRedirect("/alumina/dashboard")
            else:
                return render(request, 'login.html',
                              {"heading": "login",
                               "errorMessage": "Error loading your information",
                               'auth': auth.authMap})
       
    return render(request, 'login.html',
                    {"heading": "login",
                    'auth': auth.authMap})
