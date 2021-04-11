import time
from selenium import webdriver

#This example requires Selenium WebDriver 3.13 or newer
self.selenium = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')
self.selenium.get('http://127.0.0.1:8000/new_story/')
time.sleep(2)  # Wait 2 secs

#test help button
self.selenium.find_element_by_id('help').click() #create pop-up box (currently fails)
time.sleep(2) #wait 2 secs