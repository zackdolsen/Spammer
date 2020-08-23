import pyautogui
import time
script = "i didnt fuck my cat. i didnt cum on my cat. i didnt put my dick anywhere near my cat. Ive never done anything weird with my cats. I promised myself i wasnt going to make apology videos after last years thing so im just trying to be as short and honest with this as possible."

for x in script.split():
    pyautogui.write(x)
    time.sleep(0.1)
    pyautogui.press("enter"),
    

