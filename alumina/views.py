from alumina.controllers.aluminaApplicationController import aluminaApplicationController
from alumina.controllers.aluminaCustomerController import aluminaCustomerController
from alumina.controllers.aluminaDashboardController import aluminaDashboardController
from alumina.controllers.aluminaEmployerController import aluminaEmployerController
from alumina.controllers.aluminaJobsController import aluminaJobsController


def dashboard(request):
    return aluminaDashboardController(request)

def application(request):
    return aluminaApplicationController(request)

def jobs(request):
    return aluminaJobsController(request)

def customers(request):
    return aluminaCustomerController(request)

def employers(request):
    return aluminaEmployerController(request)