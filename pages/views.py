from django.shortcuts import render
# Create your views here.

def base(request):
    return render (request,'base.html')



def contact(request):
    return render(request,'pages/contact.html')

def login(request):
    return render(request,'pages/login.html')
