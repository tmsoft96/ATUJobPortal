from ATUJobPortal.config.auth import Auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def loginController(request):
    # checking if user sign in already
    auth = Auth(request)
    print(auth.authMap)
    if auth.authMap.get("authorize"):
        if auth.authMap.get("userType") == "customer":
            return HttpResponseRedirect("/customer/dashboard")

    if request.method == "POST":
        if request.POST.get("button") == "logIn":
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(email)
            request.session["authorize"] = True
            request.session["userType"] = "customer"
            return HttpResponseRedirect("/customer/dashboard")
    return render(request, 'login.html', {"heading": "login"})
