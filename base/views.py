from django.shortcuts import render
from .models import Room

##rooms = [
##    {'id' : 1, 'name': 'I am Ironman'},
##    {'id' : 2, 'name': 'I am Spiderman'},
##    {'id' : 3, 'name': 'I am Batman'},
##]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id= pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
