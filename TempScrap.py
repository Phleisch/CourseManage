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
    
    # Data collection section

    # Survey Details
    s_d = []
    s_d_data = driver.find_elements_by_xpath("//*[@class='details-box']//*")
    s_d.append(s_d_data[1].text[12:])                                                # Instructor name
    s_d.append(s_d_data[3].text[24:])                                                # Course name
    s_d.append(s_d_data[5].text[14:])                                                # Organization
    s_d.append(s_d_data[7].text[16:])                                                # College
    s_d.append(s_d_data[9].text[10:])                                                # Semester
    s_d.append(s_d_data[11].text[36:])                                               # Num distributed surveys
    s_d.append(s_d_data[13].text[33:])                                               # Num returned surveys

def _get_header(driver, major_abbr, course_num):
    header_data = driver.find_elements_by_xpath("//*[@class='details-box']//*")
    name            = str(header_data[1].text).split(": ")[1]
    
    course          = str(header_data[3].text).split(": ")[1]
    major_abbr      = major_abbr
    course_num      = course_num
    unique_num      = course.split("(")[1][:5]

    major           = str(header_data[5].text).split(": ")[1]
    college         = str(header_data[7].text).split(": ")[1]

    occurrence      = str(header_data[9].text).split(": ")[1].split(" ")
    semester        = occurrence[0]
    year            = occurrence[1]


    num_distributed = str(header_data[11].text).split(": ")[1]
    num_returned    = str(header_data[13].text).split(": ")[1]