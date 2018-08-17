import time
import csv
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def _get_header(driver, major_abbr, course_num):
    header_data = list()
    header = driver.find_elements_by_xpath("//*[@class='details-box']//*")
    
    #Professor's name
    header_data.append(str(header[1].text).split(": ")[1])
    
    course = str(header[3].text).split(": ")[1]
    header_data.extend([major_abbr, course_num])

    #Unique number
    header_data.append(course.split("(")[1][:5])

    #Major
    header_data.append(str(header[5].text).split(": ")[1])
    
    #College
    header_data.append(str(header[7].text).split(": ")[1])

    occurrence = str(header[9].text).split(": ")[1].split(" ")
    #Semester
    header_data.append(occurrence[0])
    
    #Year
    header_data.append(occurrence[1])

    #Number of surveys distributed
    header_data.append(str(header[11].text).split(": ")[1])
    
    #Number of surveys returned
    header_data.append(str(header[13].text).split(": ")[1])
    
    return header_data

def scrape_ratings(driver, major_abbr, course_num):
    with open('info.json.cfg') as f:
            cred = json.load(f)
    csv_file = open(cred['filename'], 'a', newline = '')
    writer = csv.writer(csv_file)
    
    # Data collection section
    data = _get_header(driver, major_abbr, course_num)
    print()

    columns = list()
    
    for table_index in range(1,4):
        driver.refresh()
        row_index = 2
        xpath = str.format("//table[{}]/tbody/tr[{}]/td", table_index, row_index)
        curr_data = driver.find_elements_by_xpath(xpath)
        while len(curr_data) is not 0:
            columns.append(curr_data)
            row_index += 1
            xpath = str.format("//table[{}]/tbody/tr[{}]/td", table_index, row_index)
            print(xpath)
            curr_data = driver.find_elements_by_xpath(xpath)

    print("That worked")
    sys.exit()

    table_index = 1
    while table_index < 4:
        row_index = 2
        xpath = str.format("//table[{}]/tbody/tr[{}]/td", table_index, row_index)
        
        try:
            curr_data = driver.find_elements_by_xpath(xpath)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            sys.exit()

        print("Here 4")
        while len(curr_data) is not 0:
            for elem_index in range(1,11):
                data.append(curr_data[elem_index].text)
            row_index += 1
            xpath = str.format("//table[{}]/tbody/tr[{}]/td", table_index, row_index)
            print(xpath)
            curr_data = driver.find_elements_by_xpath(xpath)
        table_index += 1

    writer.writerow(data)
    csv_file.close()
    driver.execute_script("window.history.go(-1)")