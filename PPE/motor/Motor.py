
#test python

#import libraries
import sys
import time
import RPi.GPIO as GPIO

#Set the board for the pin
GPIO.setmode(GPIO.BCM)

#Define the GPIO pins

#Setup pin 21 20 16
GPIO.setup(21, GPIO.OUT) #PULSE 
GPIO.setup(20, GPIO.OUT) #DIR
GPIO.setup(16, GPIO.OUT) #ENABLE



class Motor:
    
    def __init__(self):
        
        self.stepCounter = 0
        self.dir = 0
        self.stop=0

        #test direction
        #GPIO.output(20, GPIO.LOW)


    def run(self):
            
        while(self.stop):
            print(stepCounter)

            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.00003)
            GPIO.output(21, GPIO.LOW)
            time.sleep(0.00003)


            stepCounter = stepCounter + 1
            if(stepCounter==3600):
                    if(dir==1):
                            dir=0
                            GPIO.output(20, GPIO.HIGH)
                    elif(dir==0):
                            dir=1
                            GPIO.output(20, GPIO.LOW)		

                    stepCounter = 0
                    print("Changing direction")
                    time.sleep(0.1)


     def stop():
         self.stop=1
 
