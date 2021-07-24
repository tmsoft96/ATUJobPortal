from django.shortcuts import render


def studentRegisterFormController(request):
    return render(request, 'studentRegisterForm.html', {"heading": "Create a Job Seeker Account | ATU Job Portal"})
