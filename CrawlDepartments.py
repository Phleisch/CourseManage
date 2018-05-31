import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from CrawlSurveys import CrawlSurveys

def CrawlDepartments(driver):
    course_search = driver.find_element_by_link_text("Search by Course")		#Easier than 'Search by Instructor'
    course_search.click()

    drop_down = driver.find_element_by_id('s_in_search_course_dept')			#Element that is drop down of departments
    num_options = len(drop_down.find_elements_by_tag_name('option'))            #Number of departments to choose from

    for option_index in range(num_options):
        drop_down = driver.find_element_by_id('s_in_search_course_dept')        #Get drop down element to renew after page refresh
        search_box = driver.find_element_by_id('s_in_search_course_num')        #Use element to refresh instead of 'Search' button
        option = drop_down.find_elements_by_tag_name('option')[option_index]    #Get the 'option_index'-th department
        # print((option.text[:4])[1:])                                          #Unique three letter department identifier
        option.click()
        search_box.send_keys(Keys.ENTER)                                        #Refresh page after department selection
        CrawlSurveys(driver)