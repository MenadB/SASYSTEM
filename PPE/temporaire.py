
import random
import sys
from threading import Thread
import time

class Capteur(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.capteurValue = 0
        
    def run(self):
        tab = [
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
               11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 
               11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0
               ]
        
        while(True):
            for i in range(0,len(tab)):
                self.capteurValue = tab(i)
                time.sleep(0.5)
        

