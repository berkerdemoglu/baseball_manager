from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Team, Player, Manager
from .forms import TeamForm, PlayerForm, ManagerForm
from .utils import check_team_owner


# Team views
@login_required
def teams(request):
	"""Page that lists all teams."""
	teams = Team.objects.filter(owner=request.user).order_by('city')
	context = {'teams': teams}
	return render(request, 'teams/teams.html', context)


@login_required
def team(request, team_id):
	"""Page for a single team."""
	team = Team.objects.get(id=team_id)
	check_team_owner(request, team)

	players = team.player_set.all().order_by('position')
	context = {'team': team, 'players': players, 'player_amount': len(players)}
	return render(request, 'teams/team.html', context)


@login_required
def new_team(request):
	"""Page for adding a new team."""
	if request.method != 'POST':
		form = TeamForm()
	else:
		# POST method, process the form.
		form = TeamForm(data=request.POST)
		if form.is_valid():
			new_team = form.save(commit=False)
			new_team.owner = request.user
			new_team.save()
			return redirect('teams:teams')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'teams/new_team.html', context)


@login_required
def remove_team(request, team_id):
	"""View for removing a team."""
	team = Team.objects.get(id=team_id)
	check_team_owner(request, team)

	team.delete()
	return redirect('teams:teams')


# Player views
@login_required
def player(request, player_id):
	"""Page for an individual player."""
	player = Player.objects.get(id=player_id)
	check_team_owner(request, player.team)

	context = {'player': player}
	return render(request, 'teams/player.html', context)


@login_required
def new_player(request, team_id):
	"""Page for adding a new player to a team."""
	team = Team.objects.get(id=team_id)
	check_team_owner(request, team)

	if request.method != 'POST':
		form = PlayerForm()
	else:
		# POST method, process the form.
		form = PlayerForm(data=request.POST)
		if form.is_valid():
			new_player = form.save(commit=False)
			new_player.team = team
			new_player.save()

			return redirect('teams:team', team_id=team_id)

	context = {'form': form, 'team': team}
	return render(request, 'teams/new_player.html', context)


@login_required
def remove_player(request, player_id):
	"""View for removing a player."""
	player = Player.objects.get(id=player_id)
	check_team_owner(request, player.team)

	team_id = player.team.id
	player.delete()
	return redirect('teams:team', team_id=team_id)


@login_required
def edit_player(request, player_id):
	"""Page for editing a player."""
	player = Player.objects.get(id=player_id)
	check_team_owner(request, player.team)

	if request.method != 'POST':
		# Fill form with previous info.
		form = PlayerForm(instance=player)
	else:
		# POST method, process the form.
		form = PlayerForm(instance=player, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('teams:player', player_id=player_id)

	context = {'form': form, 'player': player}
	return render(request, 'teams/edit_player.html', context)


# Manager views
@login_required
def manager(request, manager_id):
	"""Page for an individual manager."""
	manager = Manager.objects.get(id=manager_id)
	check_team_owner(request, manager.team)

	context = {'manager': manager}
	return render(request, 'teams/manager.html', context)


@login_required
def remove_manager(request, manager_id):
	"""View for removing a manager."""
	manager = Manager.objects.get(id=manager_id)
	check_team_owner(request, manager.team)

	team_id = manager.team.id
	manager.delete()
	return redirect('teams:team', team_id=team_id)


@login_required
def new_manager(request, team_id):
	"""Page for adding a manager to a team."""
	team = Team.objects.get(id=team_id)
	check_team_owner(request, team)

	if request.method != 'POST':
		form = ManagerForm()
	else:
		# POST method, process the form.
		form = ManagerForm(data=request.POST)
		if form.is_valid():
			new_manager = form.save(commit=False)
			new_manager.team = team
			new_manager.save()

		return redirect('teams:team', team_id=team_id)

	context = {'form': form, 'team': team}
	return render(request, 'teams/new_manager.html', context)


@login_required
def edit_manager(request, manager_id):
	"""Page for editing a manager."""
	manager = Manager.objects.get(id=manager_id)
	check_team_owner(request, manager.team)

	if request.method != 'POST':
		# Fill form with previous info.
		form = ManagerForm(instance=manager)
	else:
		# POST method, process the form.
		form = ManagerForm(instance=manager, data=request.POST)
		if form.is_valid():
			form.save()

		return redirect('teams:manager', manager_id=manager_id)

	context = {'form': form, 'manager': manager}
	return render(request, 'teams/edit_manager.html', context)
