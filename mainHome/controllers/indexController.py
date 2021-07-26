from django.shortcuts import render


def indexController(request):
    return render(request, 'index.html', {'heading': 'Home'})