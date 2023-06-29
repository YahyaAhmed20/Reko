from django.shortcuts import render
# Create your views here.

def base(request):
    return render (request,'base.html')

def index(request):
    return render(request,'pages/index.html')


def contact(request):
    return render(request,'pages/contact.html')

def offer(request):
    return render(request, 'pages/offer.html')