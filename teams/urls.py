#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""..."""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("teams", views.teams, name="teams"),
    path("team/<int:team_id>", views.team, name="team"),
    path("players", views.players, name="players"),
    path("player/<int:player_id>", views.player, name="player"),
]