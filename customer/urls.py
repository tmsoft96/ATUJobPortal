from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signUp, name="customerSignUp"),
    path('dashboard', views.dashboard, name="customerDashboard"),
    path('profile', views.careerProfile, name="careerProfile"),
    path('profile/employment', views.careerProfileEmployment, name="profileEmployment"),
    path('profile/about-me', views.careerProfileAboutMe, name="profileAboutMe"),
    path('profile/work-experience', views.careerProfileWorkExperience, name="profileWorkExperience"),
    path('profile/education', views.careerProfileEducation, name="profileEducation"),
    path('profile/certificate', views.careerProfileCertificate, name="profileCertificate"),
    path('profile/language', views.careerProfileLanguage, name="profileLanguage"),
    path('profile/cover-letter', views.careerProfileCoverLetter, name="profileCoverLetter"),
    path('profile/cv', views.careerProfileCv, name="profileCv"),
]
