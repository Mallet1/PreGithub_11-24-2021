import pyautogui

print(pyautogui.size()) # returns screen size

width, height = pyautogui.size() # sets width and height
# multiple assignment trick

print(pyautogui.position()) # returns the positions of the mouse

#pyautogui.moveTo(100, 100, duration=1) # moves the mouse to that position

#pyautogui.moveRel(200, 0, duration=1) # moves the mouse however many pixels 
# adds the x and y you pass it

#pyautogui.click() # clicks the mouse
#pyautogui.doubleClick(35,29,duration=0)
#pyautogui.click(1555,242,duration=.25)

# empty trash
#pyautogui.rightClick(35,29,duration=.1)
#pyautogui.click(106,62,duration=.2)
#pyautogui.click(1036,541,duration=.4)

# use pyautogui.displayMousePosition() in python.exe to constantly show the position

# pyautogui.readthedocs.org then hit cheat sheet
