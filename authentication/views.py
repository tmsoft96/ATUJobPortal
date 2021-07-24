from authentication.authControllers.studentRegisterFormController import studentRegisterFormController
from authentication.authControllers.loginController import loginController
from authentication.authControllers.registerController import registerController


def login(request):
    return loginController(request)


def register(request):
    return registerController(request)


def studentRegisterForm(request):
    return studentRegisterFormController(request)
