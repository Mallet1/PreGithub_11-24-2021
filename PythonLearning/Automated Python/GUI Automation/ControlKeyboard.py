import pyautogui

pyautogui.click(1580,200)
#pyautogui.typewrite('Hello world!')#, interval=.08)
pyautogui.keyDown('d')
pyautogui.PAUSE=1
pyautogui.keyUp('d')
# interval is the time between each letter

pyautogui.typewrite(['a','b','left','left','X','Y'], interval=.8)

pyautogui.KEYBOARD_KEYS # returns the keyboard keys

# pyautogui.readthedocs.org then hit cheat sheet
