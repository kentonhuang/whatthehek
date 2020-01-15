import time

from celery import shared_task
from celery.utils.log import get_task_logger

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



logger = get_task_logger(__name__)

@shared_task
def test_task():
  logger.info('test task ran')

@shared_task
def sel_test():

  options = webdriver.ChromeOptions()
  options.add_argument('--verbose')
  options.add_argument("--whitelisted-ips")
  options.add_argument("--start-maximized")                                                                                                                                

  capabilities = options.to_capabilities()

  driver = webdriver.Remote(
      command_executor='http://172.17.0.1:4444/wd/hub',
      desired_capabilities=capabilities,
  )
  # driver.get('http://f3c24081.ngrok.io/')

  # score1 = driver.find_element_by_class_name('score1')
  # score2 = driver.find_element_by_class_name('score2')

  # i = 0;

  # while i < 5:
  #   logger.info(score1.text)
  #   logger.info(score2.text)
  #   i += 1
  #   time.sleep(2)
  score1 = [];
  driver.get('https://stats.nba.com/game/0021900002/?StartRange=7200&EndRange=9000&RangeType=2')
  #driver.get('https://google.com')
  time.sleep(5)

  el = driver.find_element_by_tag_name('body')
  source = el.get_attribute("outerHTML");
  # score1 = driver.find_element_by_class_name('nba-stat-table')
  logger.info(source)
  #score2 = driver.find_element_by_class_name('score2')

  # i = 0;

  # while i < 5:
  #   logger.info(score1.text)
  #   logger.info(score2.text)
  #   i += 1
  #   time.sleep(2)

  driver.quit()
  





