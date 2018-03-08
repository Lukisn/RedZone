from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    home_city = models.CharField(max_length=50)
    home_page = models.URLField(max_length=100)

    def __str__(self):
        return f"{self.team_name}"


class Player(models.Model):
    POSITIONS = (  # TODO: extract in Position model?
        # Offense:
        ("C", "Center"),
        ("OL", "Offense line"),
        ("OG", "Offensive guard"),
        ("OT", "Offensive tackle"),
        ("QB", "Quarterback"),
        ("RB", "Running back"),  # FB "Full back", HB "Half back"
        ("WR", "Wide receiver"),
        ("TE", "Tight end"),
        # Defense:
        ("DL", "Defense line"),
        ("DT", "Defensive tackle"),
        ("DE", "Defensive end"),
        ("DB", "Defensive back"),
        ("MLB", "Middle line backer"),
        ("LB", "Line backer"),  # SLB "Strongside LB", WLB "Weakside LB"
        ("CB", "Corner back"),
        ("S", "Safety"),  # SF "Strong safety", FS "Free safety"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    home_country = models.CharField(max_length=50, null=True)
    home_city = models.CharField(max_length=50, null=True)
    # TODO: extract into many to many relationship?!
    number = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=50, choices=POSITIONS)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name()}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
