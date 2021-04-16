from django.db import models
from django_countries.fields import CountryField


class Team(models.Model):
	"""A baseball team."""
	city = models.CharField(max_length=80)
	name = models.CharField(max_length=50)

	fullname = models.CharField(max_length=130, blank=True)

	def __str__(self):
		"""String representation of a team."""
		return f'{self.city} {self.name}'.title()

	def save(self, *args, **kwargs):
		"""Create fullname field when saving."""
		self.fullname = str(self)
		super().save(*args, **kwargs)


class Player(models.Model):
	"""A baseball player on a team."""
	PLAYER_POSITIONS = (
			('P', 'Pitcher'),
			('C', 'Catcher'),
			('1B', 'First Baseman'),
			('2B', 'Second Baseman'),
			('3B', 'Third Baseman'),
			('SS', 'Shortstop'),
			('LF', 'Left Fielder'),
			('CF', 'Center Fielder'),
			('RF', 'Right Fielder'),
		)

	name = models.CharField(max_length=110)
	position = models.CharField(max_length=2, choices=PLAYER_POSITIONS)
	team = models.ForeignKey(Team, models.CASCADE)
	country = CountryField(blank_label='(Select nationality)')
	jersey_number = models.PositiveSmallIntegerField()

	def __str__(self):
		"""String representation of a player."""
		return f'{self.name.title()}, {self.position} #{self.jersey_number}'


	# Position properties
	@property
	def is_outfielder(self):
		return self.position in ('LF', 'CF', 'RF')

	@property
	def is_infielder(self):
		return self.position in ('1B', '2B', '3B', 'SS')

	@property
	def is_pitcher(self):
		return self.position == 'P'

	@property
	def is_catcher(self):
		return self.position == 'C'

	@property
	def numerical_position(self):
		numerical_positions = {
			'P': 1, 'C': 2, '1B': 3,
			'2B': 4, '3B': 5, 'SS': 6,
			'LF': 7, 'CF': 8, 'RF': 9,
		}

		return numerical_positions[self.position]


class Manager(models.Model):
	"""The manager of a baseball team."""
	name = models.CharField(max_length=110)
	team = models.OneToOneField(Team, models.CASCADE)
	country = CountryField(blank_label='(Select nationality)')
	jersey_number = models.PositiveSmallIntegerField()

	def __str__(self):
		"""String representation of a player."""
		return f'{self.name.title()}, Manager of {self.team}, #{self.jersey_number}'
