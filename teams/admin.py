from django.contrib import admin
from .models import Position, Player, Team, Membership

# Register your models here.
admin.site.register(Position)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Membership)
