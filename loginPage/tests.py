import time
from selenium import webdriver

#This example requires Selenium WebDriver 3.13 or newer
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')
driver.get('http://127.0.0.1:8000/new_story/')
time.sleep(2)  # Wait 2 secs

#test help button
driver.find_element_by_id('help').click() #create pop-up box (currently fails)
time.sleep(2) #wait 2 secs