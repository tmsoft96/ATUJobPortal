from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def loginController(request):
    # checking if user sign in already
    auth = Authentication(request)
    if auth.authMap.get("authorize"):
        if auth.authMap.get("userType") == "customer":
            return HttpResponseRedirect("/customer/dashboard")
        elif auth.authMap.get("userType") == "employer":
            return HttpResponseRedirect("/employer/dashboard")

    if request.method == "POST":
        if request.POST.get("button") == "logIn":
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(email)
            if email == "customer@gmail.com":
                request.session["userType"] = "customer"
                request.session["authorize"] = True
                return HttpResponseRedirect("/customer/dashboard")
            elif email == "employer@gmail.com":
                request.session["userType"] = "employer"
                request.session["authorize"] = True
                return HttpResponseRedirect("/employer/dashboard")
            else:
                return render(request, 'login.html',
                              {"heading": "login",
                               "wrongCredential": True,
                               'auth': auth.authMap})

    return render(request, 'login.html',
                  {"heading": "login",
                   'auth': auth.authMap})
