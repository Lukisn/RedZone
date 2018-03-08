from django.shortcuts import render


def teams(request):
    return render(request, "teams/teams.html")


def team(request, team_id):
    return render(request, "teams/team.html", {"team_id": team_id})


def players(request):
    return render(request, "teams/players.html")


def player(request, player_id):
    return render(request, "teams/player.html", {"player_id": player_id})
