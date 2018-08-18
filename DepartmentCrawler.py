import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SurveyCrawler import crawl_surveys

def crawl_departments(driver, start_dept, start_class, start_year, start_sem):
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
        department = department.strip()

        if found_start is False and (department == start_dept or start_dept is None):
            found_start = True
        
        if found_start is True:
            option.click()
            
            if department == start_dept and start_class is not None:
                search_box.send_keys(start_class)
                needs_backspace
            elif needs_backspace:
                needs_backspace = False
                
                for x in range(len(start_class)):
                    search_box.send_keys(Keys.BACK_SPACE)
            
            time.sleep(1)
            search_box.send_keys(Keys.ENTER)                                    #Refresh page after department selection
            crawl_surveys(driver, department, start_year, start_sem)