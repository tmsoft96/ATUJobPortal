from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('job-listings/', views.jobListing, name='jobListings'),
    path('job-details', views.jobDetails, name="jobDetails"),
    path('about', views.aboutUs, name='about'),
]
