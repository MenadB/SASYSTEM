from time import sleep
import RPi.GPIO as GPIO
import pygame



class Sound:
        
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()
        
        #List of audio files
        """Ajouter les instructions ici"""
	
        self.audio = [
            pygame.mixer.Sound("sound1.wav"),
            pygame.mixer.Sound("sound2.wav"),
            pygame.mixer.Sound("sound3.wav"),
            pygame.mixer.Sound("sound4.wav")
            
            
            
            ]
	

        
        self.actual = 0
        self.pause = 0
        self.continuer = 1
    
    #Play
    def play(self):
        print(str(self.audio[self.actual]))
        self.audio[self.actual].play()
        sleep(self.audio[self.actual].get_length())
        
        
            
    #PAUSE
    def pause(self):
    
        if (GPIO.input(5)==0):
            if self.pause==0:
                pygame.mixer.pause()
                self.pause = 1
            
            elif self.pause==1:
                pygame.mixer.unpause()
                self.pause = 0
        #self.audio[actual].stop()

    def stop(self):
        
        #STOP
         #if (GPIO.input(6)==False):
            pygame.mixer.stop()
            sleep(0.5)
        
        
    def nextInstruction(self):
        
        #Next instruction   
        #if (GPIO.input(13)==False):
        if(self.actual < len(self.audio)-1):
            self.actual= self.actual+1
            pygame.mixer.stop()
            self.play()
        else:
            print(self.actual)
            self.play()
        sleep(0.5)    

        #Previous insctruction
    def prevInstruction(self):
        #elif (GPIO.input(19)==False):
        if(self.actual>0):
            self.actual = self.actual-1
            pygame.mixer.stop()
            
            self.play()
        else:
            self.play()
        sleep(0.5)

            



