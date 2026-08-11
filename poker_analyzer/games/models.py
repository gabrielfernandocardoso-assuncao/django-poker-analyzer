from django.db import models

# Create your models here.
class Player(models.Model):
    # name
    name = models.CharField(max_length=200)
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    # date
    date = models.DateField()
    # base_buy_in_value
    base_buy_in_value = models.DecimalField
    # initial_chips
    initial_chips = models.IntegerField()
    # is_active
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"O jogo da data {self.date} está {'aberto' if self.is_active else 'Fechado'}"

class PlayerSession(models.Model):
    # player
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # rebuys
    rebuys = models.IntegerField(default=0)
    # final_chips
    final_chips = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Sessão encerrada com {self.final_chips if self.final_chips else 0} moedas."