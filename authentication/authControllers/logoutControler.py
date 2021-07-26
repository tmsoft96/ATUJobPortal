from django.shortcuts import render
from django.contrib import auth


def logoutController(request):
    auth.logout(request)
    request.session["authorize"] = False
    request.session["userType"] = None
    return render(request, 'login.html',
                  {"heading": "login"})
