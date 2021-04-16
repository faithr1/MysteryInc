import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass

    def test_site(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        time.sleep(1)  # Wait 2 secs

        #enter signup page
        self.selenium.find_element_by_id('signupButton').click() #test signup button
        time.sleep(1)  # Wait 2 secs

        #login to home
        id_input = self.selenium.find_element_by_id('id_username') #set id_input var
        pass1_input = self.selenium.find_element_by_id('id_password1') #set pass1_input var
        pass2_input = self.selenium.find_element_by_id('id_password2') #set pass2_input var
        id_input.clear()
        id_input.send_keys('johnDoe1')
        pass1_input.send_keys('flowerCats')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('submitButton').click() #click sign up
        time.sleep(1)  # Wait 2 secs
        
        #move to storyboard page
        self.selenium.find_element_by_id('continueButton').click() #continue to create page
        time.sleep(1) #wait 2 secs

        #write values into Title and Synopsis
        pass1_input = self.selenium.find_element_by_id('title')
        pass2_input = self.selenium.find_element_by_id('synopsis')
        pass1_input.send_keys('Test Title1')
        pass2_input.send_keys('Im going to press refresh before save and show that the values wont save')
        time.sleep(4)
        self.selenium.find_element_by_id('refresh').click()
        time.sleep(2)


        pass1_input = self.selenium.find_element_by_id('title')
        pass2_input = self.selenium.find_element_by_id('synopsis')
        pass1_input.send_keys('Test Title2')
        pass2_input.send_keys('Now Im going to hit save then refresh and show that the values save')
        time.sleep(4)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('refresh').click()
        time.sleep(2)


        pass1_input = self.selenium.find_element_by_id('title')
        pass2_input = self.selenium.find_element_by_id('synopsis')
        pass1_input.clear()
        pass2_input.clear()
        pass1_input.send_keys('Test Title3')
        pass2_input.send_keys('Now Im going to hit save then return home to show continuing the story will allow '
                              'the values to remain')
        time.sleep(4)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('returnHomeButton').click()
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('continueButton').click()
        time.sleep(2)

        pass1_input = self.selenium.find_element_by_id('title')
        pass2_input = self.selenium.find_element_by_id('synopsis')
        pass1_input.clear()
        pass2_input.clear()
        pass1_input.send_keys('Test Title4')
        pass2_input.send_keys('Now Im going to hit save then return home to show starting a new story will erase '
                              'the current values')
        time.sleep(4)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('returnHomeButton').click()
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('newStoryButton').click()


        pass1_input = self.selenium.find_element_by_id('title')
        pass2_input = self.selenium.find_element_by_id('synopsis')
        pass1_input.clear()
        pass2_input.clear()
        time.sleep(1)
        pass1_input.send_keys('Test Title5')
        pass2_input.send_keys('Now Im going to hit save, logout, then log back in and show the values remain')
        time.sleep(4)
        self.selenium.find_element_by_id('save').click()
        self.selenium.find_element_by_id('returnHomeButton').click()
        self.selenium.switch_to.alert.accept()
        time.sleep(1)
        self.selenium.find_element_by_id('logoutButton').click()
        time.sleep(1)
        pass1_input = self.selenium.find_element_by_id('id_username')
        pass2_input = self.selenium.find_element_by_id('id_password')
        pass1_input.send_keys('johnDoe1')
        pass2_input.send_keys('flowerCats')
        self.selenium.find_element_by_id('loginButton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('continueButton').click()
        time.sleep(4)





