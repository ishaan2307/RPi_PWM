import RPi.GPIO as GPIO                #importing libraries. 
import time

GPIO.setmode(GPIO.BOARD)     

LED = 12                    # the pins to which the following units are connected. 
TRIG = 40
ECHO = 38
GPIO.setup(LED, GPIO.OUT)  
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pwm = GPIO.PWM(LED, 100)        # initializing and starting the pwm method with 100hz as frequency. 
pwm.start(0)


def Distance():                
    GPIO.output(TRIG, True)       # triggering an ultrasonic outburst so that it hits the object. 
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:        #for the time the input is not there and is 0 record the time(that will be start) 
        start = time.time()          

    while GPIO.input(ECHO) == 1:      #till echo is 1 record the time( that will be stop time). 
        stop = time.time()

    time_interval = stop - start             #time interval will be stop time - start time. 

    distance = time_interval / 0.000058      #making calculations for finding distance. 
    return distance


while True:
    distance = Distance()       
    print(distance)              
    if distance <= 25:    
        pwm.ChangeDutyCycle(100 - (distance/25 * 100))        
        time.sleep(0.1)                                               
    else:
        pwm.ChangeDutyCycle(0)           #if distance is greater than 25 then change the duty cycle to 0 and turn off the led. 


pwm.stop()              
GPIO.cleanup()
