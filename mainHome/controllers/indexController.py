from django.shortcuts import render
from ATUJobPortal.config.auth import Auth


def indexController(request):
    auth = Auth(request)
    return render(request, 'index.html',
                  {'heading': 'Home',
                   "auth": auth.authMap})
