import pyautogui
import eyes


def makeDecision():
    clickx=eyes.clickTarget[0]/2
    clicky=eyes.clickTarget[1]/2
    print("Folding")
    pyautogui.click(x=clickx,y=clicky)
    #pyautogui.click(x=clickTarget[0]/2,y=clickTarget[1]/2)
