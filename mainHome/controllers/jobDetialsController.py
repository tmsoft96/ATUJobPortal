from django.shortcuts import render

def jobDetailsController(request):
    return render(request, 'jobDetails.html', {'heading': "Job Details"})