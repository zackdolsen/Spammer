import pyautogui
script = "Happy Birthday to You! Happy Birthday to You! Happy Birthday Dear Daddy James, Happy Birthday to You! From good friends and true, From old friends and new, May good luck go with you, And happiness too. "

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter"),
    

