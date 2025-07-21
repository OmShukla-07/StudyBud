from django.shortcuts import render

rooms = [
    {'id' : 1, 'name': 'I am Ironman'},
    {'id' : 2, 'name': 'I am Spiderman'},
    {'id' : 3, 'name': 'I am Batman'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    return render(request, 'base/room.html')
