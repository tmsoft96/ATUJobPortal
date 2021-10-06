from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render
from ATUJobPortal.config.constant import Constants
from customer.config.testimonyModel import TestimonyModel
from customer.config.userModel import CustomerUserModel

from employers.config.userModel import EmployerUserModel


def aboutController(request):
    auth = Authentication(request)
    constants = Constants()
    testimonies = TestimonyModel.allTestimony()

    userDetails = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    return render(request, 'about.html',
                  {'heading': "About",
                   "auth": auth.authMap,
                   "userDetails": userDetails,
                   "testimonies": testimonies})
