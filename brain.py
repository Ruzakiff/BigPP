import pyautogui
import eyes

from Hands import fold
from Hands import check
from Hands import call
from Hands import rebet
from Hands import bet
from eyes import checkPotSize

#from Hands import raise
def makeDecision(currentStack,potsize):
    if(not check()):
        if((not bet("30")) and (not rebet("69.69"))):
            fold()
    #pyautogui.click(x=clickTarget[0]/2,y=clickTarget[1]/2)

def ImNotABot(): #ask rob if this is supposed to be here
    print("as")
