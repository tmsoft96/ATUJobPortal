from django.shortcuts import render


def dashboardController(request):
    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal"})
