from authentication.controllers.logoutControler import logoutController
from authentication.controllers.loginController import loginController
from authentication.controllers.registerController import registerController


def login(request):
    return loginController(request)


def register(request):
    return registerController(request)

def logout(request):
    return logoutController(request)