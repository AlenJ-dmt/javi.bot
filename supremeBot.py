import pyautogui
import time
import os

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

tires_15_inch = ['1456515', '1556015', '1656015', '1656515', '1755515', '1756515', '1855515', '1856015', '1856515', 'LT1957515', '1954515', '1955015', '1955515', '1956015', '1956515', '1957015', '1957515', 'LT2057015', 'LT2057515', '2055015', '2055515', '2056015', '2056515', '2057015', '2057515', 'LT2157515', 'LT2158015', '2155015', '2155515', '2156015', '2156515', '2157015', '2157515', '2257515', 'LT2257515', '2254515', '2255015', '2255515', '2256015', '2256515', '2257015', '2356015', '2356515', '2357015', '2357515', 'LT2357015', 'LT2357515', '30X9.5015', '33X9.5015', '2455015', '2456015', '2457015', 'LT2456515', 'LT2457015', 'LT2457515', '2556015', '2556515', '2557015', '2557515', 'LT2557015', 'LT2557515', '2655015', '2657015', '2657515', 'LT2657515', 'LT2657015', '31X10.5015', '33X10.5015', '2755015', '2756015', 'LT2857015', '2857015', '32X11.5015', '2955015', 'LT3157015', '33X12.5015', '35X12.5015', 'LT3256015', '3255015', '3256015', '33X13.5015', '35X13.5015', '3453515', '35X14.5015', '37X14.5015', '36X15.5015', '38X15.5015']

tires_16_inch = ['1755516', '1756016', '1856016', '1855016', '1855516', '1954516', '1955016', '1955516', '1956016', '1957516', '2054016', '2054516', '2055016', '2055516', '2056016', '2056516', '2057016', '2154016', '2154516', '2155016', '2155516', '2156016', '2156516', '2157016', '2157516', '2158516', 'LT2156516', 'LT2157016', 'LT2158516', '2254016', '2254516', '2255016', '2255516', '2256016', '2256516', 'LT2257016', '2257016', 'LT2257516', '2257516', '2356516', '2357016', '2357516', 'LT2357016', '2355016', 'LT2358516', '2355516', '2356016', 'LT2457516', '2454516', '2455016', '2455516', '2457016', '2457516', 'LT2457016', 'LT2557016', 'LT2558516', '2555016', '2555516', '2556516', '2557016', 'LT2657016', 'LT2657516', '2654516', '2655016', '2657016', '2657516', 'LT2757016', '2755016', '2756016', '2756516', '2757016', 'LT2856016', 'LT2857016', 'LT2857516', '2856016', '2856516', '33X11.5016', 'LT2957516', '2955016', 'LT3057016', 'LT3157016', 'LT3157516', 'LT3157516', '35X12.5016', 'LT3258016', 'LT3557016', 'LT3656516', 'LT3657016', '33X14.5016', '35X14.5016', '38X14.5016', 'LT3755516', 'LT3756516', 'LT3857016', 'LT3957016']

tires_17_inch = ['1954017', '1954517', '2055017', '2055517', '2054017', '2054517', '2153517', '2154017', '2154517', '2155017', '2155517', '2156017', '2156517', '2157017', '2253517', '2254017', '2254517', '2255017', '2255517', '2256017', '2256517', '2257517', '2354017', '2354517', '2355017', '2355517', '2356017', '2356517', '2357017', '2357517', '2358017', '2358017', '2457517', '2457017', '2457517', '2453517', '2454017', '2454517', '2455017', '2456517', '2455517', '2457017', '2456517', '2557517', '2558017', '2554017', '2554517', '2555017', '2555517', '2556017', '2556517', '2557017', '2557517', '2656517', '2657017', '2657517', '2654017', '2655517', '2656017', '2656517', '2657017', '2756517', '2757017', '2754017', '2755017', '2755517', '2756017', '2756517', '2757017', '2857017', '2857517', '2854017', '2856017', '2856517', '2857017', '2957017', '3056517', '3057017', '3056017', '3157017', '3153517', '33X125017', '35X125017', '37X125017', '3257017', '3353517', '37X135017', '38X135017', '40X135017', '3455517', '3557017', '38X145017', '40X145017']

