import requests
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process

options = Options() 
#options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

url = 'https://steamcommunity.com/id/radars/badges/?sort=a'
url2 = 'https://steamcommunity.com/id/m0nsterOG/badges/'

# url3 = 'http://localhost:3001/'

# data = []
# driver = webdriver.Chrome(chrome_options=options)
# driver.get(url3)

# score1 = driver.find_element_by_class_name('score1')
# score2 = driver.find_element_by_class_name('score2')

# while(True):
#   print(score1.text)
#   print(score2.text)
#   time.sleep(2)

url3 = 'http://localhost:3001/'
url4 = 'http://localhost:3002/'

def proc1():
  data = []
  driver = webdriver.Chrome(chrome_options=options)
  driver.get(url3)

  score1 = driver.find_element_by_class_name('score1')
  score2 = driver.find_element_by_class_name('score2')

  while(True):
    print(score1.text)
    print(score2.text)
    time.sleep(2)

def proc2():
  data = []
  driver = webdriver.Chrome(chrome_options=options)
  driver.get(url4)
  element = None
  score1 = driver.find_element_by_class_name('li')

  while(True):
    try:
      element = score1.find_element_by_xpath('//li[1]')
    except:
      print('error')
    if(element):
      print(element.text)
    time.sleep(2)

if __name__ == '__main__':
  # p1 = Process(target=proc1)
  # p1.start()
  p2 = Process(target=proc2)
  p2.start()
  # p1.join()
  p2.join()

# current_page = 1
# while True:
#   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#   time.sleep(0.1)
#   page_content = BeautifulSoup(driver.page_source, 'html.parser')
#   badges = page_content.findAll('div', {'class': ['badge_row', 'is_link']})
#   for badge in badges:
#     data.append(badge)

#   try:
#     element = driver.find_element_by_link_text('>')
#   except:
#     break
#   is_disabled = 'disabled' in element.get_attribute("class")
#   if(is_disabled):
#     break
#   element.click()

# for badge in data:
#   description = badge.find('div',attrs={"class": "badge_info_description"})
#   sub_title = description.find('div', attrs={"class": "badge_info_title"}).text.strip()
  
#   level_xp = description.find('div',{"class": None}).text.strip()
#   level_xp_join = " ".join(level_xp.split()).split(',')
#   unlocked = description.find('div', attrs={"class": "badge_info_unlocked"}).text.strip()

#   anchor = badge.find('a',attrs={"class":"badge_row_overlay"})
#   link = anchor.get('href')

#   new_link = re.sub('https:\/\/steamcommunity.com\/id\/[a-zA-Z0-9]*\/', '', link).split('/')
#   title = badge.find('div',attrs={"class":"badge_title"}).text.strip()
#   title_text = " ".join(title.split())
#   title_text = title_text.replace('View details', '')

#   src = badge.find('img')
#   img = src.get('src')
#   print(img)
#   print(new_link)
#   print(title_text)
#   print(sub_title)
#   print(level_xp_join)
#   print(unlocked)

#driver.quit()