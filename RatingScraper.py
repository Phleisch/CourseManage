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
    with open('info.json.cfg') as f:    											    # Get the file for saving csv data
            cred = json.load(f)
    csv_file = open(cred['filename'], 'a', newline = '')
    writer = csv.writer(csv_file)
    
    # Data collection section

    data = _get_header(driver, major_abbr, course_num)

    # Question 1: The course was well organized
    q_1_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[2]/td")
    data.append(q_1_data[1].text)                                                        # Strongly disagree
    data.append(q_1_data[2].text)                                                        # Disagree
    data.append(q_1_data[3].text)                                                        # Neutral
    data.append(q_1_data[4].text)                                                        # Agree
    data.append(q_1_data[5].text)                                                        # Strongly agree
    data.append(q_1_data[6].text)                                                        # Num respondents
    data.append(q_1_data[7].text)                                                        # Avg rating
    data.append(q_1_data[8].text)                                                        # Organization avg
    data.append(q_1_data[9].text)                                                        # College avg
    data.append(q_1_data[10].text)                                                       # University avg

    # Question 2: The instructor communicated information effectively
    q_2_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[3]/td")
    data.append(q_2_data[1].text)                                                        # Strongly disagree
    data.append(q_2_data[2].text)                                                        # Disagree
    data.append(q_2_data[3].text)                                                        # Neutral
    data.append(q_2_data[4].text)                                                        # Agree
    data.append(q_2_data[5].text)                                                        # Strongly Agree
    data.append(q_2_data[6].text)                                                        # Num respondents
    data.append(q_2_data[7].text)                                                        # Avg rating
    data.append(q_2_data[8].text)                                                        # Organization avg
    data.append(q_2_data[9].text)                                                        # College avg
    data.append(q_2_data[10].text)                                                       # University avg

    # Question 3: The instructor showed interest in the progress of students.
    q_3_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[4]/td")
    data.append(q_3_data[1].text)                                                        # Strongly disagree
    data.append(q_3_data[2].text)                                                        # Disagree
    data.append(q_3_data[3].text)                                                        # Neutral
    data.append(q_3_data[4].text)                                                        # Agree
    data.append(q_3_data[5].text)                                                        # Strongly Agree
    data.append(q_3_data[6].text)                                                        # Num respondents
    data.append(q_3_data[7].text)                                                        # Avg rating
    data.append(q_3_data[8].text)                                                        # Organization avg
    data.append(q_3_data[9].text)                                                        # College avg
    data.append(q_3_data[10].text)                                                       # University avg

    # Question 4: The tests/assignments were usually graded and returned promptly.
    q_4_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[5]/td")
    index = 5
    if "tests" in q_4_data[0].text:
        data.append(q_4_data[1].text)                                                        # Strongly disagree
        data.append(q_4_data[2].text)                                                        # Disagree
        data.append(q_4_data[3].text)                                                        # Neutral
        data.append(q_4_data[4].text)                                                        # Agree
        data.append(q_4_data[5].text)                                                        # Strongly Agree
        data.append(q_4_data[6].text)                                                        # Num respondents
        data.append(q_4_data[7].text)                                                        # Avg rating
        data.append(q_4_data[8].text)                                                        # Organization avg
        data.append(q_4_data[9].text)                                                        # College avg
        data.append(q_4_data[10].text)                                                       # University avg
        index+=1
    else:
        data.append("N/A")                                                        # Strongly disagree
        data.append("N/A")                                                        # Disagree
        data.append("N/A")                                                        # Neutral
        data.append("N/A")                                                        # Agree
        data.append("N/A")                                                        # Strongly Agree
        data.append("N/A")                                                        # Num respondents
        data.append("N/A")                                                        # Avg rating
        data.append("N/A")                                                        # Organization avg
        data.append("N/A")                                                        # College avg
        data.append("N/A")                                                       # University avg

    # Question 5: The instructor made me feel free to ask questions, disagree, and express my ideas.
    q_5_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[{}]/td".format(index))
    data.append(q_5_data[1].text)                                                        # Strongly disagree
    data.append(q_5_data[2].text)                                                        # Disagree
    data.append(q_5_data[3].text)                                                        # Neutral
    data.append(q_5_data[4].text)                                                        # Agree
    data.append(q_5_data[5].text)                                                        # Strongly Agree
    data.append(q_5_data[6].text)                                                        # Num respondents
    data.append(q_5_data[7].text)                                                        # Avg rating
    data.append(q_5_data[8].text)                                                        # Organization avg
    data.append(q_5_data[9].text)                                                        # College avg
    data.append(q_5_data[10].text)                                                       # University avg
    index+=1

    # Question 6: At this point in time, I feel that this course will be (or has already been) of value to me.
    q_6_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[{}]/td".format(index))
    data.append(q_6_data[1].text)                                                        # Strongly disagree
    data.append(q_6_data[2].text)                                                        # Disagree
    data.append(q_6_data[3].text)                                                        # Neutral
    data.append(q_6_data[4].text)                                                        # Agree
    data.append(q_6_data[5].text)                                                        # Strongly Agree
    data.append(q_6_data[6].text)                                                        # Num respondents
    data.append(q_6_data[7].text)                                                        # Avg rating
    data.append(q_6_data[8].text)                                                        # Organization avg
    data.append(q_6_data[9].text)                                                        # College avg
    data.append(q_6_data[10].text)                                                       # University avg

    # Question 7: Overall, this instructor was...
    q_7_data = driver.find_elements_by_xpath("//table[2]/tbody/tr[2]/td")
    data.append(q_7_data[1].text)                                                        # Strongly disagree
    data.append(q_7_data[2].text)                                                        # Disagree
    data.append(q_7_data[3].text)                                                        # Neutral
    data.append(q_7_data[4].text)                                                        # Agree
    data.append(q_7_data[5].text)                                                        # Strongly Agree
    data.append(q_7_data[6].text)                                                        # Num respondents
    data.append(q_7_data[7].text)                                                        # Avg rating
    data.append(q_7_data[8].text)                                                        # Organization avg
    data.append(q_7_data[9].text)                                                        # College avg
    data.append(q_7_data[10].text)                                                       # University avg

    # Question 8: Overall, this course was...
    q_8_data = driver.find_elements_by_xpath("//table[2]/tbody/tr[3]/td")
    data.append(q_8_data[1].text)                                                        # Strongly disagree
    data.append(q_8_data[2].text)                                                        # Disagree
    data.append(q_8_data[3].text)                                                        # Neutral
    data.append(q_8_data[4].text)                                                        # Agree
    data.append(q_8_data[5].text)                                                        # Strongly Agree
    data.append(q_8_data[6].text)                                                        # Num respondents
    data.append(q_8_data[7].text)                                                        # Avg rating
    data.append(q_8_data[8].text)                                                        # Organization avg
    data.append(q_8_data[9].text)                                                        # College avg
    data.append(q_8_data[10].text)                                                       # University avg

    # Question 9: In my opinion, the workload in this course was...
    q_9_data = driver.find_elements_by_xpath("//table[3]/tbody/tr[2]/td")
    data.append(q_9_data[1].text)                                                        # Strongly disagree
    data.append(q_9_data[2].text)                                                        # Disagree
    data.append(q_9_data[3].text)                                                        # Neutral
    data.append(q_9_data[4].text)                                                        # Agree
    data.append(q_9_data[5].text)                                                        # Strongly Agree
    data.append(q_9_data[6].text)                                                        # Num respondents
    data.append(q_9_data[7].text)                                                        # Avg rating
    data.append(q_9_data[8].text)                                                        # Organization avg
    data.append(q_9_data[9].text)                                                        # College avg
    data.append(q_9_data[10].text)                                                       # University avg

    writer.writerow(data)
    csv_file.close()
    driver.execute_script("window.history.go(-1)")      # Go to previous page when done getting ratings