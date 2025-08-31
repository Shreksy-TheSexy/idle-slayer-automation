import keyboard
import time
import threading
import pyautogui
import tkinter as tk

pyautogui.PAUSE = 0

running = False
clicking = False

bg = "#70a9a1"
fg = "#f5f5f5"

"bonus stage activation requirements"
bonus_stage = 'bonus_stage_indicator.png'   
bonus_stage_location = (1200,250,1400,550)

"chest hunt activation requirements"
chest_hunt = 'chest_hunt_indicator.png'
chest_hunt_location = (480,680,2850,820)


win = tk.Tk()
win.overrideredirect(True)
win.geometry("400x100+1715+0")
win.withdraw()
win.configure(bg = bg)
win.attributes("-topmost", True)
label = tk.Label(win, text = "Program Running", font = ("Ariel", 20),fg = fg, bg = bg)
label.pack(expand=True)

conf = 1

def pixel_watcher():
    global clicking
    while True:
        if running:

            try: 
                if pyautogui.locateOnScreen(bonus_stage, region = bonus_stage_location, confidence=0.8) != None:
                    clicking = False
                    not_started = True
                    while not_started:
                        print("balls")
                        if pyautogui.pixel(1307,1694)[0] == 0 or pyautogui.pixel(1307,1522)[0] == 0:
                            print("r2l")
                            not_started = False
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
                            print("l2r")
                            not_started = False
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
                try: 
                    if pyautogui.locateOnScreen(chest_hunt, region = chest_hunt_location, confidence= 0.8) != None :
                        clicking = False
                        chest_hunt_ended = False
                        time.sleep(4)
                        pyautogui.click(3240,800)
                        time.sleep(3)
                        pyautogui.click(3240,1400)
                        time.sleep(3)
                        for i in range(1400,700,-300):
                            for j in range(630,3500,290):
                                if pyautogui.pixel(1900,1930)[1] == 175:
                                    chest_hunt_ended = True
                                    break
                                pyautogui.click(j,i)
                                time.sleep(3)
                            if chest_hunt_ended:
                                break
                        pyautogui.click(1900,1970)
                        time.sleep(3)

                        clicking = True
                except:
                    pass
            
            time.sleep(0.1)
        time.sleep(0.1)





def auto_clicker():
    while True:
        if clicking:
            pyautogui.leftClick(3840,1475)
            pyautogui.rightClick(3840,1475)
        time.sleep(0.01)

      

def bonus_stage_player():
    global clicking
    time.sleep(40)
    if running:
        pyautogui.click(2150,1650)
        time.sleep(6)
        clicking = True




def exit_program():
    keyboard.wait('esc')
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
interference_thread = threading.Thread(target = pixel_watcher,daemon=True)

interference_thread.start()
click_thread.start()


hot_keys = ['f6','f6+space','f6+f7','f6+f5']

for key in hot_keys:
    keyboard.add_hotkey(key,toggle_event)

exit_thread = threading.Thread(target = exit_program,daemon = True).start()


win.mainloop()