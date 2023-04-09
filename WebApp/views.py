from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import LeagueProbsSerializer
from .models import LeagueProbs
from .algo import *
import logging

from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)

# Create your views here.
class LeagueCalculateView(APIView):
    def post(self, request):
        data = request.data
        serializer = LeagueProbsSerializer(data=data)
        #logger.debug(request.data)
        if serializer.is_valid():
            league = League(data['name'], data['total_games'], [])
            for row in data['rows']:
                league.teams.append(Team(row['team_name'], row['wins'], row['draws'], row['losses']))
            win_rates = calculate_probabs(league)
            for row in data['rows']:
                row['probab'] = win_rates[row['team_name']]
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeagueProbsView(viewsets.ModelViewSet):
    serializer_class = LeagueProbsSerializer
    queryset = LeagueProbs.objects.all()

catchall = TemplateView.as_view(template_name='index.html')

