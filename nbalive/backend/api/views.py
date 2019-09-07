from django.shortcuts import render
from api.models import Game, BoxScore
from api.serializers import GameSerializer, BoxScoreSerializer

from rest_framework import generics, status
# Create your views here.

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class BoxScoreList(generics.ListCreateAPIView):
    queryset = BoxScore.objects.all()
    serializer_class = BoxScoreSerializer

class BoxScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoxScore.objects.all()
    serializer_class = BoxScoreSerializer
