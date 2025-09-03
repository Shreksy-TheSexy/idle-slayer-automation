import keyboard
import time
import threading
import pyautogui
import tkinter as tk

pyautogui.PAUSE = 0

running = False
clicking = False

hot_keys = ['f6','f6+space','f6+f7','f6+f5']

mouse_pos = (3840,1450)

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


win = tk.Tk()
win.overrideredirect(True)
win.geometry("400x100+1715+0")
win.withdraw()
win.configure(bg = bg)
win.attributes("-topmost", True)
label = tk.Label(win, text = "Program Running", font = ("Ariel", 20),fg = fg, bg = bg)
label.pack(expand=True)


def pixel_watcher():
    global clicking,bonus_stage_count,chest_hunt_count,perfect_chest_hunt_count
    while True:
        if running:

            try: 
                if pyautogui.locateOnScreen(bonus_stage, region = bonus_stage_location, confidence=0.8) != None:
                    clicking = False
                    print("bonus stage")
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
                if pyautogui.locateOnScreen(chest_hunt, region = chest_hunt_location, confidence= 0.8) != None :
                    clicking = False
                    print("chest hunt")
                    chest_hunt_count+=1
                    x2_found = False
                    perfect_chest_hunt = False

                    time.sleep(4)
                    if running:
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

                    if running:
                        if (3202, 821) in chests_locations:
                            pyautogui.click(3202, 821)
                            time.sleep(3)
                            if pyautogui.pixel(2050,1970) == (106,190,48):
                                x2_found = True
                                pyautogui.click(saver_location)
                                time.sleep(3)

                    if running and not x2_found and (3202, 1391) in chests_locations:
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
                        
                        if pyautogui.pixel(1900,1930)[0] == 175 and running:
                                break
                        if pyautogui.pixel(1900,1976) == (106,190,48) and not x2_found:
                                x2_found = True
                                pyautogui.click(saver_location)
                                time.sleep(3)
                        if (chest_x,chest_y) in chests_locations and running:
                            pyautogui.click(chest_x,chest_y)
                            time.sleep(3)
                    else:
                        if running:
                            time.sleep(10)
                            try:
                                if pyautogui.locateOnScreen(perfect_chest,region = chest_hunt_location,confidence=0.9):
                                    perfect_chest_hunt = True
                                    perfect_chest_hunt_count+=1
                            except pyautogui.ImageNotFoundException:
                                pass


                    if perfect_chest_hunt and running:

                        pyautogui.click(2370,1230)
                        time.sleep(12)
                        print("perfect!!!")
                    
                    if running:
                        pyautogui.click(1900,1970)
                        time.sleep(3)
                        if running:
                            clicking = True
            except pyautogui.ImageNotFoundException:
                pass

            
            time.sleep(0.1)
        time.sleep(0.1)




def auto_clicker():
    while True:
        if clicking:
            pyautogui.leftClick(mouse_pos)
            pyautogui.rightClick(mouse_pos)
        time.sleep(0.001)

      

def bonus_stage_player():
    global clicking
    time.sleep(40)
    if running:
        pyautogui.click(2150,1650)
        time.sleep(6)
        clicking = True




def exit_program():
    keyboard.wait('esc')
    print(f"bonus stages: {bonus_stage_count}, chest hunts: {chest_hunt_count}, perfect chest hunts: {perfect_chest_hunt_count}")
    win.after(0,win.destroy)

        
def toggle_event():
    global running,win,clicking
    running = not running
    clicking = running
    if running:
        win.deiconify()
    else:
       win.withdraw()
        
        



click_thread = threading.Thread(target=auto_clicker, daemon=True)
interference_thread = threading.Thread(target=pixel_watcher,daemon=True)

interference_thread.start()
click_thread.start()


for key in hot_keys:
    keyboard.add_hotkey(key,toggle_event)

exit_thread = threading.Thread(target = exit_program,daemon = True).start()


win.mainloop()