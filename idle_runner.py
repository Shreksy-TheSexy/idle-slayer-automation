import keyboard
import time
import threading
import pyautogui
import tkinter as tk
import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from email.utils import make_msgid
import mimetypes

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

email = os.getenv("EMAIL")
email_password = os.getenv("PASSWORD")




image_cid = make_msgid()

context = ssl.create_default_context()


pyautogui.PAUSE = 0

program_running = False
interference_runnning = False
clicking = False
email_alerts = True # controls email alerts


hot_keys = ['f6','f6+space','f6+f7','f6+f5']

mouse_pos = (3839,1450)

bg = "#70a9a1"
fg = "#f5f5f5"

"bonus stage activation requirements"
bonus_stage = 'bonus_stage_indicator.png'   
bonus_stage_location = (1200,250,1400,550)
bonus_stage_count = 0


"chest hunt activation requirements"
chest_hunt = 'chest_hunt_indicator.png'
saver = 'chest_hunt_saver.png'
perfect_chest = 'perfect_chest.png'
chest_hunt_location = (380,600,3020,950)
chest_hunt_count = 0
perfect_chest_hunt_count = 0


"random box activation requerments"
random_box = "random_box.png"
random_box_loaction = (300,200,300,900)
random_box_count = 0

minion_collected_count = 0

win = tk.Tk()
win.overrideredirect(True)
win.geometry("400x100+1715+0")
win.withdraw()
win.configure(bg = bg)
win.attributes("-topmost", True)
label = tk.Label(win, text = "Program Running", font = ("Ariel", 20),fg = fg, bg = bg)
label.pack(expand=True)


def pixel_watcher():
    global clicking,bonus_stage_count,chest_hunt_count,random_box_count,perfect_chest_hunt_count,minion_collected_count,interference_runnning
    while True:
        if program_running:

            try: 
                if pyautogui.locateOnScreen(bonus_stage, region = bonus_stage_location, confidence=0.8) != None and not interference_runnning:
                    interference_runnning = True
                    clicking = False
                    bonus_stage_count+=1

                    if pyautogui.pixel(1307,1694)[0] == 0 or pyautogui.pixel(1307,1522)[0] == 0:
                        if pyautogui.pixel(1307,1522)[0] == 0:
                            y = 1530
                        else:
                            y = 1700
                        button_location = (2470,y)
                        pyautogui.moveTo(button_location)
                        time.sleep(1)
                        end_location = (button_location[0]-1150,button_location[1])
                        pyautogui.mouseDown()
                        pyautogui.moveTo(end_location,duration = 1)
                        pyautogui.mouseUp()
                        bonus_stage_player()
                    
                    elif pyautogui.pixel(2527,1694)[0] == 0 or pyautogui.pixel(2527,1526)[0] == 0:
                        if pyautogui.pixel(2527,1522)[0] == 0:
                            y = 1530
                        else:
                            y = 1700
                        button_location = (1370,y)
                        pyautogui.moveTo(button_location)
                        time.sleep(1)
                        end_location = (button_location[0]+1150,button_location[1])
                        pyautogui.mouseDown()
                        pyautogui.moveTo(end_location,duration = 1)
                        pyautogui.mouseUp()
                        bonus_stage_player()
                    
            except pyautogui.ImageNotFoundException:
                pass

            try: 
                if pyautogui.locateOnScreen(chest_hunt, region = chest_hunt_location, confidence= 0.8) != None and not interference_runnning:
                    interference_runnning = True
                    clicking = False
                    chest_hunt_count+=1
                    chest_hunt_player()

            except pyautogui.ImageNotFoundException:
                pass

            try:
                if pyautogui.locateOnScreen(random_box, region = random_box_loaction, confidence= 0.9) != None and not interference_runnning:
                    interference_runnning = True
                    clicking = False
                    random_box_count+=1
                    random_box_player()
            
            except pyautogui.ImageNotFoundException:
                pass

            """if pyautogui.pixel(350,250) != (0,68,171) and not interference_runnning:
                interference_runnning = True
                clicking = False
                minion_collected_count +=1
                minion_collector()"""



            time.sleep(0.1)
        time.sleep(0.1)




def auto_clicker():
    while True:
        if clicking:
            pyautogui.leftClick(mouse_pos)
            pyautogui.rightClick(mouse_pos)
        time.sleep(0.001)

      

def bonus_stage_player():
    global clicking,interference_runnning
    time.sleep(40)
    if program_running:
        pyautogui.click(2150,1650)
        time.sleep(6)
        interference_runnning = False
        clicking = True



