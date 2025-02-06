import os
import time
import pyautogui
import pyperclip
import threading


def scroll(x):
    pyautogui.scroll(-1 * x)
    time.sleep(0.1)

for i in range(1, 6):
    print(i)
    time.sleep(1)

# 5개하면 대략 3분 30초.

for k in range(10):

    for i in range(13):

        pyautogui.click(3507, 101)
        time.sleep(0.002)

        for j in range(18):
            pyautogui.scroll(-1)
            time.sleep(0.002)

        pyautogui.click(3200, 391)
        time.sleep(0.5)

        scroll(k)
        
        pyautogui.click(3133, 194 + 17*i)
        time.sleep(0.01)
        pyautogui.click(3133, 194 + 17*i)
        time.sleep(0.01)





print("🎉 모든 프레임이 전송되었습니다!")
