import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('/Program Files/chromedriver/chromedriver.exe')	#Path to ChromeDriver
driver.get('https://utdirect.utexas.edu/ctl/ecis/results/search.WBX')		#Website to scrape

with open("cred.json.cfg") as f:											#Load credentials from-
        cred = json.load(f)													#Json file

user_field = driver.find_element_by_id("IDToken1")							#Find username field
pass_field = driver.find_element_by_id("IDToken2")							#Find password field
user_field.send_keys(cred["username"])										#Enter username
pass_field.send_keys(cred["password"])										#Enter password
pass_field.send_keys(Keys.ENTER)											#Equivalent to clicking 'log in'
driver.implicitly_wait(1)													#Wait for next page to load

course_search = driver.find_element_by_link_text("Search by Course")		#Easier than 'Search by Instructor'
course_search.click()
#search_btn = driver.find_elements_by_xpath("//input[@value='Search']")[1]

drop_down = driver.find_element_by_id('s_in_search_course_dept')			#Element that is drop down of departments
for option in drop_down.find_elements_by_tag_name('option'):				#Go through each element and look at each course
    option.click()
    search_btn.click()
    print('Searched')