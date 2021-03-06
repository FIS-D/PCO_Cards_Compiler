from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import math, pyautogui as pgui,time,csv

#setting up selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

ignoredExceptions = (NoSuchElementException,StaleElementReferenceException)


print('Getting link using firefox...')

browser = webdriver.Firefox()

browser.get('https://sainsburysowe.pcomanagedservice.com:9443/WebEngine/')

input('Navigate to starting ticket then press Enter.')

test1 = False
while test1 == False:
    try:

        dataTable = WebDriverWait(browser,10,ignored_exceptions=ignoredExceptions)\
            .until(expected_conditions.presence_of_element_located((By.ID,'datagrid')))
        
        navLabel = browser.find_element_by_class_name('navigatorLabel')
        nextButton = browser.find_element_by_class_name('next')
        print('Successfully located %s element, beginning scrape.'%(dataTable.tag_name))
        test1 = True

    except:

        print('This starting point is not valid, log in and go to the starting date in PCO')
        input('Press Enter to continue...')

table = browser.find_elements_by_xpath("//table[@id='datagrid']")
body = dataTable.find_elements_by_xpath(".//tbody")

headings = ['Application Ref.No','House Number','Postcode','Forename','Surname','Date of Birth',
            'Last Processed Date','Queue','Reason Code','Decision','','']
        
with open('out.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    
    
    while nextButton.tag_name == 'a':  
        
        # dataTable = browser.find_element_by_id('datagrid')
        dataTable = WebDriverWait(browser,10,ignored_exceptions=ignoredExceptions)\
            .until(expected_conditions.presence_of_element_located((By.ID,'datagrid')))
        body = dataTable.find_elements_by_xpath(".//tbody")
        
        i = 0
        for row in dataTable.find_elements_by_xpath(".//tr"):
            i = i + 1
            if (i > 2):
                line = [td.text for td in row.find_elements_by_xpath(".//div[1]")]
                print(line)
                csvHappy = ['="' + value + '"' for value in line]
                writer.writerow(csvHappy)
                
        nextButton.click()
        sleep(1.5)
        nextButton = browser.find_element_by_class_name('next')
               
        dataTable = browser.find_element_by_id('datagrid')
        dataTable = WebDriverWait(browser,10,ignored_exceptions=ignoredExceptions)\
            .until(expected_conditions.presence_of_element_located((By.ID,'datagrid')))
        body = dataTable.find_elements_by_xpath(".//tbody")

    time.sleep(0.5)
    
    # dataTable = browser.find_element_by_id('datagrid')
    dataTable = WebDriverWait(browser,10,ignored_exceptions=ignoredExceptions)\
        .until(expected_conditions.presence_of_element_located((By.ID,'datagrid')))
    body = dataTable.find_elements_by_xpath(".//tbody")

    i = 0
    for row in dataTable.find_elements_by_xpath(".//tr"):
        i = i + 1
        if (i > 2):
            line = [td.text for td in row.find_elements_by_xpath(".//div[1]")]
            print(line)
            csvHappy = ['="' + value + '"' for value in line]
            writer.writerow(csvHappy)
                        
test2 = True
print('Output completed successfully!')
input('Press any key to continue...')

browser.close()
        
def tearDown(self):
    self.driver.quit()
