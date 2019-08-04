import time
from eyes import isOurAction
from eyes import checkAllCards
from brain import makeDecision


checkAllCards()
while True:
    if(isOurAction()):
        print("Making Decision")
        makeDecision()
    time.sleep(1)
