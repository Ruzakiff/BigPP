import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui

allCards=[[
"/BigPP/Assets/Cards/AS.png","/BigPP/Assets/Cards/2S.png",
"/BigPP/Assets/Cards/3S.png","/BigPP/Assets/Cards/4S.png",
"/BigPP/Assets/Cards/5S.png","/BigPP/Assets/Cards/6S.png",
"/BigPP/Assets/Cards/7S.png","/BigPP/Assets/Cards/8S.png",
"/BigPP/Assets/Cards/9S.png","/BigPP/Assets/Cards/TS.png",
"/BigPP/Assets/Cards/JS.png","/BigPP/Assets/Cards/QS.png",
"/BigPP/Assets/Cards/KS.png",
],
[
"/BigPP/Assets/Cards/AC.png","/BigPP/Assets/Cards/2C.png",
"/BigPP/Assets/Cards/3C.png","/BigPP/Assets/Cards/4C.png",
"/BigPP/Assets/Cards/5C.png","/BigPP/Assets/Cards/6C.png",
"/BigPP/Assets/Cards/7C.png","/BigPP/Assets/Cards/8C.png",
"/BigPP/Assets/Cards/9C.png","/BigPP/Assets/Cards/TC.png",
"/BigPP/Assets/Cards/JC.png","/BigPP/Assets/Cards/QC.png",
"/BigPP/Assets/Cards/KC.png",
],
[
"/BigPP/Assets/Cards/AH.png","/BigPP/Assets/Cards/2H.png",
"/BigPP/Assets/Cards/3H.png","/BigPP/Assets/Cards/4H.png",
"/BigPP/Assets/Cards/5H.png","/BigPP/Assets/Cards/6H.png",
"/BigPP/Assets/Cards/7H.png","/BigPP/Assets/Cards/8H.png",
"/BigPP/Assets/Cards/9H.png","/BigPP/Assets/Cards/TH.png",
"/BigPP/Assets/Cards/JH.png","/BigPP/Assets/Cards/QH.png",
"/BigPP/Assets/Cards/KH.png",
],
[
"/BigPP/Assets/Cards/AD.png","/BigPP/Assets/Cards/2D.png",
"/BigPP/Assets/Cards/3D.png","/BigPP/Assets/Cards/4D.png",
"/BigPP/Assets/Cards/5D.png","/BigPP/Assets/Cards/6D.png",
"/BigPP/Assets/Cards/7D.png","/BigPP/Assets/Cards/8D.png",
"/BigPP/Assets/Cards/9D.png","/BigPP/Assets/Cards/TD.png",
"/BigPP/Assets/Cards/JD.png","/BigPP/Assets/Cards/QD.png",
"/BigPP/Assets/Cards/KD.png",
]]

imageLocation=[]

screen='/users/ryan/Desktop/screen.png'
screenpath=str("/users/ryan/Desktop/screen.png")

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

    cv2.rectangle(img,top_left,bottom_right,255,2)

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

    #cv2.rectangle(img,top_left, bottom_right, 255, 2)
    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(img,cmap = 'gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle("cv2.TM_SQDIFF")
    #plt.show()
    if max_val<threshold:
        return False
    else:
        return True

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
            print(allCards[i][j], end=' ')
    print()

# def main():
# 	pyautogui.screenshot(template)
# 	isOurAction()
#
# if __name__=="__main__":
#     main()
