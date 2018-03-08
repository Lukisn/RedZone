from django.shortcuts import render, get_object_or_404
from .models import Team, Player


def teams(request):
    teams_list = Team.objects.all()
    return render(request, "teams/teams.html", {"teams_list": teams_list})


def team(request, team_id):
    team_data = get_object_or_404(Team, id=team_id)
    return render(request, "teams/team.html", {"team_data": team_data})


def players(request):
    return render(request, "teams/players.html")


def player(request, player_id):
    return render(request, "teams/player.html", {"player_id": player_id})
