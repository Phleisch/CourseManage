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

    # Question 1: The course was well organized
    q_1 = []
    q_1_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[2]/td")
    q_1.append(q_1_data[1].text)                                                        # Strongly disagree
    q_1.append(q_1_data[2].text)                                                        # Disagree
    q_1.append(q_1_data[3].text)                                                        # Neutral
    q_1.append(q_1_data[4].text)                                                        # Agree
    q_1.append(q_1_data[5].text)                                                        # Strongly agree
    q_1.append(q_1_data[6].text)                                                        # Num respondents
    q_1.append(q_1_data[7].text)                                                        # Avg rating
    q_1.append(q_1_data[8].text)                                                        # Organization avg
    q_1.append(q_1_data[9].text)                                                        # College avg
    q_1.append(q_1_data[10].text)                                                       # University avg

    # Question 2: The instructor communicated information effectively
    q_2 = []
    q_2_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[3]/td")
    q_2.append(q_2_data[1].text)                                                        # Strongly disagree
    q_2.append(q_2_data[2].text)                                                        # Disagree
    q_2.append(q_2_data[3].text)                                                        # Neutral
    q_2.append(q_2_data[4].text)                                                        # Agree
    q_2.append(q_2_data[5].text)                                                        # Strongly Agree
    q_2.append(q_2_data[6].text)                                                        # Num respondents
    q_2.append(q_2_data[7].text)                                                        # Avg rating
    q_2.append(q_2_data[8].text)                                                        # Organization avg
    q_2.append(q_2_data[9].text)                                                        # College avg
    q_2.append(q_2_data[10].text)                                                       # University avg

    # Question 3: The instructor showed interest in the progress of students.
    q_3 = []
    q_3_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[4]/td")
    q_3.append(q_3_data[1].text)                                                        # Strongly disagree
    q_3.append(q_3_data[2].text)                                                        # Disagree
    q_3.append(q_3_data[3].text)                                                        # Neutral
    q_3.append(q_3_data[4].text)                                                        # Agree
    q_3.append(q_3_data[5].text)                                                        # Strongly Agree
    q_3.append(q_3_data[6].text)                                                        # Num respondents
    q_3.append(q_3_data[7].text)                                                        # Avg rating
    q_3.append(q_3_data[8].text)                                                        # Organization avg
    q_3.append(q_3_data[9].text)                                                        # College avg
    q_3.append(q_3_data[10].text)                                                       # University avg

    # Question 4: The tests/assignments were usually graded and returned promptly.
    q_4 = []
    q_4_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[5]/td")
    q_4.append(q_4_data[1].text)                                                        # Strongly disagree
    q_4.append(q_4_data[2].text)                                                        # Disagree
    q_4.append(q_4_data[3].text)                                                        # Neutral
    q_4.append(q_4_data[4].text)                                                        # Agree
    q_4.append(q_4_data[5].text)                                                        # Strongly Agree
    q_4.append(q_4_data[6].text)                                                        # Num respondents
    q_4.append(q_4_data[7].text)                                                        # Avg rating
    q_4.append(q_4_data[8].text)                                                        # Organization avg
    q_4.append(q_4_data[9].text)                                                        # College avg
    q_4.append(q_4_data[10].text)                                                       # University avg

    # Question 5: The instructor made me feel free to ask questions, disagree, and express my ideas.
    q_5 = []
    q_5_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[6]/td")
    q_5.append(q_5_data[1].text)                                                        # Strongly disagree
    q_5.append(q_5_data[2].text)                                                        # Disagree
    q_5.append(q_5_data[3].text)                                                        # Neutral
    q_5.append(q_5_data[4].text)                                                        # Agree
    q_5.append(q_5_data[5].text)                                                        # Strongly Agree
    q_5.append(q_5_data[6].text)                                                        # Num respondents
    q_5.append(q_5_data[7].text)                                                        # Avg rating
    q_5.append(q_5_data[8].text)                                                        # Organization avg
    q_5.append(q_5_data[9].text)                                                        # College avg
    q_5.append(q_5_data[10].text)                                                       # University avg

    # Question 6: At this point in time, I feel that this course will be (or has already been) of value to me.
    q_6 = []
    q_6_data = driver.find_elements_by_xpath("//table[1]/tbody/tr[7]/td")
    q_6.append(q_6_data[1].text)                                                        # Strongly disagree
    q_6.append(q_6_data[2].text)                                                        # Disagree
    q_6.append(q_6_data[3].text)                                                        # Neutral
    q_6.append(q_6_data[4].text)                                                        # Agree
    q_6.append(q_6_data[5].text)                                                        # Strongly Agree
    q_6.append(q_6_data[6].text)                                                        # Num respondents
    q_6.append(q_6_data[7].text)                                                        # Avg rating
    q_6.append(q_6_data[8].text)                                                        # Organization avg
    q_6.append(q_6_data[9].text)                                                        # College avg
    q_6.append(q_6_data[10].text)                                                       # University avg

    # Question 7: Overall, this instructor was...
    q_7 = []
    q_7_data = driver.find_elements_by_xpath("//table[2]/tbody/tr[2]/td")
    q_7.append(q_7_data[1].text)                                                        # Strongly disagree
    q_7.append(q_7_data[2].text)                                                        # Disagree
    q_7.append(q_7_data[3].text)                                                        # Neutral
    q_7.append(q_7_data[4].text)                                                        # Agree
    q_7.append(q_7_data[5].text)                                                        # Strongly Agree
    q_7.append(q_7_data[6].text)                                                        # Num respondents
    q_7.append(q_7_data[7].text)                                                        # Avg rating
    q_7.append(q_7_data[8].text)                                                        # Organization avg
    q_7.append(q_7_data[9].text)                                                        # College avg
    q_7.append(q_7_data[10].text)                                                       # University avg

    # Question 8: Overall, this course was...
    q_8 = []
    q_8_data = driver.find_elements_by_xpath("//table[2]/tbody/tr[3]/td")
    q_8.append(q_8_data[1].text)                                                        # Strongly disagree
    q_8.append(q_8_data[2].text)                                                        # Disagree
    q_8.append(q_8_data[3].text)                                                        # Neutral
    q_8.append(q_8_data[4].text)                                                        # Agree
    q_8.append(q_8_data[5].text)                                                        # Strongly Agree
    q_8.append(q_8_data[6].text)                                                        # Num respondents
    q_8.append(q_8_data[7].text)                                                        # Avg rating
    q_8.append(q_8_data[8].text)                                                        # Organization avg
    q_8.append(q_8_data[9].text)                                                        # College avg
    q_8.append(q_8_data[10].text)                                                       # University avg

    # Question 9: In my opinion, the workload in this course was...
    q_9 = []
    q_9_data = driver.find_elements_by_xpath("//table[3]/tbody/tr[2]/td")
    q_9.append(q_9_data[1].text)                                                        # Strongly disagree
    q_9.append(q_9_data[2].text)                                                        # Disagree
    q_9.append(q_9_data[3].text)                                                        # Neutral
    q_9.append(q_9_data[4].text)                                                        # Agree
    q_9.append(q_9_data[5].text)                                                        # Strongly Agree
    q_9.append(q_9_data[6].text)                                                        # Num respondents
    q_9.append(q_9_data[7].text)                                                        # Avg rating
    q_9.append(q_9_data[8].text)                                                        # Organization avg
    q_9.append(q_9_data[9].text)                                                        # College avg
    q_9.append(q_9_data[10].text)                                                       # University avg

