from customer.controllers.careerProfileController import careerProfileController
from customer.controllers.dashboardController import dashboardController
from customer.controllers.signUpController import signUpController

def signUp(request):
    return signUpController(request)

def dashboard(request):
    return dashboardController(request)

def careerProfile(request):
    return careerProfileController(request)