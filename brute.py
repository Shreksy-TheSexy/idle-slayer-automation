import keyboard
import time
import threading
import pyautogui
import tkinter as tk
import sys

pyautogui.PAUSE = 0

running = False

bg = "#70a9a1"
fg = "#f5f5f5"

win = tk.Tk()
win.overrideredirect(True)
win.geometry("400x100+1690+0")
win.configure(bg = bg)
win.attributes("-topmost", True)
label = tk.Label(win, text = "Program Running", font = ("Ariel", 20),fg = fg, bg = bg)
label.pack(expand=True)





def auto_clicker():
    while True:
        if running:
            pyautogui.leftClick()
        time.sleep(0.01)

      
def exit_program():
    keyboard.wait('esc')
    win.after(0,win.destroy)

        
def toggle_event():
    global running,win
    running = not running
    if running:
        win.deiconify()
    else:
       win.withdraw()
        
        



click_thread = threading.Thread(target=auto_clicker, daemon=True)
click_thread.start()




keyboard.add_hotkey('r',toggle_event)
exit_thread = threading.Thread(target = exit_program,daemon = True).start()


win.mainloop()