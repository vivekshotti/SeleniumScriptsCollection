import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')
driver.get("https://youtube.com/")

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Samay Raina')

driver.implicitly_wait(10)

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

first_click = driver.find_element_by_class_name("style-scope ytd-channel-renderer")
first_click.click()

second_click = driver.find_element_by_link_text('Popular uploads')
second_click.click()

element = driver.find_element_by_id("subscriber-count").text
print("Total Subscribers as of today: ", element)



