from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
import PyPDF2

def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        ConfirmPassword=request.POST['ConfirmPassword']

        if password!=ConfirmPassword:
            messages.info(request,"Passwords didn't match!")
            redirect('/')
        elif User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exists!")
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Exists!")
            return redirect('/')        
        else:    
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.info(request,"User Created.")
            return redirect('login')
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/fileupload')
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    return render(request,"login.html")   

def fileupload(request):
    if request.method == "POST":
        name = request.POST['name']
        file = request.FILES['file']
        
        #TEXT EXTRACTION FROM PDF FILE USING PYPDF2
        text = PyPDF2.PdfReader(file)
        page = text.pages[0].extract_text()

        data = File(name=name, file=file, text=page)
        data.save()
    return render(request,"fileupload.html")     
