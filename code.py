import RPi.GPIO as GPIO     
import time

GPIO.setmode(GPIO.BOARD)     

LED = 12                    
TRIG = 40
ECHO = 38
GPIO.setup(LED, GPIO.OUT)  
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pwm = GPIO.PWM(LED, 100)   
pwm.start(0)


def Distance():                
    GPIO.output(TRIG, True)       
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()          

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    time_interval = stop - start

    distance = time_interval / 0.000058
    return distance


while True:
    distance = Distance()       
    print(distance)              
    if distance <= 25:    
        pwm.ChangeDutyCycle(100 - (distance/25 * 100))        
        time.sleep(0.1)                                               
    else:
        pwm.ChangeDutyCycle(0)


pwm.stop()              
GPIO.cleanup()
