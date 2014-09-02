# PLAY BY PLAY AND BOX SCORE SCRAPING LIBRARY


## Requirements


This library was created on a Mac, so the setup instructions are geared toward a *nix environment (sorry Windows users)

* Python 2.5 or greater
* MySQL
* MySQLdb - Python's API to the MySQL database

TODO: Add postgres, sqlite support

## Instructions


* Clone the repository to your local machine (change your_folder_path to whatever folder you want to put the repo)

```
cd your_folder_path
git clone git@github.com:kpascual/nbascrape.git
```

* Add this new directory to your PYTHONPATH in ~/.bash_profile

```
PYTHONPATH="/your_folder_path/nbascrape:$PYTHONPATH"
export PYTHONPATH
```

* add mysql lib to ld library path

```sh
export DYLD_LIBRARY_PATH=/path_to_mysql/mysql-version/lib/:$DYLD_LIBRARY_PATH
```

* Go to the libscrape/config
* Copy constants_example.py to constants.py, and edit rows 3-8 in constants.py with the path containing this repo.

```
cd libscrape/config
cp constants_example.py constants.py
```

* Copy db_example.py to db.py

```
cp db_example.py db.py
```

* In config.py, enter your MySQL database credentials
```
vi db.py

  4 dbconn_prod_nba = {
  5     'user': 'username_for_database',
  6     'passwd': 'password__for_database',
  7     'db': 'production_database_name'
  8 }
```

* Finally, load the database with the required tables and data

```
cd your_path_here/schema
mysql -u user_name -p database_name < core_schema.sql
mysql -u user_name -p database_name < core_data.sql
mysql -u user_name -p database_name < game_data.sql
```

To actually do scraping, run the master.py file within the libscrape directory, and enter the date (YYYY-MM-DD) of the games that you want to scrape.

```
cd your_path_here/libscrape
python master.py 2012-10-30
```

## Extract scripts

To run batch script generator, first install Node.js and NPM. After that, install dependencies using command :

```sh
npm install moment
```

run the batch script generator 

```sh
node extractScriptGen.js
```


## issues

```
extracting 2013-04-16  2014-01-29   2013-12-04
Traceback (most recent call last):
  File "master.py", line 89, in <module>
    main()
  File "master.py", line 85, in main
    scrapeDailyAuto(dt, files)
  File "master.py", line 50, in scrapeDailyAuto
    scrape(dbobj, dt, files)
  File "master.py", line 68, in scrape
    clean.main.go(gamedata, dbobj)
  File "/Users/pan/git/nbascrape/libscrape/clean/main.py", line 116, in go
    obj.resolveNewPlayers()
  File "/Users/pan/git/nbascrape/libscrape/clean/player.py", line 37, in resolveNewPlayers
    players = self.getPlayers()
  File "/Users/pan/git/nbascrape/libscrape/clean/player.py", line 51, in getPlayers
    players = team.findAll("pl")
AttributeError: 'NoneType' object has no attribute 'findAll'


extracting 2013-11-17  2014-02-07 2014-02-12 2014-03-05
Traceback (most recent call last):
  File "master.py", line 89, in <module>
    main()
  File "master.py", line 85, in main
    scrapeDailyAuto(dt, files)
  File "master.py", line 50, in scrapeDailyAuto
    scrape(dbobj, dt, files)
  File "master.py", line 68, in scrape
    clean.main.go(gamedata, dbobj)
  File "/Users/pan/git/nbascrape/libscrape/clean/main.py", line 135, in go
    globals()["func_" + f](gamedata,files[f], dbobj)
  File "/Users/pan/git/nbascrape/libscrape/clean/main.py", line 72, in func_playbyplay_espn
    pbp_espn.Clean(**pbpvars).cleanAll()
  File "/Users/pan/git/nbascrape/libscrape/clean/pbp_espn.py", line 76, in cleanAll
    all_plays = function_name(all_plays)
  File "/Users/pan/git/nbascrape/libscrape/clean/pbp_espn.py", line 132, in replaceBlankScores
    if data[0]['away_score'] == '':
IndexError: list index out of range
```

