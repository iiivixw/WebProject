from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')
