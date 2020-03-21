import Tkinter as tk 
from gopigo import *

led_on(LED_L)
led_on(LED_R)
enable_servo()

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)
   
    if key_press == 'w':
        fwd()
        print "moving forward"
        
    elif key_press == 'q':
        left_rot()
        print "rotating anticlockwise"
        
    elif key_press == 'e':
        right_rot()
        print "rotating clockwise"
        
    elif key_press == 'a':
         left()

    elif key_press == 's':
        bwd()
        print "moving backward"

        
    elif key_press == 'd':
        right()
        
    elif key_press == 'space':
        stop()
        print "stop"
        
    elif key_press == 'z':
        print volt()
    elif key_press == 'x':
        increase_speed()
    elif key_press == 'c':
        decrease_speed()
    elif key_press == 'v':
         set_speed(200)

    elif key_press == '1':
         servo(180)
         time.sleep(1)
         disable_servo()

    elif key_press == '2':
         servo(135)
         time.sleep(1)
         disable_servo()

    elif key_press == '3':
         servo(90)
         time.sleep(1)
         disable_servo()

    elif key_press == '4':
         servo(45)
         time.sleep(1)
         disable_servo()
        
    elif key_press == '5':
         servo(0)
         time.sleep(1)
         disable_servo()
        
        


command = tk.Tk()
command.bind_all('<Key>',key_input)
command.mainloop()
