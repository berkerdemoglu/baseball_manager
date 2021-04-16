from django import forms
from django_countries.widgets import CountrySelectWidget

from .models import Team, Player, Manager


class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ['city', 'name']
		labels = {'city': 'City:', 'name': 'Name:'}
		widgets = {
			'city': forms.TextInput(attrs={'size': 30}),
			'name': forms.TextInput(attrs={'size': 30}),
		}


class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = ['name', 'position', 'team', 'country', 'jersey_number']
		labels = {
			'name': 'Name:', 'position': 'Position:', 
			'team': 'Team:', 'country': 'Country:',
			'jersey_number': 'Jersey Number:',
		}
		widgets = {
			'name': forms.TextInput(attrs={'size': 50, 'placeholder': 'Enter the player\'s name'}),
			'position': forms.Select(),
			'team': forms.Select(),
			'country': CountrySelectWidget(),
			'jersey_number': forms.NumberInput(),
		}


class ManagerForm(forms.ModelForm):
	class Meta:
		model = Manager
		fields = ['name', 'team', 'country', 'jersey_number']
		labels = {
			'name': 'Name:', 'team': 'Team:', 
			'country': 'Country:', 'jersey_number': 'Jersey Number',
		}
		widgets = {
			'name': forms.TextInput(attrs={'size': 50, 'placeholder': 'Enter the manager\'s name'}),
			'team': forms.Select(),
			'country': CountrySelectWidget(),
			'jersey_number': forms.NumberInput(),
		}
