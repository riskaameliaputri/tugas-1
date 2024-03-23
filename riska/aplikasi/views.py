from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def riska(request):
    return render(request, 'riska.html')