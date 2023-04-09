from django.contrib import admin
from .models import LeagueProbs, LeagueRow

# Register your models here.
class LeagueProbsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class LeagueRowAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'league_id', 'wins', 'draws', 'losses', 'probab')

# Register your models here.

admin.site.register(LeagueProbs, LeagueProbsAdmin)
admin.site.register(LeagueRow, LeagueRowAdmin)