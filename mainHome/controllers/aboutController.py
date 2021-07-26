from ATUJobPortal.config.auth import Auth
from django.shortcuts import render


def aboutController(request):
    auth = Auth(request)
    return render(request, 'about.html',
                  {'heading': "About",
                   "auth": auth.authMap})
