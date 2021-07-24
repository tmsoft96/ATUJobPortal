from django.shortcuts import render

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


def studentRegisterFormController(request):
    dayList = []
    yearList = []

    for day in range(1, 32):
        dayList.append(day)

    for year in range(1900, 2015):
        yearList.append(year)

    yearList.reverse()
    dobMap = {
        "day": dayList,
        "month": months,
        "year": yearList,
    }

    return render(request,
                  'studentRegisterForm.html',
                  {"heading": "Create a Job Seeker Account | ATU Job Portal",
                   "dob": dobMap, })
