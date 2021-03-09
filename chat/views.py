from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request , "index.html")

def room(request,room_name):
    print(request.user.username)
    return render(request , "chatroom.html" , {
        'room_name':room_name
    })