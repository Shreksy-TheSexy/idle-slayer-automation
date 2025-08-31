import tkinter as tk
import pyautogui

def update_position():
    x, y = pyautogui.position() 
    color = pyautogui.pixel(x,y)
    label.config(text=f"X: {x}  Y: {y}, color:{color}")
    root.geometry(f"+{x + 20}+{y + 20}")
    root.after(50, update_position)

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
label = tk.Label(root, text="", font=("Arial", 10), bg="yellow")
label.pack()

update_position()  


root.mainloop()