#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teams app url configuration."""
from django.urls import path
from . import views


urlpatterns = [
    path("team/", views.teams, name="teams"),
    path("team/<int:team_id>", views.team, name="team"),
    path("player/", views.players, name="players"),
    path("player/<int:player_id>", views.player, name="player"),
]
