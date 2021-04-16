from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Page for registering a new user."""
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		# POST, process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user.save()
			login(request, new_user)  # log the user in
			return redirect('pages:index')

	context = {'form': form}
	return render(request, 'registration/register.html', context)