tires_18_inch = ['2054018', '2154018', '2154518', '2155018', '2155518', '2153518', '2253518', '2254018', '2254518', '2255018', '2255518', '2256018', '2353518', '2354018', '2354518', '2355018', '2355518', '2356018', '2356518', '2457018', '2453518', '2454018', '2454518', '2455018', '2455518', '2456018', '2553518', '2554018', '2554518', '2555018', '2555518', '2556018', '2556518', '2557018', '2653518', '2654018', '2654518', '2656018', '2656518', '2656518', '2657018', '2657018', '2653018', '2756518', '2753518', '2757018', '2754018', '2754518', '2755518', '2756018', '2756518', '2757018', '2856518', '2857018', '2857518', '2853018', '2853518', '2854018', '2854518', '2855018', '2855518', '2856018', '2856518', '2857018', '2956518', '2957018', '2953018', '2953518', '2954018', '2954518', '3056018', '3056518', '3057018', '3053518', '3054518', '3055518', '3153018', '3156018', '33X12.5018', '35X12.5018', '37X12.5018', '3256018', '3256518', '3256518', '3353018', '37X13.5018', '38X13.5018', '3453018', '3453518', '3556518', '3756018', '38X15.5018', '3956518']

tires_19_inch = ['2153519', '2253519', '2254019', '2254519', '2255519', '2353519', '2354019', '2354519', '2355019', '2355519', '2356519', '2453519', '2454019', '2454519', '2455019', '2455519', '2553019', '2553519', '2554019', '2554519', '2555019', '2555519', '2556019', '2653019', '2653519', '2654019', '2655019', '2655519', '2753019', '2753519', '2754019', '2754519', '2755019', '2755519', '2853019', '2853519', '2854019', '2854519', '2855519', '2856019', '2952519', '2953019', '2953519', '3052519', '3053019', '3053519', '3154019', '3152519', '3153019', '3253019', '3453019', '3453519', '3552519', '3553019']

tires_20_inch = ['2154520', '2253020', '2253520', '2353020', '2353520', '2354520', '2355520', '2453020', '2453520', '2454020', '2454520', '2455020', '2456020', '2553020', '2553520', '2554020', '2554520', '2555020', '2555520', '2653020', '2653520', '2654020', '2654520', '2655020', '2656020', 'LT2656020', 'LT2756020', 'LT2756520', '2752520', '2753020', '2753520', '2754020', '2754520', '2755020', '2755520', '2756020', '2756520', '2853020', '2853520', 'LT2855520', '2854020', 'LT2856020', '2854520', 'LT2856520', '2855020', '2855520', '2856020', '2852520', '2952520', '2953020', '2953520', '2954020', '2954520', '2955020', '2955520', '2956020', '2956520', 'LT3055520', 'LT3056020', '3052520', '3053020', '3053520', '3054020', '3054520', '3055020', '3055520', 'LT3156020', '3153020', '3153520', '33X12.5020', '35X12.5020', '37X12.5020', 'LT3255020', 'LT3256020', '3252520', '3253020', '3253520', '3352520', '3353020', '35X13.5020', '37X13.5020', '38X13.5020', '3452520', 'LT3556020', '42X14.5020', '36X15.5020', '38X15.5020']

tires_22_inch = ['2353022', '2453022', '2553022', '2553522', '2554022', '2554522', '2653022', '2653522', '2654022', '2654522', '3352522', '2753022', '2753522', '2754022', '2754522', '2755022', 'LT2855022', 'LT2855522', '2852522', '2853022', '2853522', '2854022', '2854522', '2855022', '2953522', '2952522', '2953022', '2954522', '3054522', '3052522', '3053022', '3053522', '3054022', '3152522', '3153022', '3153522', '33X12.5022', '35X12.5022', '37X12.5022', '3253522', '3254022', 'LT3255022', 'LT3255522', 'LT3256022', 'LT3355522', '37X13.5022', '40X15.5022']

tires_24_inch = ['2553024', '2752524', '2753024', '2853024', '2853524', '2854024', '2953024', '2953524', '2954024', '3053524', '3054024', '3153024', '3153524', 'LT3155024', '3254524', 'LT3254524', 'LT3255024', '38X13.5024', '37X13.5024', '3853524', '4052524']

