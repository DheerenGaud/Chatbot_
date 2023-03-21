from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Contact

# Create your views here.
#  return HttpResponse("Hello Mathew")
def say_hello(request):
     
     if(request.method=="POST"):
         Fname=request.POST.get("Fname")
         Lname=request.POST.get("Lname")
         email=request.POST.get("email")
         contact=Contact(Fname=Fname,email=email,Lname=Lname)
         contact.save()
         
     return render(request,'contact.html')