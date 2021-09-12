from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

def employerDashboardController(request):
    auth = Authentication(request)
    return render(request,
                  'employerDashboard.html',
                  {"heading": "Welcome | ATU Job Portal",
                   'auth': auth.authMap})