#     prof_rate = driver.find_elements_by_xpath("//table[2]/tbody/tr[2]/td")[7].text
#     course_rate = driver.find_elements_by_xpath("//table[2]/tbody/tr[3]/td")[7].text

#     writer.writerow( (instructor, course, organization, college, 
#     semester, num_dist, num_ret, prof_rate, course_rate) )                              # Save the data gathered as csv
#     writer.writerow( (s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5], s_d[6], prof_rate, course_rate) )
    writer.writerow( (s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5], s_d[6],
                      q_1[0], q_1[1], q_1[2], q_1[3], q_1[4], q_1[5], q_1[6], q_1[7], q_1[8], q_1[9],
                      q_2[0], q_2[1], q_2[2], q_2[3], q_2[4], q_2[5], q_2[6], q_2[7], q_2[8], q_2[9],
                      q_3[0], q_3[1], q_3[2], q_3[3], q_3[4], q_3[5], q_3[6], q_3[7], q_3[8], q_3[9],
                      q_4[0], q_4[1], q_4[2], q_4[3], q_4[4], q_4[5], q_4[6], q_4[7], q_4[8], q_4[9],
                      q_5[0], q_5[1], q_5[2], q_5[3], q_5[4], q_5[5], q_5[6], q_5[7], q_5[8], q_5[9],
                      q_6[0], q_6[1], q_6[2], q_6[3], q_6[4], q_6[5], q_6[6], q_6[7], q_6[8], q_6[9],
                      q_7[0], q_7[1], q_7[2], q_7[3], q_7[4], q_7[5], q_7[6], q_7[7], q_7[8], q_7[9],
                      q_8[0], q_8[1], q_8[2], q_8[3], q_8[4], q_8[5], q_8[6], q_8[7], q_8[8], q_8[9],
                      q_9[0], q_9[1], q_9[2], q_9[3], q_9[4], q_9[5], q_9[6], q_9[7], q_9[8], q_9[9]) )
    csv_file.close()
    # print('Scraping ratings...')
    # Execute code needed to get
    time.sleep(2)
    driver.execute_script("window.history.go(-1)")      # Go to previous page when done getting ratings