import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Program Files/chromedriver/chromedriver.exe')	#Path to ChromeDriver
driver.get('https://utdirect.utexas.edu/ctl/ecis/results/search.WBX')		#Website to scrape
driver.maximize_window()

with open("cred.json.cfg") as f:											#Load credentials from-
        cred = json.load(f)													#Json file

user_field = driver.find_element_by_id("IDToken1")							#Find username field
pass_field = driver.find_element_by_id("IDToken2")							#Find password field
user_field.send_keys(cred["username"])										#Enter username
pass_field.send_keys(cred["password"])										#Enter password
pass_field.send_keys(Keys.ENTER)											#Equivalent to clicking 'log in'
driver.implicitly_wait(3600)												#Wait for next page to load

course_search = driver.find_element_by_link_text("Search by Course")		#Easier than 'Search by Instructor'
course_search.click()

drop_down = driver.find_element_by_id('s_in_search_course_dept')			#Element that is drop down of departments
num_options = len(drop_down.find_elements_by_tag_name('option'))            #Number of departments to choose from

for option_index in range(num_options):
    drop_down = driver.find_element_by_id('s_in_search_course_dept')        #Get drop down element to renew after page refresh
    search_box = driver.find_element_by_id('s_in_search_course_num')        #Use element to refresh instead of 'Search' button
    option = drop_down.find_elements_by_tag_name('option')[option_index]    #Get the 'option_index'-th department
    # print((option.text[:4])[1:])                                          #Unique three letter department identifier
    option.click()
    search_box.send_keys(Keys.ENTER)                                        #Refresh page after department selection