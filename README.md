#SOCCER ISLAND - IS6065 PROJECT GROUP BY

This system is made for the Mayor Island Soccer Organization (MISO). It will be used by fans, players, coaches, referees, and administrators of MISO.

### User Interfaces

We will divide the system in two parts. Part A) will be open to everyone. Part B) will only be open to referees and administrators. Administrators will have access to more features than referees.  
Part A) is only consisting of data retrieval. It will display information about teams, divisions, schedules, results, stats, and standings of the MISO divisions, playoffs, and tournaments.  
Part B) is for creating and updating the system's data. Divisions, playoffs, tournaments, teams, players, schedules, games can be created and updated by administrators.  
Additionally administrators can create and update other users of part B), namely other administrators and referees. Referees can only update game information of games they have been assigned to.

#### Part A) 
There are two major competition categories divisons (with playoffs) and tournaments.  

Each division will have an overview page. Displayed on the overview are last games, upcoming games, standings, top goal scorers, top assists givers, top carded players (yellow/red).  
![overview](docs/division-overview.png)  
Each team playing in a division will have a team page that shows the team's roster. Additional information such as goals scored, number/minutes of games played,... can be displayed for each player.  
![team roster](docs/team-roster.png)  
Each division will have a schedule page that shows all upcoming games including dates for playoffs.  
![schedule](docs/schedule.png)  
Each division will have a playoffs page similar to the overview page. The schedule will be displayed here as well.  
![playoffs](docs/playoffs.png)  

Each tournament will have a overview page similar to the divisions overview page.  
![cup](docs/cup.png)  

For each competition there will be a player's stats page displaying goals, assists and cards.
![players stats](docs/players-stats.png)

#### Part B)
The plan is to develop part B) iteratively in two steps. Step one is to create all interfaces for the administrator, step two will consist of a season generator and the referee system.  
The adiministrator's interface will have pages to create, update, read and delete (crud) all entities and their relationships. Namely that would be crud:
- Divisions
- Cups
- Seasons
- Teams
- Players
- Matches
- Goals
- Cards

Optional there will be a referee system. The referee system will allow authenticated referees to create and update game data. Referees will be able to login and will be directed to a list of games they have been assigned to. Referees can select games from the list and insert information.

Optional there will be a season generator. A new Season will be created by selecting a year and all teams for the season. The system then generates all the matches for the season. The job of the adminstrator would then be to select dates for each matchday.

### Database Schema
![database schema](docs/miso.png)

### Architecture Choice
This system will be a web application and be accessible over the Internet. We will be using Django a python based web application framework. Our database will be MySQL. For styling the UI we will use the twitter bootstrap framework and jQuery.

### Physical Database Model
![Physical Database Model](docs/eer_diagram.png)

#### SQL Migration Statements
To see the generated SQL Statements click on this link: [Sql Migrations](docs/create_database.sql).

## Install (Development)
Instructions to install and run soccer-island for developing or testing it. This does not cover deployment into
an procduction environment.

#### Prerequisites
- Python 2.7 with (virtualenv) and pip
- MySQL Server 5.5
 - create a database 'soccer_island'
 - create a user 'django' identified by 'soccer' with all privileges on the database 'soccer_island'
 - load the file docs/dump.sql into the created 'soccer_island' database
- (git)

#### Process
Use git to download the repository, or manually download the repository as zip and extract it.
(Create a virtual python environment with virtualenv.) 
Use the tool pip together with the file docs/requirements.txt, to install all requirements for this project into the python environment.
Start the development server, by executing the file soccer_island/manage.py via terminal command 'pyhton manage.py runserver'.
The development server is now running on localhost.

## Instructions
To create a new season, you have to use the Django admin page.
Create all elements needed for a season, and mind the foreign key constrains,
which can be derived from the database model.
You will have to create:
- classification (mens, womens,...)
- competiton (division 1, tournament,...)
- season (instance of an competition, e.g. division 1 2014-2015)
- teams with players and coaches (use 'play fors', players and coaches need persons to exist)
- assign the teams to the season
- create matchdays for the season
- create games for matchdays (you will also need to create referees and fields)

The next step will be to create a navigation, that points to the season
instance. This will be a future step, and can hopefully be achieved by
integrating the app into a CMS system.

The season can now be browsed in a webserver. There is a login, which provides
access to forms that allow authorized users to update game data.

Also, see the screenshots in docs/Screenshots.
