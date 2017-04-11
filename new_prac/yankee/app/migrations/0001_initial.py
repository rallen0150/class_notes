# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=3)),
                ('games', models.IntegerField()),
                ('plate_appearance', models.IntegerField()),
                ('at_bat', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('hits', models.IntegerField()),
                ('doubles', models.IntegerField()),
                ('triples', models.IntegerField()),
                ('homeruns', models.IntegerField()),
                ('rbi', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('caught_stealing', models.IntegerField()),
                ('walks', models.IntegerField()),
                ('strikeouts', models.IntegerField()),
                ('avg', models.FloatField()),
                ('obp', models.FloatField()),
                ('slg', models.FloatField()),
                ('ops_percentage', models.FloatField()),
                ('ops', models.IntegerField()),
                ('total_base', models.IntegerField()),
                ('gidp', models.IntegerField()),
                ('hbp', models.IntegerField()),
                ('sac_hit', models.IntegerField()),
                ('sac_fly', models.IntegerField()),
                ('ibb', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=3)),
                ('wins', models.CharField(max_length=10)),
                ('loss', models.CharField(max_length=10)),
                ('win_loss', models.CharField(max_length=10)),
                ('era', models.CharField(max_length=10)),
                ('games', models.CharField(max_length=10)),
                ('games_started', models.CharField(max_length=10)),
                ('games_finished', models.CharField(max_length=10)),
                ('complete_games', models.CharField(max_length=10)),
                ('shutout', models.CharField(max_length=10)),
                ('saves', models.CharField(max_length=10)),
                ('ip', models.CharField(max_length=10)),
                ('hits', models.CharField(max_length=10)),
                ('runs', models.CharField(max_length=10)),
                ('earned_runs', models.CharField(max_length=10)),
                ('hr', models.CharField(max_length=10)),
                ('walks', models.CharField(max_length=10)),
                ('ibb', models.CharField(max_length=10)),
                ('strikeouts', models.CharField(max_length=10)),
                ('hbp', models.CharField(max_length=10)),
                ('balks', models.CharField(max_length=10)),
                ('wild_pitch', models.CharField(max_length=10)),
                ('batters_faced', models.CharField(max_length=10)),
                ('erav', models.CharField(max_length=10)),
                ('fip', models.CharField(max_length=10)),
                ('whip', models.CharField(max_length=10)),
                ('h9', models.CharField(max_length=10)),
                ('hr9', models.CharField(max_length=10)),
                ('bb9', models.CharField(max_length=10)),
                ('so9', models.CharField(max_length=10)),
                ('sow', models.CharField(max_length=10)),
            ],
        ),
    ]
