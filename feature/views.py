from django.shortcuts import render
# Create your views here.

def feature(request):
    return render(request, 'feature/feature.html')