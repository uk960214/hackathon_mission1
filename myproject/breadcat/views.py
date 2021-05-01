from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'breadcat/home.html')

def create(request):
    return render(request, 'breadcat/create.html')

def detail(request):
    return render(request, 'breadcat/detail.html')

def update(request):
    return render(request, 'breadcat/update.html')
