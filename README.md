#SOCCER ISLAND - PROPOSAL IS6050 PROJECT GROUP BY

This system is made for the Mayor Island Soccer Organization (MISO). It will be used by fans, players, coaches, referees, and administrators of MISO.

### Architecture Choice

This system will be a web application and be accessible over the Internet. We will be using Django a python based web application framework. Our database will be MySQL. For styling the UI we will use the twitter bootstrap framework and jQuery.

### User Interfaces

We will divide the system in two parts. Part A) will be open to everyone. Part B) will only be open to referees and administrators. Administrators will have access to more features than referees.  
Part A) is only consisting of data retrieval. It will display information about teams, divisions, schedules, results, stats, and standings of the MISO divisions, playoffs, and tournaments.  
Part B) is for creating and updating the system's data. Divisions, playoffs, tournaments, teams, players, schedules, games can be created and updated by administrators.  
Additionally administrators can create and update other users of part B), namely other administrators and referees. Referees can only update game information of games they have been assigned to.

#### Part A) 
There are two major competition categories divisons (with playoffs) and tournaments.  
Each division will have an overview page. Displayed on the overview are last games, upcoming games, standings, top goal scorers, top assists givers, top carded players (yellow/red).  
Each team playing in a division will have a team page that shows the team's roster. Additional information such as goals scored, number/minutes of games played,... can be displayed for each player.  
Each division will have a schedule page that shows all upcoming games including dates for playoffs.  
Each division will have a playoffs page similar to the overview page. The schedule will be displayed here as well.  
Each tournament will have a overview page similar to the divisions overview page.  

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
