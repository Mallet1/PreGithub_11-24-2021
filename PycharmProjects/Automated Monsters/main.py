import pyautogui, time

while True:

    # check if there are no islands with torches left
    if pyautogui.locateCenterOnScreen('Finished.png', confidence = .8) is not None:
        break

    # visit someone's island
    location = None
    while location is None:
        location = pyautogui.locateCenterOnScreen('Visit Island Button.png', confidence = .8)
    else:
        pyautogui.click(location)

    # find their island with a flame
    count = 0
    count_to = 21
    location = None
    while location is None:
        location = pyautogui.locateCenterOnScreen('Flame on Map.png', confidence = .7)
        if location is not None:
            x, y = location
        else:
            x, y = (0, 0)

        # make sure the fire is in the center of the screen
        if x < 900 or x > 1080:
            print('not centered')
            location = None
            next_coords = pyautogui.locateCenterOnScreen('Next Island.png', confidence = .8)
            pyautogui.click(next_coords)
            count += 1

        print(location)

        # if there is no fire check mirror islands
        if count >= count_to:
            mirror_coords = pyautogui.locateCenterOnScreen('Mirror Islands.png', confidence=.8)
            pyautogui.click(mirror_coords)
            count = 0
            count_to = 6
    else:
        # click go button
        go_coords = pyautogui.locateCenterOnScreen('Go Button.png', confidence = .8)
        pyautogui.click(go_coords)

    # find flame on island
    location = None
    while location is None:
        location = pyautogui.locateCenterOnScreen('Fire on Island.png', confidence = .8)
    else:
        time.sleep(1)
        pyautogui.click(location)

        friend_coords = pyautogui.locateCenterOnScreen('Friends Button.png', confidence = .8)
        pyautogui.click(friend_coords)

    time.sleep(1)