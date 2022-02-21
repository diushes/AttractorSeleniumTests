from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests


class TestTheInternetPage:
    def __init__(self, browser):
        self.url = "http://the-internet.herokuapp.com"
        self.browser = browser

    #Function that tests authentification, password and username are arguments passed by user
    def testLogin(self, username, password):
        self.browser.get(self.url)
        tap_loginlink = self.browser.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a').click()
        type_username = self.browser.find_element_by_name('username').send_keys(username)
        type_password = self.browser.find_element_by_name('password').send_keys(password)
        press_loginbtn = self.browser.find_element_by_class_name('radius').click()

    #Function that tests dropdown, no arguments need to be passed
    def testDropdown(self):
        self.browser.get(self.url)
        tap_dropdownlink = self.browser.find_element_by_xpath('//*[@id="content"]/ul/li[11]/a').click()
        dropdown = Select(self.browser.find_element_by_id("dropdown"))
        dropdown.select_by_visible_text("Option 1")
    
    #Function that tests Key presses, keys argument is passed by user
    def testKeyPress(self, keys):
        self.browser.get(self.url)
        tap_keypresslink = self.browser.find_element_by_xpath('//*[@id="content"]/ul/li[31]/a').click()
        type_input = self.browser.find_element_by_id('target').send_keys(keys)

    #Function that tests File download, additionaly checks presense of passed word argument
    def testFileDowload(self, word):
        self.browser.get(self.url)
        tap_filedownlink = self.browser.find_element_by_xpath('//*[@id="content"]/ul/li[17]/a').click()
        file_link = self.browser.find_element_by_xpath('//*[@id="content"]/div/a[1]').get_attribute('href')
        r = requests.get(file_link, allow_redirects=True)
        #saving file to a specified location
        open('Documents/somerandom.txt', 'wb').write(r.content)
        #checking whether word exists in file 
        if word in r.content.decode():
            print("The file contains requested word - " + word)

            
       
#Uncomment to start testing
'''
#Setting up the browser
browser = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver')
TestPage = TestTheInternetPage(browser=browser)

#Running 1st test
TestPage.testLogin(username="tomsmith", password="SuperSecretPassword!")

#Running 2nd test
TestPage.testDropdown()

#Running 3rd test
TestPage.testKeyPress(keys="x")

#Running 4th test
TestPage.testFileDowload("Helvetica")

'''


        