import time
import json
import csv
import sys
import argparse
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DepartmentCrawler import crawl_departments

SEMESTER_MAPPER = {"Spring": 1, "Summer": 2, "Fall": 3, "spring": 1, "summer": 2, "fall": 3}

def Main(start_dept, start_class, start_year, start_sem):
    
    with open('info.json.cfg') as f:
        cred = json.load(f)

    driver = webdriver.Chrome('/Program Files/chromedriver/chromedriver.exe')   #Path to ChromeDriver
    driver.get('https://utdirect.utexas.edu/ctl/ecis/results/search.WBX')	    #Website to scrape
    driver.maximize_window()

    user_field = driver.find_element_by_id("IDToken1")				            #Find username field
    pass_field = driver.find_element_by_id("IDToken2")				            #Find password field
    user_field.send_keys(cred["username"])					                    #Enter username
    pass_field.send_keys(cred["password"])					                    #Enter password
    pass_field.send_keys(Keys.ENTER)						                    #Equivalent to clicking 'log in'
    driver.implicitly_wait(3600)						                        #Wait for next page to load
    crawl_departments(driver, start_dept, start_class, start_year, start_sem)

    print('Application Run Successfully')

parser = argparse.ArgumentParser(description='Crawl the surveys of the UT CIS website.')
parser.add_argument('-m', '--major', help='major to start crawling')
parser.add_argument('-c', '--course', help='course to start crawling')
parser.add_argument('-y', '--year', default=0, help='earliest year to include surveys from')
parser.add_argument('-s', '--semester', help='earliest semester to include surveys from')
args = parser.parse_args()
args.semester = SEMESTER_MAPPER.get(args.semester, 0)

Main(args.major, args.course, args.year, args.semester)