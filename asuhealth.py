#https://www.asu.edu/healthcheck/preferences.html#
#you will need chrome web driver

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver



yourusername = "Your user name"
yourpassword = "Your password!"

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.asu.edu/healthcheck/preferences.html")
driver.find_element_by_id("username").send_keys(yourusername)
driver.find_element_by_id("password").send_keys(yourpassword)
driver.find_element_by_name("submit").click()

#avoid crashes from slow ASU website with sleep
time.sleep(5)

driver.get("https://dailycheck.m.asu.edu/symptoms-health-check")

time.sleep(4)
#driver.get("https://www.asu.edu/healthcheck/preferences.html")

#driver.find_element_by_xpath('//*@class="MuiButtonBase-root"').click()


driver.find_element_by_xpath("//span[text()='None']").click()

driver.find_element_by_xpath("//span[text()='Next']").click()

time.sleep(1)

driver.find_element_by_xpath("//span[text()='None']").click()

driver.find_element_by_xpath("//span[text()='Submit']").click()