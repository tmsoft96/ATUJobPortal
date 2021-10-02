from ATUJobPortal.config.dictionary import Dictionary
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def aluminaDashboardController(request):
    auth = Authentication(request)

    return render(request,
                  'aluminaDashboard.html',
                  {"heading": "Alumina Dashboard | ATU Job Portal",
                   "auth": auth.authMap})
