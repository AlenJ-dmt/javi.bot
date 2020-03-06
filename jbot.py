from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
import os

tire_size = ['2365', '4589', '4669', '5658', '58911', '59202', '59807', '59856', '71781A',
             '72246A', '72317', '73742', '74217', '77245', '85100', '86044', '86290']

'''
'37x135022', '2853522', '3153022', '2057016', '2255018', '2057014', '2756518', '2255017',
             '2457517', '2357515', '3153522', '1855516', '2457017', '1858013', '2453520', '3255022', '2255517',
             '2455016', '2055017', '2456517', '2154517', '2657017', '2756020'
'''

brands =['Dodge', 'Cadillac', 'cadillac', 'GMC', 'Audi', 'BMW', 'Jaguar', 'Jaguar', 'Acura',
         'Land Rover', 'Land Rover', 'Infiniti', 'Lexus', 'Land Rover', 'MBZ', 'BMW', 'BMW']   

'''
'Toyo', 'Atturo', 'Continental', 'Continental', 'Pirelli', 'Wind Force',
         'BF Goodrich', 'Pirelli', 'Michelin', 'Radial', 'Pirelli', 'Federal',
         'Michelin', 'Michelin', 'Nexen', 'BF Goodrich', 'Nitto', 'Road Huger',
         'Kumho', 'Goodyear', 'Federal', 'Firestone', 'Firestone', 'BF Goodrich'
'''
number_of_postings = 16


city = ["hou", 'ama', 'aus', 'bpt', 'bro', 'cst', 'crp', 'dal', 'etx', 'elp', 'gls', 'grk', 'lrd', 'lbb', 'mca', 'sat', 'tsu', 'wtx', 'vtx', 'wco', 'wtf']

# create a new Firefox session
driver = webdriver.Chrome()

driver.maximize_window()

# Navigate to the application home page
driver.get("https://accounts.craigslist.org/login")


# get the search textbox
user = driver.find_element_by_id("inputEmailHandle")
user.send_keys('socialmedia@mywheelrepair.com')
# send password
password = driver.find_element_by_id("inputPassword")
password.send_keys('Wheelntire1')

login_button = driver.find_element_by_id("login")
login_button.click()

time.sleep(10)

# This is the beginning o the loop

for ciudad in city:

    # select The city
    select_city = driver.find_element_by_xpath(
        "/html/body/article/section/form[2]/select")
    select = Select(select_city)
    select.select_by_value(ciudad)

    driver.find_element_by_xpath(
        "//button[@type='submit' and @value='go']").click()

    time.sleep(10)

    driver.find_element_by_xpath(
        "/html/body/article/section/form/ul/li[6]/label/span[2]").click()
    time.sleep(10)

    driver.find_element_by_xpath(
        '//*[@id="new-edit"]/div/label/label[6]/div/span').click()

    time.sleep(10)

    # Post Title
    title = driver.find_element_by_id("PostingTitle")
    title.send_keys('Set of OEM 21" Porsche Cayenne Sport Wheels For Sale')

    time.sleep(10)

    # Post Zip code
    zip_code = driver.find_element_by_id("postal_code")
    zip_code.send_keys("77057")

    time.sleep(10)

    # Post Body
    posting_body = driver.find_element_by_id("PostingBody")
    posting_body.send_keys("Set of OEM 21 Porsche Cayenne Sport Wheels For Sale for Sale\nUsed OEM Wheels \nMany Sizes in Stock\nSets of 4\nRunflat Tires\nAll Terrain / Mud Terrain\nHigh thread and low tread tires\nInventory Constantly Changing\nFor more information call (713) 780-8083\nAsk for Sales (Sabino, Lalo, Anthony)\nHablamos Espanol")


    time.sleep(15)

    # continue to Adress page
    continue_button = driver.find_element_by_xpath(
        "//*[@id='new-edit']/div/div[3]/div/button")
    continue_button.click()

    time.sleep(10)

    # continue to Pictures page
    continue_button_two = driver.find_element_by_xpath(
        "//*[@id='leafletForm']/button")
    continue_button_two.click()
    '''
    upload_pics = driver.find_element_by_xpath("//*[@id='plupload']")
    upload_pics.click()
    '''
    time.sleep(10)

    # Select pictures and upload


    file_upload = driver.find_element_by_tag_name('input')

    file_upload.send_keys(r"C:\Users\Rollo's\Desktop\inventory\tires_pictures\p.jpg")


    time.sleep(15)

    # continue to final draft
    done_with_img_button = driver.find_element_by_xpath(
        "/html/body/article/section/form/button")
    done_with_img_button.click()

    time.sleep(15)

    # publish Add

    publish_button = driver.find_element_by_xpath("//*[@id='publish_top']/button")
    publish_button.click()

    time.sleep(30)
    # Go back to account page
    return_to_account = driver.find_element_by_xpath(
        "//*[@id='new-edit']/div/div/ul/li[3]/a")
    return_to_account.click()

    number_of_postings = number_of_postings - 1
    time.sleep(300)
    
