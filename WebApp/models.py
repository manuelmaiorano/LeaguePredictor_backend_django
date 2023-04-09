from django.db import models
from django.core.validators import MinValueValidator

class LeagueProbs(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    total_games = models.PositiveIntegerField(default=38)

class LeagueRow(models.Model):
    league_id = models.ForeignKey(LeagueProbs, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)
    wins = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    draws = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    losses = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    probab = models.FloatField(validators=[MinValueValidator(0.0)])