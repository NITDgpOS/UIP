from  setWallpaper import BackgroundChanger
import os
from constants import CURR_DIR,PICS_FOLDER,WEBSITE
import random
import time
from scrape import get_images 
class scheduler():
    def __init__(self):
        print (time.time())
        self.initFetch()
        self.setStartTime(time.time())
        self.changeCycle()
        
        #print("Anything")
    def initFetch(self):
        try:    
            get_images(WEBSITE)
        except ValueError as e:
            print("File could not be retrieved.", e)

    def changeCycle(self):

        while True:
            delta = self.deltaTime()
            if delta>=30:
                dir = CURR_DIR+PICS_FOLDER
                filename = random.choice(os.listdir(dir))
                path = os.path.join(dir, filename)
                BackgroundChanger().change_background(path)
                self.time=time.time()
        
            else:
                time.sleep(30-delta)

            
    def setStartTime(self,time):
        self.time=time

    def deltaTime(self):
        return (time.time()-self.time)

    def checkTime(self):
        if self.deltaTime()>30:
            return True
        return False


scheduler()
