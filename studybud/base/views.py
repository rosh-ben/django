from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

"""rooms = [
    {'id':1, 'name': 'Lets Learn Python 1'},
    {'id':2, 'name': 'Lets Learn Python 2'},
    {'id':3, 'name': 'Lets Learn Python 3'}
]"""

rooms = Room.objects.all()
def home(request):  
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    the_room = Room.objects.get(id=pk)
    context = {'room': the_room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    context={'form': form}
    return render(request, 'base/room_form.html', context)