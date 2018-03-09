from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Team, Player


def teams(request):
    team_list = Team.objects.all()
    return render(request, "teams/teams.html", {"team_list": team_list})


def team(request, team_id):
    team_data = get_object_or_404(Team, id=team_id)
    now = timezone.now()
    current_members = team_data.membership_set\
        .filter(date_joined__lte=now)\
        .exclude(date_released__lte=now)
    previous_members = team_data.membership_set\
        .filter(date_released__lte=now)
    return render(request, "teams/team.html", {
        "team_data": team_data,
        "current_members": current_members,
        "previous_members": previous_members,
    })


def players(request):
    player_list = Player.objects.all()
    return render(request, "teams/players.html", {"player_list": player_list})


def player(request, player_id):
    player_data = get_object_or_404(Player, id=player_id)
    now = timezone.now()
    current_teams = player_data.membership_set\
        .filter(date_joined__lte=now)\
        .exclude(date_released__lte=now)
    previous_teams = player_data.membership_set\
        .filter(date_released__lte=now)
    return render(request, "teams/player.html", {
        "player_data": player_data,
        "current_teams": current_teams,
        "previous_teams": previous_teams,
    })
