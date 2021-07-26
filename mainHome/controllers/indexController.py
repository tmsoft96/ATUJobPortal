from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def indexController(request):
    auth = Authentication(request)
    return render(request, 'index.html',
                  {'heading': 'Home',
                   "auth": auth.authMap})
