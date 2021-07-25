from django.shortcuts import render

def aboutController(request):
    return render(request, 'about.html', {'heading': "About"})