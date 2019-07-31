import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
ourAction=False

clickTarget=[]

template='/users/ryan/Desktop/template.png'


def findImage(target,threshold):
	print(target)
	global clickTarget
	global template
	img = cv2.imread(template,0)
	print(img)
	img2 = img.copy()
	template = cv2.imread(target,0)
	print(template)
	w, h = template.shape[::-1]

	# All the 6 methods for comparison in a list
	#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	           # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

	#for meth in methods:
	img = img2.copy()
	method = eval("cv2.TM_CCOEFF_NORMED")

	# Apply template Matching
	res = cv2.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	#if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
	#top_left = min_loc
	#else:
	print (max_val)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)

	print (top_left)
	clickTarget=list(top_left)
	clickTarget[0]=int(clickTarget[0]+(w/2))
	clickTarget[1]=int(clickTarget[1]+(h/2))

	cv2.rectangle(img,top_left, bottom_right, 255, 2)

	plt.subplot(121),plt.imshow(res,cmap = 'gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(img,cmap = 'gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.suptitle("cv2.TM_SQDIFF")
	plt.show()
	if max_val<threshold:
		return False
	else:
		top_left = max_loc
		bottom_right = (top_left[0] + w, top_left[1] + h)

		print (top_left)
		clickTarget=list(top_left)
		clickTarget[0]=int(clickTarget[0]+(w/2))
		clickTarget[1]=int(clickTarget[1]+(h/2))

		cv2.rectangle(img,top_left, bottom_right, 255, 2)

		plt.subplot(121),plt.imshow(res,cmap = 'gray')
		plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
		plt.subplot(122),plt.imshow(img,cmap = 'gray')
		plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
		plt.suptitle("cv2.TM_SQDIFF")
		#plt.show()
		return True

def isOurAction():
	if findImage('/Users/ryan/Desktop/a.png',.85):
		print("Image Found")
		ourAction=True
		pyautogui.click(x=clickTarget[0]/2,y=clickTarget[1]/2)


def main():

	pyautogui.screenshot(template)
	isOurAction()

if __name__=="__main__":
    main()
