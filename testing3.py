import Tkinter as tk 
from gopigo import *

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'w':
        fwd()
    elif key_press == 'q':
        left_rot()
    elif key_press == 'e':
        right_rot()
    elif key_press == 'a':
         left()
    elif key_press == 's':
        bwd()
    elif key_press == 'd':
        right()
    elif key_press == 'space':
        stop()

command = tk.Tk()
command.bind_all('<Key>',key_input)
command.mainloop()
