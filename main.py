# import
import time
import pyautogui
import keyboard


def moveBegin():  # code for snake game
    t = 0.165  # seconds per tile (0.165 for slow, 0.118 for medium, 0.0707 for fast)
    pyautogui.keyDown('d')
    time.sleep(t * 6)
    pyautogui.keyDown('w')
    time.sleep(t * 4)
    while True:
        if keyboard.is_pressed('e'):
            break
        pyautogui.keyDown('a')
        if keyboard.is_pressed('e'):
            break
        time.sleep(t * 9)
        pyautogui.keyDown('s')
        if keyboard.is_pressed('e'):
            break
        time.sleep(t * 8)
        pyautogui.keyDown('d')
        br = False
        for _ in range(4):
            if loop(t):
                br = True
        if br: break
        time.sleep(t * 0.48485)  # calculated ratio for quick turns
        pyautogui.keyDown('w')
        if keyboard.is_pressed('e'):
            break
        time.sleep(t * 8)


def loop(t):  # code for loop portion
    if keyboard.is_pressed('e'):
        return True
    time.sleep(t * 0.24242)  # calculated ratio for quick turns
    pyautogui.keyDown('w')
    if keyboard.is_pressed('e'):
        return True
    time.sleep(t * 7)
    pyautogui.keyDown('d')
    if keyboard.is_pressed('e'):
        return True
    time.sleep(t * 0.2424)
    pyautogui.keyDown('s')
    if keyboard.is_pressed('e'):
        return True
    time.sleep(t * 7)
    pyautogui.keyDown('d')
    if keyboard.is_pressed('e'):
        return True


while True:  # start bot when user press 'q'
    if keyboard.is_pressed('q'):
        moveBegin()
        break
