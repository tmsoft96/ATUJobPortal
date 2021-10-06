from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

from ATUJobPortal.config.firebase import Firebase


def forgetPasswordController(request):
    auth = Authentication(request)
    firebase = Firebase()

    if request.method == "POST":
        if request.POST.get("button") ==  "forgetPassword":
            email = request.POST.get("email")
            firebase.authe.send_password_reset_email(email)
            return HttpResponseRedirect("/account/login?action=actionSuccess")

    return render(request, 'forgetPassword.html',
                    {"heading": "Forget Password",
                    'auth': auth.authMap})