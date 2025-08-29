import keyboard
import time
import threading
import pyautogui
import tkinter as tk

hotkey = 'r'
pyautogui.PAUSE = 0

clicking = False

def auto_clicker():
    while True:
        if clicking:
            pyautogui.leftClick()
        time.sleep(0.001)


def show_message(msg):
    win = tk.Tk()
    win.overrideredirect(True)
    win.geometry("400x100+1800+350")
    win.attributes("-topmost", True)
    label = tk.Label(win, text = msg, font=("Ariel",20))
    label.pack(expand=True,fill="both")
    win.after(1000,win.destroy)
    win.mainloop()

        
def toggle_event(key):
    global clicking
    if key.name == hotkey:
        if clicking:
            show_message("clicking stopped")
        else:
            show_message("clicking started")
        clicking = not clicking

click_thread = threading.Thread(target=auto_clicker, daemon=True)

click_thread.start()



keyboard.on_release(callback=toggle_event)
keyboard.wait("esc")