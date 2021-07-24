from authentication.authControllers.loginController import loginController
from authentication.authControllers.registerController import registerController


def login(request):
    return loginController(request)


def register(request):
    return registerController(request)

