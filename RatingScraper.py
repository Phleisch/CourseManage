import csv
import json
from selenium import webdriver

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
    tables = driver.find_elements_by_xpath("//table")

    for table in tables:
        num_elems = len(table.find_elements_by_xpath("tbody/tr"))
        for row_index in range(2,num_elems+1):
            xpath = "tbody/tr[{}]/td".format(row_index)
            curr_row = table.find_elements_by_xpath(xpath)
            for elem_index in range(1,11):
                data.append(curr_row[elem_index].text)

    writer.writerow(data)
    csv_file.close()
    driver.execute_script("window.history.go(-1)")