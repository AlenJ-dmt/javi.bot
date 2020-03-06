import pyautogui
import time
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


done_size =[0] * 20
done_brands = [0] * 20

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

number_of_postings = 15



#Select Active Window

pyautogui.moveTo(100, 420)
pyautogui.click()
time.sleep(3)

#maximize window

pyautogui.moveTo(460, 10)
pyautogui.click()
time.sleep(15)

while number_of_postings > 0:

    #+Sell Something

    pyautogui.moveTo(200, 365)
    pyautogui.click()
    time.sleep(15)

    #Pick Category

    pyautogui.moveTo(550, 380)
    pyautogui.click()
    time.sleep(7)

    #Cat

    pyautogui.moveTo(500, 320)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('Auto')
    time.sleep(3)
    pyautogui.moveTo(500, 365)
    pyautogui.click()

    #Title

    pyautogui.moveTo(500, 365)
    pyautogui.click()
    time.sleep(15)
    pyautogui.write('Set Of Used OEM ' + tire_size[number_of_postings] + ' ' + brands[number_of_postings] +' Insurance Quality for Sale')
    time.sleep(10)

    #price
    pyautogui.moveTo(470, 415)
    pyautogui.click()
    time.sleep(10)
    pyautogui.write('1')
    time.sleep(10)

    #picture

    pyautogui.moveTo(470, 600)
    time.sleep(7)
    pyautogui.click()
    time.sleep(9)
    pyautogui.moveTo(300, 465)
    pyautogui.click()
    time.sleep(5)
    di = (r"C:\Users\Rollo's\Desktop\inventory\tires_pictures")
    foto = (tire_size[number_of_postings]+".jpg")
    file_link = os.path.join(di, foto)
    pyautogui.write(file_link)
    time.sleep(7)
    pyautogui.moveTo(520, 495)
    pyautogui.click()
    time.sleep(7)

    #Donnashhh

    pyautogui.moveTo(900, 715)
    time.sleep(6)
    pyautogui.click()
    time.sleep(8)

    #Now Done For Real

    pyautogui.moveTo(880, 690)
    time.sleep(8)
    pyautogui.click()
    time.sleep(5)
    number_of_postings = number_of_postings - 1

    time.sleep(100)

    




