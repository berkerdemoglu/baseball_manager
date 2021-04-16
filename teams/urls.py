"""teams URL configuration."""

from django.urls import path

from . import views


# Every pattern has teams/ before it.
urlpatterns = [
	# Page listing all teams
	path('', views.teams, name='teams'),

	# Individual page for a team
	path('<int:team_id>/', views.team, name='team'),

	# Page for adding a new team
	path('new_team/', views.new_team, name='new_team'),

	# Page for removing a team
	path('remove_team/<int:team_id>/', views.remove_team, name='remove_team'),

	# Individual page for a player
	path('players/<int:player_id>/', views.player, name='player'),

	# Page for adding a new player
	path('<int:team_id>/new_player/', views.new_player, name='new_player'),

	# Page for removing a player from team
	path('players/remove_player/<int:player_id>/', views.remove_player, name='remove_player'),

	# Page for editing a player
	path('players/edit_player/<int:player_id>/', views.edit_player, name='edit_player'),

	# Page for an individual manager
	path('managers/<int:manager_id>/', views.manager, name='manager'),

	# Page for removing a manager
	path('managers/remove_manager/<int:manager_id>/', views.remove_manager, name='remove_manager'),

	# Page for adding a manager
	path('<int:team_id>/new_manager/', views.new_manager, name='new_manager'),

	# Page for editing a manager
	path('managers/edit_manager/<int:manager_id>/', views.edit_manager, name='edit_manager'),
]
