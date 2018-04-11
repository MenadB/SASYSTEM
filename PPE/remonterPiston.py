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

stepCounter = 0
dir = 1
monte = 0

timeSleep = 0.0003
GPIO.output(20, GPIO.HIGH)


while(monte < 200):
	#print(stepCounter)

	GPIO.output(21, GPIO.HIGH)
	time.sleep(timeSleep)
	GPIO.output(21, GPIO.LOW)
	time.sleep(timeSleep)

	
        monte = monte + 1
        
GPIO.cleanup()





