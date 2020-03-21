from ps3 import *
from gopigo import *

led_on(LED_L)
led_on(LED_R)
enable_servo()

print "preparing ps3 control"
p=ps3()		
print "ready"
s=200	
run=1
while True:
	if run:
		set_speed(s)	
	p.update()			
	if p.up:			
		if run:
			fwd()
		print "moving forward"

	elif p.left:		
		if run:
			left_rot()
			
		print "rotating left"

	elif p.right:		
		if run:
			right_rot()
			
		print "rotating right"

	elif p.down:		
		if run:
			bwd()
		print "moving backwards"

	elif p.cross:		
		if run:
			stop()

		print"stop"
		print us_dist(15)

	elif p.square:
                if run:
                        servo(135)
                        time.sleep(0.1)
                        print "135 camera degree"
                        disable_servo()

        elif p.triangle:
                if run:
                        servo(90)
                        time.sleep(0.1)
                        print "90 camera degree"
                        disable_servo()

        elif p.circle:
              if run:
                      servo(45)
                      time.sleep(0.1)
                      print "45 camera degree"
                      disable_servo()
                        
        elif p.l1:
           if run:
                   servo(180)
                   time.sleep(0.1)
                   print "180 camera degree"
                   disable_servo()

        elif p.r1:
           if run:
                   servo(0)
                   time.sleep(0.1)
                   print "0 camera degree"
                   disable_servo()

        elif p.l2:
           if run:
                   print "speed down -10"
                   s-=10

        elif p.r2:
           if run:
                   print "speed up +10"
                   s+=10

        elif p.ps:
           if run:
                   print "turning led light off"
                   led_off(LED_L)
                   led_off(LED_R)
                   

        elif p.start:
              if run:
                      print "default speed"
                      s=200
                      time.sleep(0.1)
                      
                      

        elif p.select:
               if run:
                       print volt()
                       print "turning led light on"
                       led_on(LED_L)
                       led_on(LED_R)
                       
                   
                        
                        
                        
                       
			

		
		
