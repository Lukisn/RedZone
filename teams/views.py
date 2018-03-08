from django.shortcuts import render
from django.http import HttpResponse


def index(request):  # TODO: extract into index app
    # return HttpResponse("teams index page")
    return render(request, "teams/index.html")


def teams(request):
    # return HttpResponse("teams overview page")
    return render(request, "teams/teams.html")


def team(request, team_id):
    # return HttpResponse(f"team details page for team {team_id}")
    return render(request, "teams/team.html", {"team_id": team_id})


def players(request):
    # return HttpResponse("players overview page")
    return render(request, "teams/players.html")


def player(request, player_id):
    #return HttpResponse(f"player details page for player {player_id}")
    return render(request, "teams/player.html", {"player_id": player_id})
