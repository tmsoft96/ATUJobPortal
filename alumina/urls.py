from django.urls import path
from . import views

urlpatterns = [
   path("dashboard", views.dashboard, name="aluminaDashboard"),
   path("application", views.application, name="aluminaApplication"),
   path("job", views.jobs, name="aluminaJob"),
   path("customers", views.customers, name="aluminaCustomer"),
   path("employers", views.employers, name="aluminaEmployer"),
]
