import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')
driver.get("https://www.nba.com/bulls/custom-jersey")

driver.implicitly_wait(10)

searchButton = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
searchButton.click()

first_click = driver.find_element_by_id("lastName")
first_click.send_keys("Jordan")
# In this above send keys section, you can replace the exisiting name with the name that you want to display on your jersey

driver.implicitly_wait(10)

second_click = driver.find_element_by_name("jerseyNumber")
second_click.send_keys("23")
# In this above send keys section, you can replace the existing jersey number with your desired one which you want to display on your jersey

third_click = driver.find_element_by_id("customize")
third_click.click()

driver.implicitly_wait(20)

fourth_click = driver.find_element_by_xpath("//input[@value='DOWNLOAD JERSEY']")
fourth_click.click()




