import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RatingScraper import scrape_ratings

SEMESTER_MAPPER = {"Spring": 1, "Summer": 2, "Fall": 3, "spring": 1, "summer": 2, "fall": 3}

def crawl_surveys(driver, department, start_year, start_sem):
    department_finished = False
    while department_finished is False:
        for table_index in range(1,11):
            surveys = driver.find_elements_by_xpath('//table/tbody/tr')               # Element holding list of survey links
            curr_survey = surveys[table_index]

            if curr_survey is None:
                print("Out of surveys")
                return

            survey_elements = curr_survey.find_elements_by_tag_name('td')
            survey_class = survey_elements[1].text
            survey_time = survey_elements[3].text.split(" ")
            survey_time[0] = SEMESTER_MAPPER.get(survey_time[0], 0)
            survey_time[1] = int(survey_time[1])
            
            survey_department  = _get_department(survey_class)
            class_name = survey_class.strip(survey_department).strip()
            print(survey_department)
            print(class_name)

            if survey_time[1] < int(start_year):
                continue
            if survey_time[0] < start_sem and survey_time[1] == int(start_year):
                continue

            if survey_department != department:
                department_finished = True
                break

            sys.stdout.write("\r                                                            ")
            sys.stdout.flush()
            sys.stdout.write("\rCurrent course: " + department + ", " + class_name)
            sys.stdout.flush()
            survey_link = survey_elements[0]             # Element containing link
            time.sleep(1)
            survey_link.find_elements_by_tag_name('a')[0].click()               # Click actual link
            scrape_ratings(driver, department, class_name)

        if department_finished is False:
            next_page = driver.find_element_by_xpath("//*[@class='page-forward']//*//*[8]")     # Get next page button by xpath
            time.sleep(1)
            next_page.send_keys(Keys.ENTER)                                                     # Go to the next page of surveys

def _get_department(class_name):
    department = ''

    for letter in class_name:
        if not letter.isdigit():
            department += letter
        else:
            break
    
    department = department.strip()
    return department