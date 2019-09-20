import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
from PIL import Image
import pytesseract
import time
import re
from ImgToCardObjTranslator import getListOfCardObjectsFromImages

foundCards=[[False for i in range(13)] for j in range(4)] #THIS IS CORRECT!!

allCards=[[
'/Users/ryan/Desktop/BigPP/Assets/Cards/AS.png','/Users/ryan/Desktop/BigPP/Assets/Cards/2S.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/3S.png','/Users/ryan/Desktop/BigPP/Assets/Cards/4S.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/5S.png','/Users/ryan/Desktop/BigPP/Assets/Cards/6S.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/7S.png','/Users/ryan/Desktop/BigPP/Assets/Cards/8S.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/9S.png','/Users/ryan/Desktop/BigPP/Assets/Cards/TS.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/JS.png','/Users/ryan/Desktop/BigPP/Assets/Cards/QS.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/KS.png',
],
[
'/Users/ryan/Desktop/BigPP/Assets/Cards/AC.png','/Users/ryan/Desktop/BigPP/Assets/Cards/2C.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/3C.png','/Users/ryan/Desktop/BigPP/Assets/Cards/4C.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/5C.png','/Users/ryan/Desktop/BigPP/Assets/Cards/6C.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/7C.png','/Users/ryan/Desktop/BigPP/Assets/Cards/8C.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/9C.png','/Users/ryan/Desktop/BigPP/Assets/Cards/TC.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/JC.png','/Users/ryan/Desktop/BigPP/Assets/Cards/QC.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/KC.png',
],
[
'/Users/ryan/Desktop/BigPP/Assets/Cards/AH.png','/Users/ryan/Desktop/BigPP/Assets/Cards/2H.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/3H.png','/Users/ryan/Desktop/BigPP/Assets/Cards/4H.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/5H.png','/Users/ryan/Desktop/BigPP/Assets/Cards/6H.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/7H.png','/Users/ryan/Desktop/BigPP/Assets/Cards/8H.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/9H.png','/Users/ryan/Desktop/BigPP/Assets/Cards/TH.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/JH.png','/Users/ryan/Desktop/BigPP/Assets/Cards/QH.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/KH.png',
],
[
'/Users/ryan/Desktop/BigPP/Assets/Cards/AD.png','/Users/ryan/Desktop/BigPP/Assets/Cards/2D.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/3D.png','/Users/ryan/Desktop/BigPP/Assets/Cards/4D.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/5D.png','/Users/ryan/Desktop/BigPP/Assets/Cards/6D.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/7D.png','/Users/ryan/Desktop/BigPP/Assets/Cards/8D.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/9D.png','/Users/ryan/Desktop/BigPP/Assets/Cards/TD.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/JD.png','/Users/ryan/Desktop/BigPP/Assets/Cards/QD.png',
'/Users/ryan/Desktop/BigPP/Assets/Cards/KD.png',
]]

imageLocation=[]
windowTopLeft=[]
windowBottomRight=[]
initalized=False
screen='/users/ryan/Desktop/screen.png'
screenpath=str("/users/ryan/Desktop/screen.png")
newRound=True

def initialize():
    global initalized
    global windowTopLeft
    global windowTopRight
    global windowBottomLeft
    global windowBottomRight
    initalized=False
    current=pyautogui.position()
    last=pyautogui.position()
    print("Go to TOP LEFT corner")
    stopped=False
    seconds=0
    while(seconds<2):
        current=pyautogui.position()
        print("Current Mouse Position:"+str(current[0])+","+str(current[1]))
        if(current[0]==last[0] and current[1]==last[1]):
            seconds=seconds+1
        else:
            last=current[:]
        time.sleep(1)

    windowTopLeft=list(current)
    seconds=0
    print("Go to BOTTOM RIGHT corner")
    while(seconds<2):
        current=pyautogui.position()
        print("Current Mouse Position:"+str(current[0])+","+str(current[1]))
        if(current[0]==last[0] and current[1]==last[1]):
            seconds=seconds+1
        else:
            last=current[:]
        time.sleep(1)
    windowBottomRight=current[:]
    seconds=0
    print("TopLeft:"+str(windowTopLeft[0])+","+str(windowTopLeft[1])+\
    "\nBottomRight:"+str(windowBottomRight[0])+","+str(windowBottomRight[1]))
    initalized=True
    print("DONE!")

