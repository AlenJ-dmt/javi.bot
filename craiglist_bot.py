from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

tire_size=['35x135022', '2853522', '3153022', '2057016', '2255018', '2057014', '2756518', '2255017',
           '2457517', '2357515', '3153522', '1855516', '2457017', '1858013', '2453520', '3255022', '2255517',
           '2455016', '2055017', '2456517', '2154517', '2657017', '2756020']
tire_picture[]
city = "hou"

# create a new Firefox session
driver = webdriver.Chrome()

driver.maximize_window()

# Navigate to the application home page
driver.get("https://accounts.craigslist.org/login")


# get the search textbox
user = driver.find_element_by_id("inputEmailHandle")
user.send_keys('socialmedia@mywheelrepair.com')
# send password
password =driver.find_element_by_id("inputPassword")
password.send_keys('Wheelntire1')

login_button = driver.find_element_by_id("login")
login_button.click()

time.sleep(5)

#This is the beginning o the loop




#select The city
select_city = driver.find_element_by_xpath("/html/body/article/section/form[2]/select")
select = Select(select_city)
select.select_by_value(city)

driver.find_element_by_xpath("//button[@type='submit' and @value='go']").click()

time.sleep(5)

driver.find_element_by_xpath("/html/body/article/section/form/ul/li[6]/label/span[2]").click()

driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[6]/div/span').click()

time.sleep(5)

#Post Title
title = driver.find_element_by_id("PostingTitle")
title.send_keys("Set of used Tires For Sale")

time.sleep(3)

#Post Zip code
zip_code = driver.find_element_by_id("postal_code")
zip_code.send_keys("77057")

time.sleep(3)

#Post Body
posting_body = driver.find_element_by_id("PostingBody")
posting_body.send_keys("We got A set of used tires for Sale")

time.sleep(3)

#continue to Adress page
continue_button = driver.find_element_by_xpath("//*[@id='new-edit']/div/div[3]/div/button")
continue_button.click()

time.sleep(2)

#continue to Pictures page
continue_button_two = driver.find_element_by_xpath("//*[@id='leafletForm']/button")
continue_button_two.click()
'''
upload_pics = driver.find_element_by_xpath("//*[@id='plupload']")
upload_pics.click()
'''
time.sleep(5)

#Select pictures and upload
file_link = (r"C:\Users\Rollo's\Desktop\inventory\pictures\5658\IMG_2888.jpg")
file_upload = driver.find_element_by_tag_name('input')
file_upload.send_keys(file_link)


time.sleep(3)

#continue to final draft
done_with_img_button = driver.find_element_by_xpath("/html/body/article/section/form/button")
done_with_img_button.click()

time.sleep(4)

#publish Add

publish_button = driver.find_element_by_xpath("//*[@id='publish_top']/button")
publish_button.click()

time.sleep(5)
#Go back to account page
return_to_account = driver.find_element_by_xpath("//*[@id='new-edit']/div/div/ul/li[3]/a")
return_to_account.click()


