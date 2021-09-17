from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.contrib import auth


def logoutController(request):
    auth.logout(request)
    request.session["authorize"] = False
    request.session["verifyEmail"] = False
    request.session["userType"] = None
    request.session["userId"] = None
    request.session["idToken"] = None
    request.session["email"] = None
    return HttpResponseRedirect("/account/login")
