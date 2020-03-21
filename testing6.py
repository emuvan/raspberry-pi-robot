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
         print "moving left"

    elif key_press == 's':
         bwd()
         print "moving backward"

        
    elif key_press == 'd':
         right()
        
        
    elif key_press == 'space':
        stop()
        print "stop"
        print us_dist(15)

    elif key_press == 'r':
        print "turning light off"
        led_off(LED_L)
        led_off(LED_R)

    elif key_press =='t':
         print "turning light on" 
         led_on(LED_L)
         led_on(LED_R)
        
    elif key_press == 'z':
        print volt()
        
    elif key_press == 'x':
        print "speed up"
        increase_speed()
        
    elif key_press == 'c':
        print "speed down"
        decrease_speed()
        
    elif key_press == 'v':
         print "default speed"
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
