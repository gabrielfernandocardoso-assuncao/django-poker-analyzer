from django.contrib import admin
from .models import Game, Player, PlayerSession

# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerSession)

