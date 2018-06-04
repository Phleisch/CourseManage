import time
import csv
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def ScrapeRatings(driver):
    with open('info.json.cfg') as f:    											    # Get the file for saving csv data
            cred = json.load(f)
    csv_file = open(cred['filename'], 'a', newline = '')
    writer = csv.writer(csv_file)
    
    header_data = driver.find_elements_by_xpath("//*[@class='details-box']//*")
    instructor = header_data[1].text[12:]                                               # Get instructor name
    course = header_data[3].text[24:]                                                   # Get course name
    organization = header_data[5].text[14:]                                             # Get organization
    college = header_data[7].text[16:]                                                  # Etc... The substrings are
    semester = header_data[9].text[10:]                                                 # for removing title names
    num_dist = header_data[11].text[36:]
    num_ret = header_data[13].text[33:]

    prof_rate = driver.find_elements_by_xpath("//table[2]/tbody/tr[2]/td")[7].text
    course_rate = driver.find_elements_by_xpath("//table[2]/tbody/tr[3]/td")[7].text

    writer.writerow( (instructor, course, organization, college, 
    semester, num_dist, num_ret, prof_rate, course_rate) )                              # Save the data gathered as csv

    csv_file.close()
    # print('Scraping ratings...')
    # Execute code needed to get 
    driver.execute_script("window.history.go(-1)")      # Go to previous page when done getting ratings