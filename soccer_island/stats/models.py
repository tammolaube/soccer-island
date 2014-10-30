from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50, default='Honolulu')
    state = models.CharField(max_length=2, default='HI')
    zip_code = models.CharField(max_length=20, default='968')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, default='M')
    address = models.ForeignKey(Address, blank=True, null=True)

class Club(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=3)
    logo = models.ImageField()
    address = models.ForeignKey(Address, blank=True, null=True)

class Team(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=3)
    color_first = models.CharField(max_length=20)
    color_second = models.CharField(max_length=20)
    CLASSIFICATION_CHOICES = (
            ('Men', (
                    ('mopen', 'Men\'s Open'),
                    ('mo35', 'Men\'s 35+'),
                    ('mo45', 'Men\'s Masters'),
                ),
            ),
            ('Women', (
                    ('women', 'Women\'s Open'),
                ),
            ),
            ('Boys', (
                    ('bu19', 'Boys U19'),
                    ('bu16', 'Boys U16'),
                    ('bu14', 'Boys U14'),
                    ('bu12', 'Boys U12'),
                ),
            ),
            ('Girls', (
                    ('gu19', 'Girls U19'),
                    ('gu16', 'Girls U16'),
                    ('gu14', 'Girls U14'),
                    ('gu12', 'Girls U12'),
                ),
            ),
        )
    classification = models.CharField(max_length=5, choices=CLASSIFICATION_CHOICES)
    club = models.ForeignKey(Club, blank=True, null=True)

class Player(models.Model):
    person = models.ForeignKey(Person)
    registered = models.ManyToManyField(Team, through='PlayFor', through_fields=('player', 'team'))

class PlayFor(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

class Coach(models.Model):
    person = models.ForeignKey(Person)
    registered = models.ManyToManyField(Team, through='CoachFor', through_fields=('coach', 'team'))

class CoachFor(models.Model):
    coach = models.ForeignKey(Coach)
    team = models.ForeignKey(Team)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    RESPONSIBILITY_CHOICES = (
            ('C', 'Coach'),
            ('M', 'Manager'),
            ('A', 'Assistant Coach'),
        )
    responsiblity = models.CharField(max_length=1, choices=RESPONSIBILITY_CHOICES, null=False, default='C')

class Referee(models.Model):
    person = models.ForeignKey(Person)

class Field(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address)

class Competition(models.Model):
    name = models.CharField(max_length=50)
    TYPE_CHOICES = (
            ('L', 'League'),
            ('C', 'Cup'),
            ('P', 'Playoffs'),
            ('R', 'Relegation'),
        )
    short_name = models.CharField(max_length=5)
    competition_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    belongs = models.ForeignKey("self")

class Season(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    of = models.ForeignKey(Competition)
    enrolled = models.ManyToManyField(Team)

class Game(models.Model):
    date = models.DateField()
    away_team = models.ForeignKey(Team, related_name='game_away_team')
    home_team = models.ForeignKey(Team, related_name='game_home_team')
    referee = models.ForeignKey(Referee)
    field = models.ForeignKey(Field)
    season = models.ForeignKey(Season)

class Goal(models.Model):
    minute = models.SmallIntegerField()
    scored_by = models.ForeignKey(Player, related_name='goal_scored_by')
    assisted_by = models.ForeignKey(Player, related_name='goal_assisted_by', null=True, blank=True)
    scored_for = models.ForeignKey(Team, related_name='goal_scored_for')
    scored_against = models.ForeignKey(Team, related_name='goal_scored_against')
    scored_in = models.ForeignKey(Game)

class Card(models.Model):
    minute = models.SmallIntegerField()
    COLOR_CHOICES = (
            ('Y', 'Yellow'),
            ('R', 'Red'),
        )
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, null=False)
    received_by = models.ForeignKey(Player)
    received_in = models.ForeignKey(Game)

class Suspension(models.Model):
    date_received = models.DateField()
    number_games = models.SmallIntegerField()
    suspended_until = models.DateField()
    reason = models.CharField(max_length=1000, blank=True)
    fine = models.SmallIntegerField()
    fine_paid = models.BooleanField(default=False)
    player = models.ForeignKey(Player)
