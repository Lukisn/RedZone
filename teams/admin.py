from django.contrib import admin
from .models import Position, Player, Team, Membership

# TODO: tweak admin views
admin.site.register(Position)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Membership)
