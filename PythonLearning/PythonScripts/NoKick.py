import pyautogui, random, os, time

def randMove():
    while True:
        rand=random.randint(1,6)
        if(rand==1):
            pyautogui.keyDown('w')
        if(rand==2):
            pyautogui.keyDown('a')
        if(rand==3):
            pyautogui.keyDown('s')
        if(rand==4):
            pyautogui.keyDown('d')
        if(rand==5):
            pyautogui.keyDown('b')
        if(rand==6):
            pyautogui.press(' ')
            pyautogui.keyUp('w')
            pyautogui.keyUp('a')
            pyautogui.keyUp('s')
            pyautogui.keyUp('d')
            pyautogui.keyUp('b')
        if(pyautogui.locateCenterOnScreen('ReadyButton.png')!=None):
           pyautogui.click(pyautogui.locateCenterOnScreen('ReadyButton.png'))

def getCoords():
    coords = {'rocketIcon':pyautogui.locateCenterOnScreen('RocketIcon.png'),
              'homeScreen':pyautogui.locateCenterOnScreen('HomeScreen.png'),
              'playButton':pyautogui.locateCenterOnScreen('PlayButton.png'),
              'casual':pyautogui.locateCenterOnScreen('Casual.png'),
              'doubles':pyautogui.locateCenterOnScreen('Doubles.png'),
              'gameStart':pyautogui.locateCenterOnScreen('GameStart.png'),
              'endScreen':pyautogui.locateCenterOnScreen('EndScreen.png'),
              'readyButton':pyautogui.locateCenterOnScreen('ReadyButton.png')
              }
    return coords

def navigate():
    while True:
        if(pyautogui.locateCenterOnScreen('RocketIcon.png')!=None):
           pyautogui.doubleClick(pyautogui.locateCenterOnScreen('RocketIcon.png'))
           while(pyautogui.locateCenterOnScreen('RocketIcon.png')!=None):
               continue
           time.sleep(20); pyautogui.typewrite('space')
           time.sleep(4); pyautogui.keyDown('space'); time.sleep(.2); pyautogui.keyUp('space')
           
        #if(pyautogui.locateCenterOnScreen('HomeScreen.png')!=None):
        #   pyautogui.click(pyautogui.locateCenterOnScreen('HomeScreen.png'))
         if(pyautogui.locateCenterOnScreen('PlayButton.png')!=None):
           pyautogui.click(pyautogui.locateCenterOnScreen('PlayButton.png'))
        if(pyautogui.locateCenterOnScreen('Casual.png')!=None):
           pyautogui.click(pyautogui.locateCenterOnScreen('Casual.png'))
        if(pyautogui.locateCenterOnScreen('Doubles.png')!=None):
           pyautogui.click(pyautogui.locateCenterOnScreen('Doubles.png'))
           randMove()
        #if(pyautogui.locateCenterOnScreen('GameStart.png')!=None):
        #   randMove()
        #if(pyautogui.locateCenterOnScreen('ReadyButton.png')!=None):
        #   pyautogui.click(pyautogui.locateCenterOnScreen('ReadyButton.png'))
           
           
os.chdir('C:\\Users\\Sam Mallet\\Desktop\\Rocket Pics')

navigate()

#print(coords.get('rocketIcon'))


