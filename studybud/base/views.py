from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
# Create your views here.

"""rooms = [
    {'id':1, 'name': 'Lets Learn Python 1'},
    {'id':2, 'name': 'Lets Learn Python 2'},
    {'id':3, 'name': 'Lets Learn Python 3'}
]"""


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(name__icontains=q) | 
        Q(description__icontains=q) 
        |Q(topic__name__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
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

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'base/delete.html', {'obj': room})