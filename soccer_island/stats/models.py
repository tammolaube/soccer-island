from django.db import models

class Classification(models.Model):
    label = models.CharField(max_length=32, unique=True, help_text='Please provide a label for the classification e.g. \'Mens Open\'.')
    slug = models.SlugField(max_length=32, unique=True)
    def __unicode__(self):
        return self.label

class Address(models.Model):
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64, default='Honolulu')
    state = models.CharField(max_length=2, default='HI')
    zip_code = models.CharField(max_length=16, default='968')
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.street + ' ' + self.zip_code

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField()
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.ForeignKey(Address, blank=True, null=True)
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Club(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    address = models.ForeignKey(Address, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    colors = models.CharField(max_length=128)
    classification = models.ForeignKey(Classification)
    club = models.ForeignKey(Club, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Player(models.Model):
    person = models.ForeignKey(Person)
    registered = models.ManyToManyField(Team, through='PlayFor', through_fields=('player', 'team'))
    def __unicode__(self):
        return self.person.__unicode__()

class PlayFor(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.player.__unicode__() + ' at ' + self.team.__unicode__()

class Coach(models.Model):
    person = models.ForeignKey(Person)
    registered = models.ManyToManyField(Team, through='CoachFor', through_fields=('coach', 'team'))
    def __unicode__(self):
        return self.person.__unicode__()

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
    def __unicode__(self):
        return self.coach.__unicode__() + ' ' + self.team.__unicode__()

class Referee(models.Model):
    person = models.ForeignKey(Person)
    def __unicode__(self):
        return self.person.__unicode__()

class Field(models.Model):
    name = models.CharField(max_length=64)
    address = models.ForeignKey(Address)
    def __unicode__(self):
        return self.name

class Competition(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    MODE_CHOICES = (
            ('L', 'League'),
            ('C', 'Cup'),
            ('R', 'Relegation'),
        )
    mode = models.CharField(max_length=1, choices=MODE_CHOICES)
    classification = models.ForeignKey(Classification)
    def __unicode__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=16, help_text='Enter the \'name\' of the season in the format \'2014-2015\'.')
    slug = models.SlugField(max_length=16)
    start_date = models.DateField()
    end_date = models.DateField()
    of = models.ForeignKey(Competition)
    enrolled = models.ManyToManyField(Team)
    def __unicode__(self):
        return self.name

class Matchday(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    season = models.ForeignKey(Season)
    next_matchday = models.ForeignKey("self", blank=True, null=True)
    def __unicode__(self):
        return self.name

class Game(models.Model):
    date = models.DateField()
    away_team = models.ForeignKey(Team, related_name='game_away_team')
    home_team = models.ForeignKey(Team, related_name='game_home_team')
    referee = models.ForeignKey(Referee)
    field = models.ForeignKey(Field)
    matchday = models.ForeignKey(Matchday)
    # for tournaments so you can create a tree, and names (e.g. Semifinal A):
    next_game = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=64, blank=True)
    def __unicode__(self):
        return self.away_team.__unicode__() + ' vs. ' + self.home_team.__unicode__()

class Goal(models.Model):
    minute = models.SmallIntegerField()
    scored_by = models.ForeignKey(Player, related_name='goal_scored_by')
    assisted_by = models.ForeignKey(Player, related_name='goal_assisted_by', null=True, blank=True)
    scored_for = models.ForeignKey(Team, related_name='goal_scored_for')
    scored_in = models.ForeignKey(Game)
    def __unicode__(self):
        return self.scored_in.__unicode__() + ' ' + str(self.minute) + 'min'

class Card(models.Model):
    minute = models.SmallIntegerField()
    COLOR_CHOICES = (
            ('Y', 'Yellow'),
            ('R', 'Red'),
        )
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, null=False)
    received_by = models.ForeignKey(Player)
    received_in = models.ForeignKey(Game)
    def __unicode__(self):
        return self.received_in.__unicode__() + ' ' + str(self.minute) + 'min'

class Suspension(models.Model):
    date_received = models.DateField()
    number_games = models.SmallIntegerField()
    suspended_until = models.DateField()
    reason = models.CharField(max_length=1024, blank=True)
    fine = models.SmallIntegerField()
    fine_paid = models.BooleanField(default=False)
    player = models.ForeignKey(Player)
    def __unicode__(self):
        return self.player.__unicode__() + ' ' + self.date_received
