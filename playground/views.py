from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from playground.models import Contact
from django.contrib import messages

# Create your views here.

# def say_hello(request):
#     #pull data from db
#     # transform
#     # send email
#     # return HttpResponse("hello world")
#     return render(request,'index.html',{"name":"shubham"})

def home(request):
    # return HttpResponse("this is home")
    return render(request,'home.html')

def aboutus(request):
    # return HttpResponse("this is about us")
    return render(request,'about.html')

def contactus(request):
    # return HttpResponse("this is contact")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request,'contact.html')

def service(request):
    # return HttpResponse("this is contact")
    return render(request,'services.html')