def findImage(target,threshold):
    print(target)

    global imageLocation
    global screen
    img=cv2.imread(screenpath,0)
    img2=img.copy()
    screen=cv2.imread(target,0)
    w,h=screen.shape[::-1]
    img=img2.copy()
    # All the 6 methods for comparison in a list
	#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	           # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    method=eval("cv2.TM_CCOEFF_NORMED")
    # Apply screen Matching
    res=cv2.matchTemplate(img,screen,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

    print(max_val)
    	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    	#if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    	#top_left = min_loc
    top_left=max_loc
    bottom_right=(top_left[0]+w,top_left[1]+h)
    print(top_left)
    imageLocation=list(top_left)
    imageLocation[0]=int(imageLocation[0]+(w/2))
    imageLocation[1]=int(imageLocation[1]+(h/2))

    #cv2.rectangle(img,top_left,bottom_right,255,2)
    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(img,cmap = 'gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle("cv2.TM_SQDIFF")
    #plt.show()
    #if max_val<threshold:
    #	return False
    #else:
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    print (top_left)
    imageLocation=list(top_left)
    imageLocation[0]=int(imageLocation[0]+(w/2))
    imageLocation[1]=int(imageLocation[1]+(h/2))

    # cv2.rectangle(img,top_left, bottom_right, 255, 2)
    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(img,cmap = 'gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle("cv2.TM_SQDIFF")
    # plt.show()

    if max_val<threshold:
        return False
    else:
        return True

def readNumbers(filename):
    #cv2.imshow('image',cv2.imread(filename))
    temp=cv2.resize(cv2.imread(filename),None,fx=3,fy=3)
    #temp=cv2.GaussianBlur(temp,(11,11),0)
    #temp=cv2.medianBlur(temp,9)
    #cv2.imshow('image',temp)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    text = pytesseract.image_to_string(temp,lang='eng')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def isOurAction():
    #pyautogui.click(x=imageLocation[0]/2,y=imageLocation[1]/2)
    if findImage('/Users/ryan/Desktop/bigPP/Assets/Fold.png',.85):
        print("OURTURN Fold Image Found")
        return True
    elif findImage('/Users/ryan/Desktop/bigPP/Assets/Check.png',.85):
        print("OURTURN Raise Image Found")
        return True
    elif findImage('/Users/ryan/Desktop/bigPP/Assets/Call.png',.85):
        print("OURTURN Call Image Found")
        return True
    elif findImage('/Users/ryan/Desktop/bigPP/Assets/Rebet.png',.85):
        print("OURTURN Raise Image Found")
        return True
    elif findImage('/Users/ryan/Desktop/bigPP/Assets/AllIn.png',.85):
        print("OURTURN AllIn Image Found")
        return True
    return False


def checkAllCards(): #void, sets true all cards found, false otherwise
    for i in range(len(allCards)):
        for j in range(len(allCards[i])):
            if(findImage(allCards[i][j],.95)):
                foundCards[i][j]=True
            else:
                foundCards[i][j]=False
    getListOfCardObjectsFromImages()
            #print(allCards[i][j], end=" ")
            #print()
        #print()
        #for i in range(len(foundCards)):
        #    for j in range(len(foundCards[i])):
                #print(foundCards[i][j], end=" ")
        #print()

def findWindowEdge():
    img = Image.open("/users/ryan/desktop/screen.png")
    area = (windowTopLeft[0]*2, windowTopLeft[1]*2,windowBottomRight[0]*2, windowBottomRight[1]*2)
    cropped_img = img.crop(area)
    cropped_img.save("cropped.png")
    #cropped_img.show()

#class numReader:
txt=""
debounce=False
def checkTotalPotSize():
    global debounce
    global txt
    if(not debounce):
        debounce=True
        findWindowEdge()
        txt=readNumbers("/users/ryan/desktop/BigPP/cropped.png")
        #print(txt)
        re1='(Total)'	# Word 1
        re2='(\\s+)'	# White Space 1
        re3='(pot)'	# Word 2
        re4='(.)'	# Any Single Character 1
        re5='(\\s+)'	# White Space 2
        re6='(\\$[0-9]+(?:\\.[0-9][0-9])?)(?![\\d])'	# Dollar Amount 1
        rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)
        m = rg.search(txt)
        if m:
            word1=m.group(1)
            ws1=m.group(2)
            word2=m.group(3)
            c1=m.group(4)
            ws2=m.group(5)
            dollars1=m.group(6)
            #print ("("+word1+")"+"("+ws1+")"+"("+word2+")"+"("+c1+")"+"("+ws2+")"+"("+dollars1+")"+"\n")
            debounce=False
            return dollars1
        else:
            debounce=False
            return "INBETWEEN ROUNDS"

def checkMainPotSize():
    re1='(Main)'	# Word 1
    re2='(\\s+)'	# White Space 1
    re3='(pot)'	# Word 2
    re4='(.)'	# Any Single Character 1
    re5='(\\s+)'	# White Space 2
    re6='(\\$[0-9]+(?:\\.[0-9][0-9])?)(?![\\d])'	# Dollar Amount 1
    rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)
    m = rg.search(txt)
    if m:
        word1=m.group(1)
        ws1=m.group(2)
        word2=m.group(3)
        c1=m.group(4)
        ws2=m.group(5)
        dollars1=m.group(6)
        #print ("("+word1+")"+"("+ws1+")"+"("+word2+")"+"("+c1+")"+"("+ws2+")"+"("+dollars1+")"+"\n")
        return dollars1
    else:
        return "NO MAIN POT"

def checkStackSize():
    result=readNumbers('/users/ryan/desktop/a.png')
    #print(result)
    return result
