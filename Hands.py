import pyautogui
import eyes
from eyes import findImage

def fold():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Fold.png',.85):
        print("Fold Image Found")
        clickx=eyes.clickTarget[0]/2
        clicky=eyes.clickTarget[1]/2
        print("Folding")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False

def call():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Call.png',.85):
        print("Fold Image Found")
        clickx=eyes.clickTarget[0]/2
        clicky=eyes.clickTarget[1]/2
        print("Folding")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False

def check():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Check.png',.85):
        print("Fold Image Found")
        clickx=eyes.clickTarget[0]/2
        clicky=eyes.clickTarget[1]/2
        print("Folding")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False
