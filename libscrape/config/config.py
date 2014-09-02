from libscrape.config import db


dbconn_prod_nba = {
    'user': 'monty',
    'passwd': 'python',
    'db': 'nbascrape'
}

dbconn_prod_wnba = {
    'user': 'monty',
    'passwd': 'python',
    'db': 'nbascrape'
}

dbconn_test = {
    'user': 'monty',
    'passwd': 'python',
    'db': 'nbascrape'
}

config = {}

# Database credential for main ETL run
config['db'] = dbconn_prod_nba

# Current season and season type
config['season'] = '2012-2013'
config['season_type'] = 'REG'
config['league'] = 'nba' # nba, wnba


season = '2012-2013'
season_type = 'REG'

league = {
    'nba': {
        'db': dbconn_prod_nba,
        'season': '2012-2013',
        'season_type': 'REG',
        'league': 'nba'
    },
    'wnba': {
        'db': dbconn_prod_wnba,
        'season': '2013',
        'season_type': 'REG',
        'league': 'wnba'
    }
}
