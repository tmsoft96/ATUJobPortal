from alumina.config.userModel import AluminaUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect


def aluminaApplicationController(request):
    auth = Authentication(request)

    msg = None
    errorMessage = None
    userDetails = None
    sort = None
    noApplication = True
    

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]

        userDetails = AluminaUserModel.userModel(userId)
        print(userDetails)
            
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        sort = request.GET.get("sort")
        if sort is None:
            sort = "pending"

    # checking for no application
    for application in userDetails.get("allApplicationsList"):
        if application.get("status") == sort:
            noApplication = False
            break

    return render(request,
                  'aluminaApplications.html',
                  {"heading": "Alumina All Application | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage, 
                   "sort": sort,
                   "noApplication": noApplication})
