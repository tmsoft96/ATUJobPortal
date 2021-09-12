from customer.controllers.profileUpdate.profileUpdatePersonalController import profileUpdatePersonalController
from customer.controllers.careerProfile.careerProfileCvController import careerProfileCvController
from customer.controllers.careerProfile.careerProfileCoverLetterController import careerProfileCoverLetterController
from customer.controllers.careerProfile.careerProfileLanguageController import careerProfileLanguageController
from customer.controllers.careerProfile.careerProfileCertificateController import careerProfileCertificateController
from customer.controllers.careerProfile.careerProfileEducationController import careerProfileEducationController
from customer.controllers.careerProfile.careerProfileWorkExperienceController import careerProfileWorkExperienceController
from customer.controllers.careerProfile.careerProfileEmploymentController import careerProfileEmploymentController
from customer.controllers.careerProfile.careerProfileAboutMeController import careerProfileAboutMeController
from customer.controllers.careerProfileController import careerProfileController
from customer.controllers.dashboardController import dashboardController
from customer.controllers.signUpController import signUpController

def signUp(request):
    return signUpController(request)

def dashboard(request):
    return dashboardController(request)

def careerProfile(request):
    return careerProfileController(request)

def careerProfileEmployment(request):
    return careerProfileEmploymentController(request)

def careerProfileAboutMe(request):
    return careerProfileAboutMeController(request)

def careerProfileWorkExperience(request):
    return careerProfileWorkExperienceController(request)

def careerProfileEducation(request):
    return careerProfileEducationController(request)

def careerProfileCertificate(request):
    return careerProfileCertificateController(request)

def careerProfileLanguage(request):
    return careerProfileLanguageController(request)

def careerProfileCoverLetter(request):
    return careerProfileCoverLetterController(request)

def careerProfileCv(request):
    return careerProfileCvController(request)

def profileUpdatePersonal(request):
    return profileUpdatePersonalController(request)