tires = [ tires_16_inch, tires_17_inch, tires_18_inch, tires_19_inch, tires_20_inch, tires_24_inch]

brands = ['Haida', 'BFGoodrich', 'Bridgestone', 'Continental', 'Cooper', 'Dunlop', 'Falken', 'Firestone', 'General', 'Goodyear', 'Hankook', 'Kumho', 'Michelin', 'Nexen', 'Pirelli', 'Sumitomo', 'Toyo', 'Uniroyal', 'Yokohama']

already_posted = [['Haida', '35x12.5020'], ['Toyo', '2857017'], '37x135022', '2853522', '2255018', '2057014', '2756518', '2255017', '2457517', '2357515', '3153522', '1855516', '2457017', '1858013', '2453520', '3255022', '2255517', '2455016', '2055017', '2456517', '2154517', '2657017', '2254518', '2455019', '2355520', '2554020', '2555520', '2654020', '2754020', '2755020', '2755520', '2854520', '3153520']

#Encuentra una llanta si esta disponible (has not been posted)

def find_available_size(tire_array, marcas):

    for marca in marcas:

        tag = []
        
        current_dir = marca
        default_dir = (r"C:\Users\Rollo's\Desktop\inventory\tires")
        main_dir = os.path.join(default_dir, current_dir)
        
        

        for tire_size in tire_array:
        
            for tire in tire_size:

                foto = (tire + '.jpg')
                existe = os.path.join(main_dir, foto)
                if os.path.exists(existe):

                    tag.append(current_dir)
                    tag.append(tire)
                    
                    if tag not in already_posted:
                        
                        already_posted.append(tag)
                        return tag
                
#Open Navigator
def open_navigator():
    pyautogui.moveTo(600, 750)
    pyautogui.click()
    time.sleep(3)

#click on search box
def go_to_page(webpage):
    pyautogui.moveTo(300,50)
    pyautogui.click()
    time.sleep(2)
    if 'https://' in webpage:
        pyautogui.write(webpage)
    else:
        pyautogui.write('https://' + webpage)
    time.sleep(2)
    pyautogui.press('enter')

def open_second_window():
    pyautogui.moveTo(270, 10)
    pyautogui.click()
    time.sleep(5)
    
def go_to_facebook():
    go_to_page('facebook.com/marketplace/selling')
    time.sleep(5)

def go_to_main():
    pyautogui.moveTo(130, 10)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

def go_to_craigslist():
    go_to_page('https://accounts.craigslist.org/login/home')
    time.sleep(5)

def print_done_listings(done):
    go_to_page('https://docs.google.com/spreadsheets/d/1QKRqlr2BRwKhwad-sA9ST8PY4-gkKHRjsCLD6GN_UBI/edit#gid=0')
    time.sleep(3)
    pyautogui.moveTo(90, 230)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(done)
    time.sleep(3)


    
def post_on_facebook(tire):
    #+Sell Something

    pyautogui.moveTo(200, 365)
    pyautogui.click()
    time.sleep(5)

    #Pick Category

    pyautogui.moveTo(550, 380)
    pyautogui.click()
    time.sleep(3)

    #Cat

    pyautogui.moveTo(500, 320)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('Auto')
    time.sleep(2)
    pyautogui.moveTo(500, 365)
    pyautogui.click()

    #Title

    pyautogui.moveTo(500, 365)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write('Set Of (2) ' + tire[1] + " " + tire[0] +' Used Tires for Sales')
    time.sleep(5)

    #price
    pyautogui.moveTo(470, 415)
    pyautogui.click()
    time.sleep(5)
    pyautogui.write('1')
    time.sleep(3)

    #picture

    pyautogui.moveTo(470, 600)
    time.sleep(4)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(300, 465)
    pyautogui.click()
    time.sleep(5)
    di = (r"C:\Users\Rollo's\Desktop\inventory\tires")
    marca = tire[0]
    foto = (tire[1]+".jpg")
    file_link = os.path.join(di, marca, foto)
    pyautogui.write(file_link)
    time.sleep(7)
    pyautogui.moveTo(520, 495)
    pyautogui.click()
    time.sleep(3)

    #Donnashhh

    pyautogui.moveTo(900, 715)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)

    #Now Done For Real

    pyautogui.moveTo(880, 690)
    time.sleep(3)
    pyautogui.click()
    time.sleep(60)

