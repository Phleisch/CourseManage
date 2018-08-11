import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RatingScraper import scrape_ratings

def crawl_surveys(driver, department, start_year, start_sem):
    department_finished = False
    while department_finished is False:
        for table_index in range(1,11):
            table = driver.find_element_by_xpath('//table/tbody')                               # Element holding list of surveys
            survey = table.find_elements_by_tag_name('tr')[table_index]                         
            survey_text = survey.text.split(' ')

            if " " in department:
                survey_department = (survey_text[len(survey_text) - 5]) + " " + survey_text[len(survey_text) - 4][:1]
                class_name = survey_text[len(survey_text) - 4][1:]
            elif len(department) is 2 or len(department) is 1:
                survey_department = (survey_text[len(survey_text) - 5])
                class_name = survey_text[len(survey_text) - 4]
            else:
                survey_department = (survey_text[len(survey_text) - 4])[:3]                     # Get department name
                class_name = survey_text[len(survey_text) - 4][3:]

            if survey_department != department:
                department_finished = True
                break

            sys.stdout.write("\r                                                            ")
            sys.stdout.flush()
            sys.stdout.write("\rCurrent course: " + department + ", " + class_name)
            sys.stdout.flush()
            survey_link = survey.find_elements_by_tag_name('td')[0]                             # Element containing link
            time.sleep(2)
            survey_link.find_elements_by_tag_name('a')[0].click()                               # Click actual link
            scrape_ratings(driver)

        if department_finished is False:
            next_page = driver.find_element_by_xpath("//*[@class='page-forward']//*//*[8]")     # Get next page button by xpath
            time.sleep(2)
            next_page.send_keys(Keys.ENTER)                                                     # Go to the next page of surveys