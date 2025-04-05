from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello Bhai log, Aur batao!?")
    return render(request,'website/index.html')

def about(request):
    #return HttpResponse("Janne aaye ho humare bare me!")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Mahip ji to nahi ho!")
    return render(request, 'website/contact.html')

def login(request):
    #return HttpResponse("Login page")
    return render(request, 'website/login.html')