import pyautogui

pyautogui.screenshot('screenshot_example.png') # takes a screenshot

print(pyautogui.locateOnScreen('screenshot_example.png'))
print(pyautogui.locateCenterOnScreen('screenshot_example.png'))

#center=pyautogui.locateCenterOnScreen('screenshot_example.png')
#pyautogui.click(center)
pyautogui.moveTo((932,336), duration=1)
