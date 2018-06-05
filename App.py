import time
import json
import csv
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DepartmentCrawler import CrawlDepartments

def Main():
    start_dept = input("Department to start with, or 'None': ")
    start_class = input("Class to start with, or 'None': ")
    with open('info.json.cfg') as f:						#Load data from-
            cred = json.load(f)                                                 #Json file
    # csv_file = open(cred['filename'], 'wt', newline = '')
    # writer = csv.writer(csv_file)
    # writer.writerow( ('Instructor', 'Course', 'Organization', 
    #                 'College', 'Semester', '# Distributed', '# Returned',
    #                 'Professor Rating', 'Course Rating') )
    # csv_file.close()
    driver = webdriver.Chrome('/Program Files/chromedriver/chromedriver.exe')	#Path to ChromeDriver
    driver.get('https://utdirect.utexas.edu/ctl/ecis/results/search.WBX')	#Website to scrape
    driver.maximize_window()

    user_field = driver.find_element_by_id("IDToken1")				#Find username field
    pass_field = driver.find_element_by_id("IDToken2")				#Find password field
    user_field.send_keys(cred["username"])					#Enter username
    pass_field.send_keys(cred["password"])					#Enter password
    pass_field.send_keys(Keys.ENTER)						#Equivalent to clicking 'log in'
    driver.implicitly_wait(3600)						#Wait for next page to load
    CrawlDepartments(driver, start_dept, start_class)
    print('Application Run Successfully')

Main()