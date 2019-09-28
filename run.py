import time
from eyes import isOurAction
from eyes import checkAllCards
from eyes import findWindowEdge
from eyes import initialize
from eyes import *
from brain import makeDecision

initialize()

while True:
    total=checkTotalPotSize()
    main=checkMainPotSize()
    print("Total:"+total)
    print("Main:"+main)
    checkAllCards()
    if(isOurAction()):
        print("Making Decision")
        makeDecision(total,main)
    time.sleep(1)
