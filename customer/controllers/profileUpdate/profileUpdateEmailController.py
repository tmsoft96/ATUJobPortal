from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def profileUpdateEmailController(request):
    auth = Authentication(request)

    return render(request,
                  'customerProfileUpdate_email.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "auth": auth.authMap})