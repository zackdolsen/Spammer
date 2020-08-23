import pyautogui
import time
script = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

for x in script.split():
    pyautogui.write(x)
    time.sleep(0.1)
    pyautogui.press("enter"),
    

