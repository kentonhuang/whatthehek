from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
class Game(models.Model):
  id = models.IntegerField(primary_key=True)
  date = models.DateField(auto_now=False, auto_now_add=False)
  away_team = models.IntegerField()
  away_team_name = models.TextField(default="a")
  home_team = models.IntegerField()
  home_team_name = models.TextField(default="h")
  box_score = models.IntegerField()

class BoxScore(models.Model):
  id = models.IntegerField(primary_key=True)
  game = models.IntegerField()
  score_away = models.IntegerField(default=0)
  score_home = models.IntegerField(default=0)
  starters = JSONField(default=list, blank=True, null=True)
  away = JSONField(default=list, blank=True, null=True)
  home = JSONField(default=list, blank=True, null=True)
  a_q1 = JSONField(default=list, blank=True, null=True)
  a_q2 = JSONField(default=list, blank=True, null=True)
  a_q3 = JSONField(default=list, blank=True, null=True)
  a_q4 = JSONField(default=list, blank=True, null=True)
  h_q1 = JSONField(default=list, blank=True, null=True)
  h_q2 = JSONField(default=list, blank=True, null=True)
  h_q3 = JSONField(default=list, blank=True, null=True)
  h_q4 = JSONField(default=list, blank=True, null=True)

