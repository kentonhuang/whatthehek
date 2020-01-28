from django.shortcuts import render
from api.models import Game, BoxScore
from api.serializers import GameSerializer, BoxScoreSerializer
from example.tasks import sel_test

from rest_framework import generics, status
from rest_framework.response import Response


import json
import time
import re
# Create your views here.

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, pk, *args, **kwargs):
        if Game.objects.filter(pk=self.kwargs.get('pk')).exists():
            game = Game.objects.get(pk=self.kwargs.get('pk'))
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class BoxScoreList(generics.ListCreateAPIView):
    queryset = BoxScore.objects.all()
    serializer_class = BoxScoreSerializer

class BoxScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoxScore.objects.all()
    serializer_class = BoxScoreSerializer

    def get(self, request, pk, *args, **kwargs):
        if BoxScore.objects.filter(pk=self.kwargs.get('pk')).exists():
            game = BoxScore.objects.get(pk=self.kwargs.get('pk'))
            serializer = BoxScoreSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            pkstr = str(pk)
            keys = {
                'id': pkstr,
                'game': pkstr   
            }
        new_boxscore = BoxScore.objects.create(**keys)
        serializer = BoxScoreSerializer(new_boxscore)
        return Response(serializer.data, status=status.HTTP_200_OK)
