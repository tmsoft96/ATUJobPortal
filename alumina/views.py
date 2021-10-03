from alumina.controllers.aluminaApplicationController import aluminaApplicationController
from alumina.controllers.aluminaDashboardController import aluminaDashboardController


def dashboard(request):
    return aluminaDashboardController(request)

def application(request):
    return aluminaApplicationController(request)