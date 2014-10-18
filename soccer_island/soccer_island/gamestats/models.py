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

class Player(models.Model):
    person = models.ForeignKey(Person)
    registered = models.ManyToManyField(Team, through='PlaysFor', through_fields=('player', 'team'))

class PlayFor(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

class Coach(models.Model):
   person = models.ForeignKey(Person)

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

class Referee(models.Model)
    person = models.ForeignKey(Person)

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

class Club(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=3)
    logo = models.ImageField()
    address = models.ForeignKey(Address, blank=True, null=True)
