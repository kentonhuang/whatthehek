from rest_framework import serializers
from api.models import Game, BoxScore

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class BoxScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxScore
        fields = '__all__'