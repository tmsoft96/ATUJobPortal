from employers.controllers.employerViewAllJobController import employerViewAllJobController
from employers.controllers.employerViewAllApplicationController import employerViewAllApplicationController
from employers.controllers.customerJobAppliedDetialController import customerJobAppliedDetialController
from employers.controllers.employerPostJobController import employerPostJobController
from employers.controllers.employerDashboardController import employerDashboardController
from employers.controllers.signUpController import signUpController


def signUp(request):
    return signUpController(request)

def dashboard(request):
    return employerDashboardController(request)

def postJob(request):
    return employerPostJobController(request)

def jobAppliedDetails(request):
    return customerJobAppliedDetialController(request)

def viewAllApplication(request):
    return employerViewAllApplicationController(request)

def viewAllJob(request):
    return employerViewAllJobController(request)