from django.shortcuts import render
from .forms import GameForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    return render(request, 'games/index.html')

def create_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)

        if form.is_valid():
            nova_partida = form.save()
            
            return HttpResponseRedirect(reverse('index'))

    context = {'form' : form}

    return render(request, 'games/create_game.html', context)