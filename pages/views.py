from django.shortcuts import render


def index(request):
	"""The home page of Baseball Manager."""
	return render(request, 'pages/index.html')


def help(request):
	"""The help page."""
	return render(request, 'pages/help.html')
