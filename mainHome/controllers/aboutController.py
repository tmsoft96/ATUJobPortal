from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def aboutController(request):
    auth = Authentication(request)
    return render(request, 'about.html',
                  {'heading': "About",
                   "auth": auth.authMap})
