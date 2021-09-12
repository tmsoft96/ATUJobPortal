from employers.controllers.employerDashboardController import employerDashboardController
from employers.controllers.signUpController import signUpController


def signUp(request):
    return signUpController(request)

def dashboard(request):
    return employerDashboardController(request)