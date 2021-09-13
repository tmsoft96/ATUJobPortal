from employers.controllers.employerPostJobController import employerPostJobController
from employers.controllers.employerDashboardController import employerDashboardController
from employers.controllers.signUpController import signUpController


def signUp(request):
    return signUpController(request)

def dashboard(request):
    return employerDashboardController(request)

def postJob(request):
    return employerPostJobController(request)