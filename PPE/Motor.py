
#test python

#import libraries
import sys
import time
import RPi.GPIO as GPIO
import threading





class Motor(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.stepCounter = 0
        self.timeCounter = 0
        self.trigger = 30
        self.dir = 0
        self.continuer = 1
        
        #test direction
        #GPIO.output(20, GPIO.LOW)


    def run(self):
        
        impulsions = 0
        timeSleep = 0.01

        
        while(self.continuer):
            
            if impulsions < self.trigger:
                print(self.stepCounter)

                GPIO.output(21, GPIO.HIGH)
                time.sleep(timeSleep)
                GPIO.output(21, GPIO.LOW)
                time.sleep(timeSleep)


                self.stepCounter = self.stepCounter + 1
                if(self.stepCounter==10000):
                        if(self.dir==1):
                                self.dir=0
                                GPIO.output(20, GPIO.HIGH)
                                impulsions = impulsions + 1
                                
                        elif(self.dir==0):
                                self.dir=1
                                GPIO.output(20, GPIO.LOW)

                        self.stepCounter = 0
                        print("Changing direction")
                        time.sleep(0.1)
                        
                if(timeSleep > 0.0001):
                    timeSleep = timeSleep / 1.01
                    
                self.timeCounter = 0
                
            else:
                #play instruction
                #...
                
                #Insufflations
                print("Insufflations")
                time.sleep(5)
                impulsions = 0



 
 
