import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SurveyCrawler import CrawlSurveys

def CrawlDepartments(driver, start_dept, start_class):
    course_search = driver.find_element_by_link_text("Search by Course")		#Easier than 'Search by Instructor'
    course_search.click()

    drop_down = driver.find_element_by_id('s_in_search_course_dept')			#Element that is drop down of departments
    num_options = len(drop_down.find_elements_by_tag_name('option'))            #Number of departments to choose from
    found_start = False
    needs_backspace = False

    for option_index in range(num_options):
        drop_down = driver.find_element_by_id('s_in_search_course_dept')        #Get drop down element to renew after page refresh
        search_box = driver.find_element_by_id('s_in_search_course_num')        #Use element to refresh instead of 'Search' button
        option = drop_down.find_elements_by_tag_name('option')[option_index]    #Get the 'option_index'-th department
        department = (option.text[:4])[1:]                                      #Unique three letter department identifier
        sys.stdout.write("\rCurrent department: " + department)
        sys.stdout.flush()
        if found_start is False and (department == start_dept or start_dept == 'None'):
            found_start = True
            needs_backspace = True
        if found_start is True:
            option.click()
            if department == start_dept and start_class != 'None':
                search_box.send_keys(start_class)
            elif needs_backspace:
                needs_backspace = False
                for x in range(len(start_class)):
                    search_box.send_keys(Keys.BACK_SPACE)
            search_box.send_keys(Keys.ENTER)                                    #Refresh page after department selection
            CrawlSurveys(driver, department)