import Tkinter as tk 
from gopigo import *

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

command = tk.Tk()
command.bind_all('<Key>',key_input)
command.mainloop()
