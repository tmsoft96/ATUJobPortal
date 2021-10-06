from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

from ATUJobPortal.config.constant import Constants
from customer.config.userModel import CustomerUserModel
from employers.config.userModel import EmployerUserModel


def contactUsController(request):
    auth = Authentication(request)
    constants = Constants()

    userDetails = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    return render(request, 'contact.html',
                  {'heading': 'Contact',
                   "auth": auth.authMap,
                   "userDetails": userDetails})
