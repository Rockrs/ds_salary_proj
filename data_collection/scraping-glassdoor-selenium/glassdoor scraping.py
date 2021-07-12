'''
author : Omer Sakarya
url : https://github.com/arapfaik/scraping-glassdoor-selenium
'''

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_jobs():
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    # Initializing the webdriver''
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        executable_path="C:/Users/shrma/Documents/ds_salary_proj/data_collection/scraping-glassdoor-selenium/chromedriver", options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.co.in/Job/gurgaon-data-scientist-jobs-SRCH_IL.0,7_IC2921225_KO8,22.htm'
    driver.get(url)
    df = []

    for i in range(1, 4, 1):
        driver.find_elements_by_xpath('//div[@class="middle"]//a')[i].click()
        time.sleep(3)
        job_buttons = driver.find_elements_by_xpath(
            '//li[contains(@class, "react-job-listing")]')
        for index, job in enumerate(job_buttons):
            job.click()
            time.sleep(5)
            if len(df) == 0:
                driver.find_element_by_class_name("modal_closeIcon").click()
            try:
                job_res = {}
                job_info_parentel = driver.find_element_by_xpath(
                    '//div[contains(@class, "css-w04er4")]')
                job_info = job_info_parentel.find_elements_by_xpath(
                    './/div')

                company_info_parentel = driver.find_element_by_xpath(
                    '//div[@id="EmpBasicInfo"]')
                company_info = company_info_parentel.find_elements_by_xpath(
                    './/span')

                for index, el in enumerate(job_info):
                    if index == 0:
                        job_res['Company'] = el.get_attribute("innerHTML").split('<')[0]
                        try:
                            job_res['Rating'] = el.find_element_by_xpath('.//span').text
                        except Exception as e:
                            pass
                    if index ==1:
                        job_res['Position'] = el.text
                    try:
                        if index ==3:
                            job_res['Salary'] = el.find_elements_by_xpath('.//span')[0].text
                    except Exception as e:
                        pass

                for i in range(0, len(company_info), 2):
                    key = company_info[i].text
                    val = company_info[i+1].text
                    
                    job_res[key] = val
                df.append(job_res)
            except Exception as e:
                pass
    return pd.DataFrame(df)
    
df = get_jobs()
print (df)
df.to_pickle('gurgaon_data')