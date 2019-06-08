from django.shortcuts import render,redirect
from .models  import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.
def contact(request):
    if request.method=='POST':
        name = request.POST["Name"]
        email = request.POST["Email"]
        mobile = request.POST["Mobile"]
        message = request.POST["Message"]
        contact = Contact(name=name,email=email,number=mobile,message=message)
        contact.save()
        return redirect('community')