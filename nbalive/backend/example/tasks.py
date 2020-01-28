import time
import json

from celery import shared_task
from celery.utils.log import get_task_logger

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from api.models import Game, BoxScore

logger = get_task_logger(__name__)

@shared_task
def test_task():
  logger.info('test task ran')

@shared_task
def sel_test(gameid):

  logger.info(gameid)

  options = webdriver.ChromeOptions()
  options.add_argument('--verbose')
  options.add_argument("--whitelisted-ips")
  options.add_argument("--start-maximized")                                                                                                                                

  capabilities = options.to_capabilities()

  driver = webdriver.Remote(
      command_executor='http://172.18.0.4:4444/wd/hub',
      desired_capabilities=capabilities,
  )

  left = 0
  right = 1800
  
  while right <= 28800:
    url = 'https://stats.nba.com/game/%s/?StartRange=%s&EndRange=%s&RangeType=2' %(gameid, left, right)
    driver.get(url) 
    time.sleep(8)

    

    tables = driver.find_elements_by_class_name('nba-stat-table__overflow')
    players1 = tables[0].find_elements_by_xpath('.//table/tbody/tr')
    players2 = tables[1].find_elements_by_xpath('.//table/tbody/tr')

    minutes = int(right/600)

    away_box = {
      'time': minutes,
      'players': {}
    }
    home_box = {
      'time': minutes,
      'players': {}
    }

    for player in players1:
      rows = player.find_elements_by_tag_name('td')
      player = rows[0].text
      away_box['players'][player] = {}
      away_box['players'][player]['minutes'] = rows[1].text
      away_box['players'][player]['FGM'] = rows[2].text
      away_box['players'][player]['FGA'] = rows[3].text
      away_box['players'][player]['3PM'] = rows[5].text
      away_box['players'][player]['3PA'] = rows[6].text
      away_box['players'][player]['FTM'] = rows[8].text
      away_box['players'][player]['FTA'] = rows[9].text
      away_box['players'][player]['OREB'] = rows[11].text
      away_box['players'][player]['DREB'] = rows[12].text
      away_box['players'][player]['REB'] = rows[13].text
      away_box['players'][player]['AST'] = rows[14].text
      away_box['players'][player]['TOV'] = rows[15].text
      away_box['players'][player]['STL'] = rows[16].text
      away_box['players'][player]['BLK'] = rows[17].text
      away_box['players'][player]['PF'] = rows[18].text
      away_box['players'][player]['PTS'] = rows[19].text
      away_box['players'][player]['PM'] = rows[20].text
    
    for player in players2:
      rows = player.find_elements_by_tag_name('td')
      player = rows[0].text
      home_box['players'][player] = {}
      home_box['players'][player]['minutes'] = rows[1].text
      home_box['players'][player]['FGM'] = rows[2].text
      home_box['players'][player]['FGA'] = rows[3].text
      home_box['players'][player]['3PM'] = rows[5].text
      home_box['players'][player]['3PA'] = rows[6].text
      home_box['players'][player]['FTM'] = rows[8].text
      home_box['players'][player]['FTA'] = rows[9].text
      home_box['players'][player]['OREB'] = rows[11].text
      home_box['players'][player]['DREB'] = rows[12].text
      home_box['players'][player]['REB'] = rows[13].text
      home_box['players'][player]['AST'] = rows[14].text
      home_box['players'][player]['TOV'] = rows[15].text
      home_box['players'][player]['STL'] = rows[16].text
      home_box['players'][player]['BLK'] = rows[17].text
      home_box['players'][player]['PF'] = rows[18].text
      home_box['players'][player]['PTS'] = rows[19].text
      home_box['players'][player]['PM'] = rows[20].text

    away_json = json.dumps(away_box)
    home_json = json.dumps(home_box)

    keys = {}
    awaykey = 'a_' + str(minutes)
    homekey = 'h_' + str(minutes)

    keys[awaykey] = away_box
    keys[homekey] = home_box

    BoxScore.objects.filter(pk=gameid).update(**keys)

    logger.info(away_json)
    logger.info(home_json)

    left += 1800
    right += 1800
    time.sleep(3)

  driver.quit()
  
