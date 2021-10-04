from alumina.config.userModel import AluminaUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication
from django.http.response import HttpResponseRedirect


def aluminaCustomerController(request):
    auth = Authentication(request)

    msg = None
    errorMessage = None
    userDetails = None
    

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]

        userDetails = AluminaUserModel.userModel(userId)
        print(userDetails)
            
    else:
        return HttpResponseRedirect("/account/logout")

    return render(request,
                  'aluminaCustomer.html',
                  {"heading": "Alumina All Customer | ATU Job Portal",
                   "auth": auth.authMap,
                   "msg": msg,
                   "userDetails": userDetails,
                   "errorMessage": errorMessage,
                   "tabName": "customers"})
