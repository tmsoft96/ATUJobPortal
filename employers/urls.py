from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signUp, name="employerSignUp"),
    path('dashboard', views.dashboard, name="employerDashboard"),
    path('jobs', views.viewAllJob, name="employerViewAllJobs"),
    path('jobs/create', views.postJob, name="jobPost"),
    path('application', views.viewAllApplication, name="employerViewAllApplication"),
    path('application/details', views.jobAppliedDetails),
]
