import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui

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

		#pyautogui.click(x=imageLocation[0]/2,y=imageLocation[1]/2)
    ##move this above in implementation    return True


# def main():
# 	pyautogui.screenshot(template)
# 	isOurAction()
#
# if __name__=="__main__":
#     main()
