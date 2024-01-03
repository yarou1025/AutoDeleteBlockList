import pyautogui
import time

try: 
    time.sleep(1)
    pyautogui.moveTo(1259, 225)
    pyautogui.click()
    for i in range(29):
        time.sleep(0.5)
        pyautogui.moveTo(1345, 307)
        pyautogui.click()

        time.sleep(0.3)
        pyautogui.moveTo(1094, 532)
        pyautogui.click()

except KeyboardInterrupt:
    print("\nKeyboardInterrupt received. Stopping the script.")
