from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.authentication import Authentication
from django.contrib import auth


def logoutController(request):
    auth.logout(request)
    request.session["authorize"] = False
    request.session["userType"] = None
    return HttpResponseRedirect("/account/login")
