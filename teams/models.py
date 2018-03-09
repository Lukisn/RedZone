from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    home_country = models.CharField(max_length=50, null=True)
    home_city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.full_name()}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    short_team_name = models.CharField(max_length=20)
    home_city = models.CharField(max_length=50)
    home_page = models.URLField(max_length=100)
    members = models.ManyToManyField(Player, through="Membership")

    def __str__(self):
        return f"{self.team_name}"


class Position(models.Model):
    position_name = models.CharField(max_length=50)
    short_position_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.position_name}"


class Membership(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_released = models.DateField(null=True, blank=True)
    number = models.PositiveSmallIntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player} @ {self.team}"
