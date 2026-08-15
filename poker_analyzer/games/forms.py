from django import forms
from .models import Game, PlayerSession

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['base_buy_in_value', 'initial_chips']

class PlayerSessionForm(forms.ModelForm):
    class Meta:
        model = PlayerSession
        fields = ['player']