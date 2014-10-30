# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(default=b'Honolulu', max_length=50)),
                ('state', models.CharField(default=b'HI', max_length=2)),
                ('zip_code', models.CharField(default=b'968', max_length=20)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minute', models.SmallIntegerField()),
                ('color', models.CharField(max_length=1, choices=[(b'Y', b'Yellow'), (b'R', b'Red')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=3)),
                ('logo', models.ImageField(upload_to=b'')),
                ('address', models.ForeignKey(blank=True, to='stats.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoachFor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True, blank=True)),
                ('responsiblity', models.CharField(default=b'C', max_length=1, choices=[(b'C', b'Coach'), (b'M', b'Manager'), (b'A', b'Assistant Coach')])),
                ('coach', models.ForeignKey(to='stats.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=5)),
                ('competition_type', models.CharField(max_length=1, choices=[(b'L', b'League'), (b'C', b'Cup'), (b'P', b'Playoffs'), (b'R', b'Relegation')])),
                ('belongs', models.ForeignKey(to='stats.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.ForeignKey(to='stats.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minute', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.ForeignKey(blank=True, to='stats.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(to='stats.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayFor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True, blank=True)),
                ('player', models.ForeignKey(to='stats.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(to='stats.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suspension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_received', models.DateField()),
                ('number_games', models.SmallIntegerField()),
                ('suspended_until', models.DateField()),
                ('reason', models.CharField(max_length=1000, blank=True)),
                ('fine', models.SmallIntegerField()),
                ('fine_paid', models.BooleanField(default=False)),
                ('player', models.ForeignKey(to='stats.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=3)),
                ('color_first', models.CharField(max_length=20)),
                ('color_second', models.CharField(max_length=20)),
                ('classification', models.CharField(max_length=5, choices=[(b'Men', ((b'mopen', b"Men's Open"), (b'mo35', b"Men's 35+"), (b'mo45', b"Men's Masters"))), (b'Women', ((b'women', b"Women's Open"),)), (b'Boys', ((b'bu19', b'Boys U19'), (b'bu16', b'Boys U16'), (b'bu14', b'Boys U14'), (b'bu12', b'Boys U12'))), (b'Girls', ((b'gu19', b'Girls U19'), (b'gu16', b'Girls U16'), (b'gu14', b'Girls U14'), (b'gu12', b'Girls U12')))])),
                ('club', models.ForeignKey(blank=True, to='stats.Club', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='season',
            name='enrolled',
            field=models.ManyToManyField(to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='season',
            name='of',
            field=models.ForeignKey(to='stats.Competition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playfor',
            name='team',
            field=models.ForeignKey(to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='registered',
            field=models.ManyToManyField(to='stats.Team', through='stats.PlayFor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='assisted_by',
            field=models.ForeignKey(related_name=b'goal_assisted_by', blank=True, to='stats.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='scored_against',
            field=models.ForeignKey(related_name=b'goal_scored_against', to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='scored_by',
            field=models.ForeignKey(related_name=b'goal_scored_by', to='stats.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='scored_for',
            field=models.ForeignKey(related_name=b'goal_scored_for', to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='scored_in',
            field=models.ForeignKey(to='stats.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(related_name=b'game_away_team', to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='field',
            field=models.ForeignKey(to='stats.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name=b'game_home_team', to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='referee',
            field=models.ForeignKey(to='stats.Referee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(to='stats.Season'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coachfor',
            name='team',
            field=models.ForeignKey(to='stats.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coach',
            name='person',
            field=models.ForeignKey(to='stats.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coach',
            name='registered',
            field=models.ManyToManyField(to='stats.Team', through='stats.CoachFor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='received_by',
            field=models.ForeignKey(to='stats.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='received_in',
            field=models.ForeignKey(to='stats.Game'),
            preserve_default=True,
        ),
    ]