def post_on_craigslist(tire):

    #Click on go Button
    pyautogui.moveTo(1320, 260)
    time.sleep(3)
    pyautogui.click()

    #Click on For sale by owner

    pyautogui.moveTo(320, 470)
    time.sleep(5)
    pyautogui.click()

    #Click on tires and wheels

    pyautogui.moveTo(320, 435)
    time.sleep(5)
    pyautogui.click()

    #Post Title

    pyautogui.moveTo(320, 240)
    time.sleep(4)
    pyautogui.click()
    pyautogui.write("Set Of (2) Used Tires "+ tire[0] + " " + tire[1] + " For Sale " )
    time.sleep(5)

    #Post City

    pyautogui.moveTo(800, 240)
    time.sleep(5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.write('Houston')
    time.sleep(5)

    #Post Zip code

    pyautogui.moveTo(1100, 240)
    time.sleep(5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.write('77057')
    time.sleep(10)

    #Post A Body

    pyautogui.moveTo(600, 400)
    time.sleep(5)
    pyautogui.click()
    time.sleep(10)
    pyautogui.write("Set of Used Tires " + tire[0] + " " + tire[1] +
                           " for Sale\nUsed OEM Wheels \nMany Sizes in Stock\nSets of 4\nRunflat Tires\nAll Terrain / Mud Terrain\nHigh thread and low tread tires\nInventory Constantly Changing\nFor more information call (713) 780-8083\nAsk for Sales (Sabino, Lalo, Anthony)\nHablamos Espanol")
    time.sleep(7)
    pyautogui.moveTo(50, 500)
    pyautogui.click()
    pyautogui.scroll(-1000)
    time.sleep(4)
    pyautogui.moveTo(1100, 615)
    time.sleep(2)
    pyautogui.click()
    time.sleep(3)

    #On New Page Post Street

    time.sleep(4)
    pyautogui.moveTo(250, 215)
    time.sleep(5)
    pyautogui.click()
    time.sleep(4)
    pyautogui.write('Star Ln')
    time.sleep(4)

    #Post on cross Street

    pyautogui.moveTo(400, 215)
    time.sleep(5)
    pyautogui.write('Fountain View Dr')
    time.sleep(5)
    pyautogui.moveTo(1100, 715)
    time.sleep(6)
    pyautogui.click()
    time.sleep(5)

    #Add Images

    pyautogui.moveTo(250, 260)
    time.sleep(5)
    pyautogui.click()
    time.sleep(6)
    pyautogui.moveTo(350, 465)
    time.sleep(5)
    pyautogui.click()
    time.sleep(5)
    di = (r"C:\Users\Rollo's\Desktop\inventory\tires")
    marca = tire[0]
    foto = (tire[1]+".jpg")
    file_link = os.path.join(di, marca, foto)
    pyautogui.write(file_link)
    time.sleep(6)
    pyautogui.moveTo(550, 500)
    time.sleep(6)
    pyautogui.click()
    time.sleep(15)
    pyautogui.moveTo(1050, 555)
    time.sleep(6)
    pyautogui.click()
    time.sleep(15)

    #Publish

    pyautogui.moveTo(1100, 270)
    time.sleep(5)
    pyautogui.click()
    time.sleep(7)

    #Go Back To AccountPage

    time.sleep(5)
    pyautogui.moveTo(1100, 90)
    time.sleep(5)
    pyautogui.click()
    time.sleep(30)
    

def move_to_main_window():
    time.sleep(2)
    pyautogui.moveTo(30, 10)
    pyautogui.click()
    time.sleep(5)



number_of_postings = 3
open_navigator()
go_to_facebook()
open_second_window()
go_to_craigslist()
move_to_main_window()

i=0
while number_of_postings > i:

    print('step(1)')
    current_tire = find_available_size(tires, brands)

    post_on_facebook(current_tire)
   
    print('step(3)')
    open_second_window()
    time.sleep(30)
    
    post_on_craigslist(current_tire)
    print('step(4)')
    time.sleep(10)
    print(already_posted)
    move_to_main_window()
    time.sleep(5)

    i += 1

print_done_listings(already_posted)
        





