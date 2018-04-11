#!/usr/binenv python
#*- coding: utf- -*-

#import librairies
import random
import sys
import time
import RPi.GPIO as GPIO
from Sound import Sound
from Motor import Motor
from temporaire import Capteur
import threading

# 1) Lancement du guide d'installation
# 2) Capteur cardiaque (thread)
# 3) Soit massage cardiaque, soit indication que la personne est vivante (instruction annexe)
# 4) Si réanimation : indication à l'utilisateur, arret du massage
# Si demande d'arrêt du massage avec confirmation (demande vocale) ==> arrêt du massage
# 5) Demande de l'arrêt complet de l'appareil (confimation demandée) ==> arrêt du démon

#time.sleep(5)

if __name__ == '__main__':
    
	    
    #Variables
    step0 = 1
    step1 = 0
    step2 = 0
    compteurAlive = 0
    compteurDead = 0
    bpm = 0
    stop = 0
    
    
    #Initialisation des pins
    #Set the board for the pin
    GPIO.setmode(GPIO.BCM)

    #Define the GPIO pins

    #Setup pin 21 20 16
    GPIO.setup(21, GPIO.OUT) #PULSE 
    GPIO.setup(20, GPIO.OUT) #DIR
    GPIO.setup(16, GPIO.OUT) #ENABLE

    GPIO.setup(20, GPIO.LOW) #Direction vers le bas au début

    #Pin for button SOUND control
    GPIO.setup(5,GPIO.IN)
    GPIO.setup(6,GPIO.IN)
    GPIO.setup(13,GPIO.IN)
    GPIO.setup(19,GPIO.IN)




    try:

        #Step 0 : Give instructions to place the structure
        sound = Sound()

        while step0:
            print("**********STEP 0***********")
            print("Instruction to place the structure")
            
            
            #other instructions
            """while sound.actual < 2:
                
                if (GPIO.input(13)==False):
                    sound.nextInstruction()
                elif (GPIO.input(19)==False):
                    sound.prevIntruction()
                elif (GPIO.input(6)==False):
                    sound.stop()
                elif (GPIO.input(5)==False):
                    sound.pause()
            


            #First intructions
            sound.play()
            time.sleep(2)
            for i in range (1, len(sound.audio)):
                sound.nextInstruction()
                time.sleep(2)
	    """
 

            step0 = 0
            step1 = 1
        
        #Start to launch the captor
            
        #capteur = Pulsesensor()
        #p.startAsyncBPM()
        
        print("*********STEP 1**********")
        print("Check the heartbeat of the victim")
        while step1:
            #bpm = capteur.BPM
            bpm = random.randint(0,0)   # Scenario 1
            #bpm = random.randint(60,80) # Scenario 2
            
            if bpm > 0:
                print("BPM: %d" % bpm)
                print("The person is still alive")
                compteurAlive += 1
                compteurDead = 0
            else:
                
                print("No heartbeat found")
                compteurAlive = 0
                compteurDead += 1  
                
            if compteurAlive > 10:
                print("Launching insteuction mode to indicate the person is alive")
                step1 = 0
                
            if compteurDead > 10:
                print("Launching motor")
                step1=0
                step2=1
                
            if stop:
                step0=0
                step1=0
                step2=0
            time.sleep(0.5)
            
        print("*********STEP 2**********")
        print("Starting reanimation")
        
        
        #motor = Motor()
        #motor.start()
        
        timeSleep = 0.003
        impulsions = 0
        stepCounter = 0
        trigger = 4 #30 
        dir = 0
        
        compteurAlive = 0
        compteurDead = 0 

        while(step2):
            
            #print(stepCounter)
            if impulsions < trigger:
                GPIO.output(21, GPIO.HIGH)
                time.sleep(timeSleep)
                GPIO.output(21, GPIO.LOW)
                time.sleep(timeSleep)

                stepCounter = stepCounter + 1
                if(stepCounter==1500):  #3500
                        print(dir)
                        if(dir==1):
                                dir=0
                                GPIO.output(20, GPIO.HIGH)
                                impulsions = impulsions + 1
                                print(impulsions)
                                
                        elif(dir==0):
                                dir=1
                                GPIO.output(20, GPIO.LOW)		

                        stepCounter = 0
                        print("Changing direction")
                        timeSleep = 0.0005
                        time.sleep(0.02)
                        
                if(timeSleep > 0.00002 and stepCounter <3000):
                    timeSleep = timeSleep / 1.01
                if(timeSleep > 0.00002 and stepCounter >3000):
                    timeSleep = timeSleep / 1.01
                
                print(timeSleep)
                
            else :
                #play instruction
                #...
                
                #Insufflations
                print("Insufflations")
                impulsions = 0
                
                # Mesurer si la personne est réanimée
                bpm = random.randint(0,0)
                
                    
                # Si il y a une activité cardiaque on vérifie pendant 
                if bpm > 0:
                    print("BPM: %d" % bpm)
                    print("The person is alive")
                    
                    for i in range(1,5):
                        bpm = random.randint(0,0) # The person is dead
                        #bpm = random.randint(50,65)
                        if (bpm > 50):
                            
                            compteurAlive += 1
                            
                        time.sleep(1)
                    
                    if(compteurAlive > 4):
                        step2 = 0
                    else :
                        compteurAlive = 0
                        
                    
                else:
                    
                    print("No heartbeat found")
                    compteurAlive = 0
                    compteurDead+=1
                    
                if stop:
                    step0=0
                    step1=0
                    step2=0
                    
                    
                time.sleep(3)
                


            
        
        
        """
        compteurAlive = 0
        compteurDead = 0
        
        while step2:
            #Measure the pulse
            bpm = random.randint(0,0) # The person has not been reanimated
            #bpm = random.randint(50,55) # The person is alive
            
            #Same as before
            if bpm > 0:
                print("BPM: %d" % bpm)
                print("The person is still alive")
                compteurAlive += 1
                compteurDead = 0
            else:
                
                print("No heartbeat found")
                compteurAlive = 0
                compteurDead+=1
                
            if compteurAlive > 10:
                print("Launching instruction mode to indicate the person is alive")
                step2 = 0
                motor.continuer = 0
                
            if stop:
                step0=0
                step1=0
                step2=0
            time.sleep(3)
            """
        
    except:
        print("Fatal error daemon")
    

    
    
    
    
    

#fin du programme
    GPIO.cleanup()
    
    
    
    
