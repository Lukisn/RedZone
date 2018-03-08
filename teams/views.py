from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("teams index page")


def teams(request):
    return HttpResponse("teams overview page")


def team(request, team_id):
    return HttpResponse(f"team details page for team {team_id}")


def players(request):
    return HttpResponse("players overview page")


def player(request, player_id):
    return HttpResponse(f"player details page for player {player_id}")