def chest_hunt_player():
    global clicking,interference_runnning,perfect_chest_hunt_count
    x2_found = False
    perfect_chest_hunt = False

    time.sleep(4)
    if program_running:
        pyautogui.mouseDown(500,970)
        pyautogui.moveTo(500,1800,duration=1)
        pyautogui.mouseUp(500,1800)
    time.sleep(3)

    chests = pyautogui.locateAllOnScreen(chest_hunt, region = chest_hunt_location, confidence= 0.99) 
    chests_locations = [] 
    for chest in chests: 
        chests_locations.append((int(pyautogui.center(chest).x),int(pyautogui.center(chest).y)))
    chests_locations.sort(key=lambda k: (-k[1], k[0]))

    saver_np = pyautogui.locateCenterOnScreen(saver, region = chest_hunt_location, confidence= 0.99)
    saver_location = (int(saver_np.x),int(saver_np.y))

    if program_running:
        if (3202, 821) in chests_locations:
            pyautogui.click(3202, 821)
            time.sleep(3)
            if pyautogui.pixel(2050,1970) == (106,190,48):
                x2_found = True
                pyautogui.click(saver_location)
                time.sleep(3)

    if program_running and not x2_found and (3202, 1391) in chests_locations:
        pyautogui.click(3202, 1391)
        time.sleep(3)

    for (chest_x,chest_y) in chests_locations:
            
        try:
            if pyautogui.locateOnScreen(perfect_chest,region = chest_hunt_location,confidence=0.9):
                perfect_chest_hunt = True
                perfect_chest_hunt_count+=1
                break
        except pyautogui.ImageNotFoundException:
            pass
        
        if pyautogui.pixel(1900,1930)[0] == 175 and program_running:
                break
        if pyautogui.pixel(1900,1976) == (106,190,48) and not x2_found:
                x2_found = True
                pyautogui.click(saver_location)
                time.sleep(3)
        if (chest_x,chest_y) in chests_locations and program_running:
            pyautogui.click(chest_x,chest_y)
            time.sleep(3)
    else:
        if program_running:
            time.sleep(10)
            try:
                if pyautogui.locateOnScreen(perfect_chest,region = chest_hunt_location,confidence=0.9):
                    perfect_chest_hunt = True
                    perfect_chest_hunt_count+=1
            except pyautogui.ImageNotFoundException:
                pass


    if perfect_chest_hunt and program_running:

        pyautogui.click(2370,1230)
        time.sleep(12)


        if email_alerts:
            em = EmailMessage()
            em['FROM']  = email
            em['TO']  = email
            pyautogui.screenshot('after_perfect.png')
            em['subject']  = "perfect alert"
            em.set_content(f"random boxes: {random_box_count}, bonus stages: {bonus_stage_count}, chest hunts: {chest_hunt_count}, perfect chest hunts: {perfect_chest_hunt_count}")
            em.add_alternative("""\
            <html>
                <body>
                    <p><br>
                    </p>
                    <img src="cid:{image_cid}">
                </body>
            </html>
            """.format(image_cid=image_cid[1:-1]), subtype='html')

            with open('after_Perfect.png','rb') as img:
                    # know the Content-Type of the image
                    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                    # attach it
                    em.get_payload()[1].add_related(img.read(), 
                                                        maintype=maintype, 
                                                        subtype=subtype, 
                                                        cid=image_cid)



            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email,email_password)
                smtp.sendmail(email,email,em.as_string())
            
            del em

        print("perfect!!!")
    
    if program_running:
        pyautogui.click(1900,1970)
        time.sleep(3)
        if program_running:
            interference_runnning = False
            clicking = True



def random_box_player():
    global clicking,interference_runnning
    if program_running:
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        interference_runnning = False
        if program_running:
            clicking = True



def minion_collector():
    global clicking,interference_runnning
    if program_running:
        time.sleep(1)
        pyautogui.click(290,200)
        time.sleep(1)
        pyautogui.click(1000,2000)
        time.sleep(1)
        pyautogui.click(1000,430)
        time.sleep(1)
        pyautogui.click(1000,430)
        time.sleep(1)
        pyautogui.click(1700,2000)
        interference_runnning = False
        if program_running:
            clicking = True



def exit_program():
    keyboard.wait('esc')
    print(f"random boxes: {random_box_count}, bonus stages: {bonus_stage_count}, chest hunts: {chest_hunt_count}, perfect chest hunts: {perfect_chest_hunt_count}")
    win.after(0,win.destroy)

        
def toggle_event():
    global program_running,win,clicking,interference_runnning
    program_running = not program_running
    clicking = program_running
    if program_running:
        win.deiconify()
    else:
       interference_runnning = False
       win.withdraw()
        
        



click_thread = threading.Thread(target=auto_clicker, daemon=True)
interference_thread = threading.Thread(target=pixel_watcher,daemon=True)

interference_thread.start()
click_thread.start()


for key in hot_keys:
    keyboard.add_hotkey(key,toggle_event)

exit_thread = threading.Thread(target = exit_program,daemon = True).start()


win.mainloop()