import time
from eyes import isOurAction
from brain import makeDecision

allCards=[[
"/BigPP/Assets/Cards/2S.png","/BigPP/Assets/Cards/3S.png",
"/BigPP/Assets/Cards/4S.png","/BigPP/Assets/Cards/5S.png",
"/BigPP/Assets/Cards/6S.png","/BigPP/Assets/Cards/7S.png",
"/BigPP/Assets/Cards/8S.png","/BigPP/Assets/Cards/9S.png",
"/BigPP/Assets/Cards/TS.png","/BigPP/Assets/Cards/JS.png",
"/BigPP/Assets/Cards/QS.png","/BigPP/Assets/Cards/KS.png",
"/BigPP/Assets/Cards/AS.png",
],
[
"/BigPP/Assets/Cards/2C.png",
"/BigPP/Assets/Cards/3C.png","/BigPP/Assets/Cards/4C.png",
"/BigPP/Assets/Cards/5C.png","/BigPP/Assets/Cards/6C.png",
"/BigPP/Assets/Cards/7C.png","/BigPP/Assets/Cards/8C.png",
"/BigPP/Assets/Cards/9C.png","/BigPP/Assets/Cards/TC.png",
"/BigPP/Assets/Cards/JC.png","/BigPP/Assets/Cards/QC.png",
"/BigPP/Assets/Cards/KC.png","/BigPP/Assets/Cards/AC.png",
],
[
"/BigPP/Assets/Cards/2H.png","/BigPP/Assets/Cards/3H.png",
"/BigPP/Assets/Cards/4H.png","/BigPP/Assets/Cards/5H.png",
"/BigPP/Assets/Cards/6H.png","/BigPP/Assets/Cards/7H.png",
"/BigPP/Assets/Cards/8H.png","/BigPP/Assets/Cards/9H.png",
"/BigPP/Assets/Cards/TH.png","/BigPP/Assets/Cards/JH.png",
"/BigPP/Assets/Cards/QH.png","/BigPP/Assets/Cards/KH.png",
"/BigPP/Assets/Cards/AH.png",
],
[
"/BigPP/Assets/Cards/2D.png",
"/BigPP/Assets/Cards/3D.png","/BigPP/Assets/Cards/4D.png",
"/BigPP/Assets/Cards/5D.png","/BigPP/Assets/Cards/6D.png",
"/BigPP/Assets/Cards/7D.png","/BigPP/Assets/Cards/8D.png",
"/BigPP/Assets/Cards/9D.png","/BigPP/Assets/Cards/TD.png",
"/BigPP/Assets/Cards/JD.png","/BigPP/Assets/Cards/QD.png",
"/BigPP/Assets/Cards/KD.png","/BigPP/Assets/Cards/AD.png",
]]

while True:
    if(isOurAction()):
        print("Making Decision")
        makeDecision()
    time.sleep(1)
