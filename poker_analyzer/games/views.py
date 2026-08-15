from django.shortcuts import render, get_object_or_404
from .forms import GameForm, PlayerSessionForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Game, PlayerSession

# Create your views here.
def index(request):
    games = Game.objects.all()

    context = {'games' : games}

    return render(request, 'games/index.html', context)

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

def game_panel(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    players_at_table = PlayerSession.objects.filter(game=game)

    if request.method != 'POST':
        form = PlayerSessionForm()
    else:
        form = PlayerSessionForm(data=request.POST)

        if form.is_valid():
            nova_sessao = form.save(commit=False)
            nova_sessao.game = game
            nova_sessao.save()

            return HttpResponseRedirect(reverse('game_panel', args=[game.id]))

    context = {'form' : form, 'players_at_table' : players_at_table, 'game' : game}

    return render(request, 'games/game_panel.html', context)

def add_rebuy(request, session_id):
    sessao = get_object_or_404(PlayerSession, id = session_id)

    sessao.rebuys += 1
    sessao.save()

    return HttpResponseRedirect(reverse('game_panel', args=[sessao.game.id]))

def end_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    players = PlayerSession.objects.filter(game=game)

    if request.method == 'POST':
        for session in players:
            # pega o valor digitado no input chips_X
            fichas = request.POST.get(f'chips_{session.id}')
            if fichas:
                session.final_chips = int(fichas)
                session.save()

        # desativa a mesa pra ninguem dar rebuy fantasma
        game.is_active = False
        game.save()

        return HttpResponseRedirect(reverse('index'))
    
    context = {'game' : game, 'players': players}

    return render(request, 'games/end_game.html', context)
    
        