from django.contrib import admin

from .models import Team, Player, Manager


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Manager)
