from django.shortcuts import render

def contactUsController(request):
    return render(request, 'contact.html', {'heading': 'Contact'})