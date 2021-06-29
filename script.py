import pyautogui
import time


time.sleep(6)

i = 1

while i<=10:
  time.sleep(2)
  pyautogui.typewrite('Hello')
  pyautogui.press('enter')