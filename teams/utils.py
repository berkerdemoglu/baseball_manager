from django.http import Http404


def check_team_owner(request, team):
	"""Check that the team belongs to the user making a request."""
	if team.owner != request.user:
		raise Http404
