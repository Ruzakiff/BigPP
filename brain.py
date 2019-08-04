import pyautogui
import eyes

from Hands import fold
from Hands import check
from Hands import call
from Hands import rebet
from Hands import bet

#from Hands import raise
def makeDecision():
    if(not rebet("20") or not bet("69")):
        fold()
    #pyautogui.click(x=clickTarget[0]/2,y=clickTarget[1]/2)
