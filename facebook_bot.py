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
driver.get("https://www.facebook.com/")


# get the search textbox
user = driver.find_element_by_id("email")
user.send_keys('socialmedia@mywheelrepair.com')

password =driver.find_element_by_id("pass")
password.send_keys('Hubcap1')

login_button = driver.find_element_by_id("loginbutton")
login_button.click()

driver.get("https://www.facebook.com/marketplace/selling")

time.sleep(10)


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

#Click on Sell Something BTN

pyautogui.moveTo(100, 420) # Move the mouse to XY coordinates.
pyautogui.click()


#click on type of listing

pyautogui.moveTo(500, 700)
pyautogui.click()

'''
#Select 'Auto Part'

pyautogui.moveTo(500, 320)
pyautogui.click()
pyautogui.write('Auto')
time.sleep(2)
pyautogui.moveTo(500, 340)
time.sleep(1)
pyautogui.click()
'''
