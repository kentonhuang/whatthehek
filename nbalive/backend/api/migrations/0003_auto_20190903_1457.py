# Generated by Django 2.2 on 2019-09-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190903_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxscore',
            name='score_away',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='boxscore',
            name='score_home',
            field=models.IntegerField(default=0),
        ),
    ]
