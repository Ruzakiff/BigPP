import time
from eyes import isOurAction
from eyes import checkAllCards
from eyes import findWindowEdge
from eyes import initialize
from eyes import *
from brain import makeDecision

initialize()
while True:
    checkTotalPotSize()
    checkMainPotSize()
#     #checkPotSize()
#      if(isOurAction()):
#          print("Making Decision")
#          makeDecision()
    #time.sleep(1)
