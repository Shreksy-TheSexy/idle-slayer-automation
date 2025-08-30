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

win = tk.Tk()
win.overrideredirect(True)
win.geometry("400x100+1715+0")
win.withdraw()
win.configure(bg = bg)
win.attributes("-topmost", True)
label = tk.Label(win, text = "Program Running", font = ("Ariel", 20),fg = fg, bg = bg)
label.pack(expand=True)



def pixel_watcher():
    global clicking
    while True:
        if running:
            bonus_stage = 'bonus_stage_indicator.png'
            bonus_stage_location = (1200,250,1400,550)
            try: 
                is_bonus_stage = pyautogui.locateOnScreen(bonus_stage, region = bonus_stage_location, confidence= 0.8)
                if is_bonus_stage:
                    clicking = False
                    if pyautogui.pixel(1400,1766) == (22,12,27):
                        pyautogui.moveTo(1400,1766)
                        pyautogui.mouseDown()
                        pyautogui.moveTo(2500,1776,duration = 1)
                        pyautogui.mouseUp()
                        bonus_stage_player()
                    elif pyautogui.pixel(2425,1766) == (22,12,27):
                        pyautogui.moveTo(2425,1766)
                        pyautogui.mouseDown()
                        pyautogui.moveTo(1300,1776,duration = 1)
                        pyautogui.mouseUp()
                        bonus_stage_player()
            except pyautogui.ImageNotFoundException:
                pass
            
            time.sleep(5)
        time.sleep(0.1)





def auto_clicker():
    while True:
        if clicking:
            pyautogui.leftClick(3840,1475)
            pyautogui.rightClick(3840,1475)
        time.sleep(0.01)

      

def bonus_stage_player():
    global clicking
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
bonus_stage_thread = threading.Thread(target = pixel_watcher,daemon=True)

bonus_stage_thread.start()
click_thread.start()


hot_keys = ['f6','f6+space','f6+f7','f6+f5']

for key in hot_keys:
    keyboard.add_hotkey(key,toggle_event)

exit_thread = threading.Thread(target = exit_program,daemon = True).start()


win.mainloop()
"""

# pixel finder!!
import tkinter as tk
import pyautogui

def update_position():
    x, y = pyautogui.position()  # Get current mouse position
    color = pyautogui.pixel(x,y)
    label.config(text=f"X: {x}  Y: {y}, color:{color}")
    
    # Move the window slightly offset from the mouse so it doesn't overlap
    root.geometry(f"+{x + 20}+{y + 20}")
    
    # Schedule the function to run again after 50ms
    root.after(50, update_position)

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-topmost', True)  # Keep window on top

label = tk.Label(root, text="", font=("Arial", 10), bg="yellow")
label.pack()

update_position()  # Start the update loop
root.mainloop()"""