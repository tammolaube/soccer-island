from django.db import models

class HawaiiAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50, default='Honolulu')
    zip_code = models.CharField(max_length=20, default='968')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, default='M')
    address = models.ForeignKey(HawaiiAddress, blank=True, null=True)

class Player(models.Model):
    person = models.ForeignKey(Person)

class Coach(models.Model):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    RESPONSIBILITY_CHOICES = (
            ('C', 'Coach'),
            ('M', 'Manager'),
            ('A', 'Assistant Coach'),
        )
    responsiblity = models.CharField(max_length=1, choices=RESPONSIBILITY_CHOICES, null=False, default='C')
    person = models.ForeignKey(Person)

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
