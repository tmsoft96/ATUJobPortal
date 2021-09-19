from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render


def signUpController(request):
    dictionary = Dictionary()
    auth = Authentication(request)
    firebase = Firebase()
    constants = Constants()

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
                  'employerSignUp.html',
                  {"heading": "Create an Employer Account | ATU Job Portal",
                   "positions": dictionary.positionList,
                   "industries": dictionary.industriesList,
                   "employeesNumbers": dictionary.employeesNumberList,
                   "employerTypes": dictionary.employerTypeList,
                   'auth': auth.authMap,
                   "errorMessage": "Email Already exit"})

            print(user)
            userId = user["localId"]
            idToken = user["idToken"]
            request.session["userId"] = str(userId)
            request.session["idToken"] = str(idToken)
            request.session["email"] = str(user["email"])

            # add user detials to table user
            profile = {
                "id": userId,
                "userType": constants.userType[1],
                "lname": request.POST.get("lname"),
                "fname": request.POST.get("fname"),
                "email": user["email"],
                "position": request.POST.get("position"),
                "phone" : request.POST.get("phone"),
                "companyName": request.POST.get("companyName"),
                "industry": request.POST.get("industry"),
                "employeesNumber": request.POST.get("employeesNumber"),
                "employerType": request.POST.get("employerType"),
                "website": request.POST.get("website"),
                "address": request.POST.get("address"),
                "noOfJobs": 0,
                "noOfApplication": 0,
                "noOfViews": 0,
            }

            firebase.db.child("Users").child(userId).set(profile)

            # send email verification
            firebase.authe.send_email_verification(idToken)
            request.session["verifyEmail"] = False
            request.session["fromSignUp"] = True

            return HttpResponseRedirect("/account/login")

    return render(request,
                  'employerSignUp.html',
                  {"heading": "Create an Employer Account | ATU Job Portal",
                   "positions": dictionary.positionList,
                   "industries": dictionary.industriesList,
                   "employeesNumbers": dictionary.employeesNumberList,
                   "employerTypes": dictionary.employerTypeList,
                   'auth': auth.authMap})
