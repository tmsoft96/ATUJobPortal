from django.urls import path
from . import views

urlpatterns = [
   path("dashboard", views.dashboard, name="aluminaDashboard"),
   path("application", views.application, name="aluminaApplication"),
]
