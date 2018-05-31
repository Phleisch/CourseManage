import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from CrawlDepartments import CrawlDepartments

def Main():
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
    CrawlDepartments(driver)
    print('Application Run Successfully')

Main()