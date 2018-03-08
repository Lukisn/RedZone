from django.shortcuts import render, get_object_or_404
from .models import Team, Player


def teams(request):
    team_list = Team.objects.all()
    return render(request, "teams/teams.html", {"team_list": team_list})


def team(request, team_id):
    team_data = get_object_or_404(Team, id=team_id)
    return render(request, "teams/team.html", {"team_data": team_data})


def players(request):
    player_list = Player.objects.all()
    return render(request, "teams/players.html", {"player_list": player_list})


def player(request, player_id):
    player_data = get_object_or_404(Player, id=player_id)
    return render(request, "teams/player.html", {"player_data": player_data})
