import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RatingScraper import ScrapeRatings

def CrawlSurveys(driver, department):
    department_finished = False
    while department_finished is False:
        for table_index in range(1,11):
            table = driver.find_element_by_xpath('//table/tbody')                               # Element holding list of surveys
            survey = table.find_elements_by_tag_name('tr')[table_index]                         
            survey_text = survey.text.split(' ')
            if " " in department:
                survey_department = (survey_text[len(survey_text) - 5]) + " " + survey_text[len(survey_text) - 4][:1]
            else: 
                survey_department = (survey_text[len(survey_text) - 4])[:3]                     # Get department name
            if survey_department != department:
                department_finished = True
                break
            survey_link = survey.find_elements_by_tag_name('td')[0]                             # Element containing link
            time.sleep(2)
            survey_link.find_elements_by_tag_name('a')[0].click()                               # Click actual link
            ScrapeRatings(driver)
        if department_finished is False:
            next_page = driver.find_element_by_xpath("//*[@class='page-forward']//*//*[8]")     # Get next page button by xpath
            time.sleep(2)
            next_page.send_keys(Keys.ENTER)                                                     # Go to the next page of surveys