from rest_framework import serializers
from .models import LeagueProbs, LeagueRow


class LeagueRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueRow
        fields = ('team_name', 'wins', 'draws', 'losses', 'probab')

class LeagueProbsSerializer(serializers.ModelSerializer):
    rows = LeagueRowSerializer(many=True, source='leaguerow_set')
    class Meta:
        model = LeagueProbs
        fields = ('name', 'description', 'total_games', 'rows')
        depth = 1

    def validate(self, attrs):
        for row in attrs['leaguerow_set']:
            if not LeagueRowSerializer(data=row).is_valid():
                raise serializers.ValidationError('team data not valid')
            if not row['wins'] + row['losses'] + row['draws'] < attrs['total_games']:
                raise serializers.ValidationError('sum of wins, losses and draws must be lower than total league games')
        return attrs

    def create(self, validated_data):
        rows = validated_data.pop('leaguerow_set')
        leagueprobs = LeagueProbs.objects.create(**validated_data)
        for row in rows:
            LeagueRow.objects.create(league_id=leagueprobs, **row)
        return leagueprobs