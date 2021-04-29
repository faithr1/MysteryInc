import time
from selenium import webdriver

#This example requires Selenium WebDriver 3.13 or newer
self.selenium = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')
self.selenium.get('http://127.0.0.1:8000/new_story/')
time.sleep(2)  # Wait 2 secs

#test help button
self.selenium.find_element_by_id('help').click() #create pop-up box
self.selenium.find_element_by_id('help').click()
time.sleep(2) #wait 2 secs
self.assertEqual('.bg-modal'.style.display, 'flex')

#close the pop-up box
self.selenium.find_element_by_class_name('close').click()
time.sleep(2) #wait 2 seconds
self.assertEqual('.bg-modal'.style.display, 'none')

#checking if the function returned true after opening and closing pop up box
self.assertTrue(need_help(), 0)