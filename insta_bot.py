from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
import pyautogui



category = "Auto Parts"

# create a new Chrome session
driver = webdriver.Chrome()

driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")

pyautogui.moveTo(1340, 90)
pyautogui.click()


#set Email or account
email_set = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
email_set.send_keys('rollossolutions')

#Set Password
password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
password.send_keys('hubcap1')

#login

login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

#Find Account to follow

find_account = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
find_account.send_keys('account')
find_account.send_keys(Keys.DOWN)
find_account.send_keys(Keys.ENTER)

#Followers

account_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
account_followers.click()

