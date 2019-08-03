import pyautogui
import eyes
from Hands import fold
from Hands import check
from Hands import call
def makeDecision():
    if(not check()):
        fold()
    #pyautogui.click(x=clickTarget[0]/2,y=clickTarget[1]/2)
