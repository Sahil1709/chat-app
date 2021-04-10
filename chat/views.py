from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/chat')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if(not fname or not lname or not username or not password):
            messages.info(request,'Fields cannot be blank')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,email=email ,username=username,password=password)
                user.save()
        return redirect('/')
    else:
        return render(request, 'register.html')

def room(request,room_name):
    return render(request , "chatroom.html" , {
        'room_name':room_name
    })

def index(request):
    return render(request , 'index.html')