@shared_task
def get_quarter_box(gameid):

  logger.info(gameid)

  options = webdriver.ChromeOptions()
  options.add_argument('--verbose')
  options.add_argument("--whitelisted-ips")
  options.add_argument("--start-maximized")                                                                                                                                

  capabilities = options.to_capabilities()

  driver = webdriver.Remote(
      command_executor='http://172.18.0.6:4444/wd/hub',
      desired_capabilities=capabilities,
  )

  left = 0
  right = 7200
  
  while right <= 28800:
    url = 'https://stats.nba.com/game/%s/?RangeType=2&StartRange=%s&EndRange=%s' %(gameid, left, right)
    driver.get(url) 
    time.sleep(8)

    tables = driver.find_elements_by_class_name('nba-stat-table__overflow')
    players1 = tables[0].find_elements_by_xpath('.//table/tbody/tr')
    players2 = tables[1].find_elements_by_xpath('.//table/tbody/tr')

    quarter = int(right/7200)

    away_box = {
      'players': {}
    }
    home_box = {
      'players': {}
    }

    for player in players1:
      rows = player.find_elements_by_tag_name('td')
      player = rows[0].text
      away_box['players'][player] = {}
      away_box['players'][player]['minutes'] = rows[1].text
      away_box['players'][player]['FGM'] = rows[2].text
      away_box['players'][player]['FGA'] = rows[3].text
      away_box['players'][player]['3PM'] = rows[5].text
      away_box['players'][player]['3PA'] = rows[6].text
      away_box['players'][player]['FTM'] = rows[8].text
      away_box['players'][player]['FTA'] = rows[9].text
      away_box['players'][player]['OREB'] = rows[11].text
      away_box['players'][player]['DREB'] = rows[12].text
      away_box['players'][player]['REB'] = rows[13].text
      away_box['players'][player]['AST'] = rows[14].text
      away_box['players'][player]['TOV'] = rows[15].text
      away_box['players'][player]['STL'] = rows[16].text
      away_box['players'][player]['BLK'] = rows[17].text
      away_box['players'][player]['PF'] = rows[18].text
      away_box['players'][player]['PTS'] = rows[19].text
      away_box['players'][player]['PM'] = rows[20].text
    
    for player in players2:
      rows = player.find_elements_by_tag_name('td')
      player = rows[0].text
      home_box['players'][player] = {}
      home_box['players'][player]['minutes'] = rows[1].text
      home_box['players'][player]['FGM'] = rows[2].text
      home_box['players'][player]['FGA'] = rows[3].text
      home_box['players'][player]['3PM'] = rows[5].text
      home_box['players'][player]['3PA'] = rows[6].text
      home_box['players'][player]['FTM'] = rows[8].text
      home_box['players'][player]['FTA'] = rows[9].text
      home_box['players'][player]['OREB'] = rows[11].text
      home_box['players'][player]['DREB'] = rows[12].text
      home_box['players'][player]['REB'] = rows[13].text
      home_box['players'][player]['AST'] = rows[14].text
      home_box['players'][player]['TOV'] = rows[15].text
      home_box['players'][player]['STL'] = rows[16].text
      home_box['players'][player]['BLK'] = rows[17].text
      home_box['players'][player]['PF'] = rows[18].text
      home_box['players'][player]['PTS'] = rows[19].text
      home_box['players'][player]['PM'] = rows[20].text

    away_json = json.dumps(away_box)
    home_json = json.dumps(home_box)

    keys = {}
    awaykey = 'a_q' + str(quarter)
    homekey = 'h_q' + str(quarter)

    keys[awaykey] = away_box
    keys[homekey] = home_box

    BoxScore.objects.filter(pk=gameid).update(**keys)

    logger.info(away_json)
    logger.info(home_json)

    left += 7200
    right += 7200
    time.sleep(3)

  driver.quit()

