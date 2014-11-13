import datetime
from django.test import TestCase
from models import Address, Field, Classification, Competition, Season, Matchday, Game, Goal, Person, Player, PlayFor, Referee, Team, Card


def create_classification(label):

    classification = Classification(label=label)
    classification.save()

    return classification

def create_season(classification, competition, season_label, start, end):

    competition = Competition(
        name=competition,
        mode='l',
        classification=classification
    )
    competition.save()
    season = Season(label=season_label,
        start_date=start,
        end_date=end,
        competition=competition
    )
    season.save()

    return season

def create_team(name, classification):

    team = Team(name=name, colors='red', classification=classification)
    team.save()

    return team

def create_player(first, last):

    person = Person(first_name=first, last_name=last)
    person.save()
    player = Player(person=person)
    player.save()

    return player


class SeasonTest(TestCase):

    def setUp(self):

        # create classifcation
        self.classification = create_classification('Men\'s Open')

        # create an Address and a Field
        self.address = Address(street='ABC Street')
        self.address.save()
        self.field = Field(name='Field 1', address=self.address)
        self.field.save()

        # create a team
        self.team_1 = create_team('Team 1', self.classification)

        # create some players
        self.player_1 = create_player('One', '1')
        self.player_2 = create_player('Two', '2')
        self.player_3 = create_player('Three', '3')

        # assign the players
        self.playfor_1 = PlayFor(player=self.player_1, team=self.team_1, from_date=datetime.date.today())
        self.playfor_1.save()
        self.playfor_2 = PlayFor(player=self.player_2, team=self.team_1, from_date=datetime.date.today())
        self.playfor_2.save()
        self.playfor_3 = PlayFor(player=self.player_3, team=self.team_1, from_date=datetime.date.today())
        self.playfor_3.save()

        # create referee
        person = Person(first_name='Ref', last_name='Ref')
        person.save()
        self.referee = Referee(person=person)
        self.referee.save()

        # create two seasons
        self.season_1 = create_season(self.classification, 'Division 1', '2014-2015', datetime.date.today(), datetime.date.today())
        self.season_2 = create_season(self.classification, 'Division 2', '2015-2016', datetime.date.today(), datetime.date.today())

        # create some games
        self.matchday_season_1 = Matchday(season=self.season_1, label='1', date=datetime.date.today())
        self.matchday_season_1.save()
        self.game_season_1 = Game(matchday=self.matchday_season_1, date=datetime.date.today(),
            away_team=self.team_1, home_team=self.team_1, referee=self.referee,
            played=True, field=self.field)
        self.game_season_1.save()

        self.matchday_season_2 = Matchday(season=self.season_2, label='2', date=datetime.date.today())
        self.matchday_season_2.save()
        self.game_season_2 = Game(matchday=self.matchday_season_2, date=datetime.date.today(),
            away_team=self.team_1, home_team=self.team_1, referee=self.referee,
            played=True, field=self.field)
        self.game_season_2.save()


    def test_goals_by_season(self):

        goal_1 = Goal(scored_by=self.player_1, scored_for=self.team_1, game=self.game_season_1)
        goal_1.save()
        self.assertEqual(1, self.season_1.count_goals())
        self.assertIn(self.player_1, self.season_1.get_goal_scorers())

        goal_2 = Goal(scored_by=self.player_1, scored_for=self.team_1, game=self.game_season_1)
        goal_2.save()
        self.assertEqual(2, self.season_1.count_goals())
        self.assertIn(self.player_1, self.season_1.get_goal_scorers())

        goal_3 = Goal(scored_by=self.player_2, scored_for=self.team_1, game=self.game_season_2)
        goal_3.save()
        self.assertEqual(2, self.season_1.count_goals())
        self.assertNotIn(self.player_2, self.season_1.get_goal_scorers())
        self.assertIn(self.player_2, self.season_2.get_goal_scorers())

        goal_4 = Goal(scored_by=self.player_3, scored_for=self.team_1, game=self.game_season_1, own_goal=True)
        goal_4.save()
        self.assertEqual(3, self.season_1.count_goals())
        self.assertNotIn(self.player_3, self.season_1.get_goal_scorers())

    def test_carded_players_of_season(self):

        yellow_card_1 = Card(color='Y', play_for=self.playfor_1, in_game=self.game_season_1)
        yellow_card_1.save()
        self.assertIn(self.playfor_1, self.season_1.get_yellow_carded_playfors())
        self.assertNotIn(self.playfor_2, self.season_1.get_yellow_carded_playfors())
        red_card_1 = Card(color='R', play_for=self.playfor_3, in_game=self.game_season_1)
        red_card_1.save()
        self.assertNotIn(self.playfor_3, self.season_1.get_yellow_carded_playfors())
        self.assertIn(self.playfor_3, self.season_1.get_red_carded_playfors())

        yellow_card_2 = Card(color='Y', play_for=self.playfor_1, in_game=self.game_season_1)
        yellow_card_2.save()
        yellow_card_3 = Card(color='Y', play_for=self.playfor_2, in_game=self.game_season_1)
        yellow_card_3.save()
        yellow_card_4 = Card(color='Y', play_for=self.playfor_1, in_game=self.game_season_2)
        yellow_card_4.save()

        num_of_yellows = self.player_1.get_num_of_yellow_cards_per(self.season_1)
        self.assertEqual(num_of_yellows, 2)
