import pyautogui
import eyes
from eyes import findImage

def fold():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Fold.png',.85):
        print("Fold Image Found")
        clickx=eyes.imageLocation[0]/2
        clicky=eyes.imageLocation[1]/2
        print("ACTION Folding")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False

def call():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Call.png',.85):
        print("Call Image Found")
        clickx=eyes.imageLocation[0]/2
        clicky=eyes.imageLocation[1]/2
        print("ACTION Calling")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False

def check():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Check.png',.85):
        print("Check Image Found")
        clickx=eyes.imageLocation[0]/2
        clicky=eyes.imageLocation[1]/2
        print("ACTION Checking")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False
def raise():
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Raise.png',.85):
        print("Raise Image Found")
        clickx=eyes.imageLocation[0]/2
        clicky=eyes.imageLocation[1]/2
        print("ACTION Raising")
        pyautogui.click(x=clickx,y=clicky)
        return True
    return False
