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
  driver = webdriver.Remote(
      command_executor='http://172.17.0.1:4444/wd/hub',
      desired_capabilities=DesiredCapabilities.CHROME,
  )
  driver.get('http://f3c24081.ngrok.io/')

  score1 = driver.find_element_by_class_name('score1')
  score2 = driver.find_element_by_class_name('score2')

  i = 0;

  while i < 5:
    logger.info(score1.text)
    logger.info(score2.text)
    i += 1
    time.sleep(2)

  driver.quit()
  





