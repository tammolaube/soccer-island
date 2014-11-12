import datetime
from django.test import TestCase
from models import Address, Field, Classification, Competition, Season, Matchday, Game, Goal, Person, Player, PlayFor, Referee, Team

class GoalsAssistsTest(TestCase):

    def test_goals_by_season(self):

        # create season
        classification = Classification(label='Mens')
        classification.save()
        competition = Competition(name='l1',mode='l',classification=classification)
        competition.save()
        season = Season(label='2014-2015', start_date=datetime.date.today(), end_date=datetime.date.today(), competition=competition)
        season.save()
        team = Team(name='team1', colors='red', classification=classification)
        team.save()
        person1 = Person(first_name='t', last_name='l', gender='M')
        person1.save()
        player1 = Player(person=person1)
        player1.save()
        # player1.playfor.add(team)
        playfor1 = PlayFor(player=player1, team=team, from_date=datetime.date.today())
        playfor1.save()
        person2 = Person(first_name='s', last_name='r', gender='M')
        person2.save()
        player2 = Player(person=person2)
        player2.save()
        # player1.playfor.add(team)
        playfor2 = PlayFor(player=player2, team=team, from_date=datetime.date.today())
        playfor2.save()
        referee = Referee(person=person2)
        referee.save()
        matchday = Matchday(season=season, label='1', date=datetime.date.today())
        matchday.save()
        address = Address(street='s')
        address.save()
        field = Field(name='f1', address=address)
        field.save()
        game = Game(matchday=matchday, date=datetime.date.today(), away_team=team, home_team=team, referee=referee, played=True, field=field)
        game.save()
        goal1 = Goal(scored_by=player1, assisted_by=player2,scored_for=team, game=game)
        goal1.save()
        goal2 = Goal(scored_by=player1, assisted_by=player2,scored_for=team, game=game)
        goal2.save()
        goal3 = Goal(scored_by=player2, assisted_by=player1,scored_for=team, game=game)
        goal3.save()

        self.assertEqual(season.count_goals(), 3)
        self.assertIn(player1, season.get_goal_scorers())