@shared_task
def get_game_box(gameid):

  logger.info(gameid)

  options = webdriver.ChromeOptions()
  options.add_argument('--verbose')
  options.add_argument("--whitelisted-ips")
  options.add_argument("--start-maximized")                                                                                                                                

  capabilities = options.to_capabilities()

  driver = webdriver.Remote(
      command_executor='http://172.18.0.6:4444/wd/hub',
      desired_capabilities=capabilities,
  )

  left = 0
  right = 28800
  
  url = 'https://stats.nba.com/game/%s/?RangeType=2&StartRange=%s&EndRange=%s' %(gameid, left, right)
  driver.get(url) 
  time.sleep(8)

  tables = driver.find_elements_by_class_name('nba-stat-table__overflow')
  players1 = tables[0].find_elements_by_xpath('.//table/tbody/tr')
  players2 = tables[1].find_elements_by_xpath('.//table/tbody/tr')

  away_box = {
    'players': {}
  }
  home_box = {
    'players': {}
  }

  for player in players1:
    rows = player.find_elements_by_tag_name('td')
    player = rows[0].text
    away_box['players'][player] = {}
    away_box['players'][player]['minutes'] = rows[1].text
    away_box['players'][player]['FGM'] = rows[2].text
    away_box['players'][player]['FGA'] = rows[3].text
    away_box['players'][player]['3PM'] = rows[5].text
    away_box['players'][player]['3PA'] = rows[6].text
    away_box['players'][player]['FTM'] = rows[8].text
    away_box['players'][player]['FTA'] = rows[9].text
    away_box['players'][player]['OREB'] = rows[11].text
    away_box['players'][player]['DREB'] = rows[12].text
    away_box['players'][player]['REB'] = rows[13].text
    away_box['players'][player]['AST'] = rows[14].text
    away_box['players'][player]['TOV'] = rows[15].text
    away_box['players'][player]['STL'] = rows[16].text
    away_box['players'][player]['BLK'] = rows[17].text
    away_box['players'][player]['PF'] = rows[18].text
    away_box['players'][player]['PTS'] = rows[19].text
    away_box['players'][player]['PM'] = rows[20].text
  
  for player in players2:
    rows = player.find_elements_by_tag_name('td')
    player = rows[0].text
    home_box['players'][player] = {}
    home_box['players'][player]['minutes'] = rows[1].text
    home_box['players'][player]['FGM'] = rows[2].text
    home_box['players'][player]['FGA'] = rows[3].text
    home_box['players'][player]['3PM'] = rows[5].text
    home_box['players'][player]['3PA'] = rows[6].text
    home_box['players'][player]['FTM'] = rows[8].text
    home_box['players'][player]['FTA'] = rows[9].text
    home_box['players'][player]['OREB'] = rows[11].text
    home_box['players'][player]['DREB'] = rows[12].text
    home_box['players'][player]['REB'] = rows[13].text
    home_box['players'][player]['AST'] = rows[14].text
    home_box['players'][player]['TOV'] = rows[15].text
    home_box['players'][player]['STL'] = rows[16].text
    home_box['players'][player]['BLK'] = rows[17].text
    home_box['players'][player]['PF'] = rows[18].text
    home_box['players'][player]['PTS'] = rows[19].text
    home_box['players'][player]['PM'] = rows[20].text

  away_json = json.dumps(away_box)
  home_json = json.dumps(home_box)

  keys = {}
  awaykey = 'away'
  homekey = 'home'

  keys[awaykey] = away_box
  keys[homekey] = home_box

  BoxScore.objects.filter(pk=gameid).update(**keys)

  logger.info(away_json)
  logger.info(home_json)

  time.sleep(3)

  driver.quit()

