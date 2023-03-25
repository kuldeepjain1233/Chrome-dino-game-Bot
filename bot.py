 import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    #for cactus
    for i in range (250,300):
        for j in range (350,445):
            if data[i, j] == 172:
                hit("space")
                return

    '''for bird
    for i in range (200,260):
         for j in range (280,370):
             if data[i, j] > 160:
                 hit("down")
                 return True
    return False'''
 
if __name__ == "__main__":
    time.sleep(2)
    
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
    
        

             
        '''for i in range (160,1670):
            for j in range (390,400):
                data[i, j] = 0

        image.show()
        break'''

                


