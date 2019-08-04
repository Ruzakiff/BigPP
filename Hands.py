import pyautogui
import eyes
from eyes import findImage

def fold():
	if findImage('/Users/ryan/Desktop/bigPP/Assets/Fold.png',.85):
		print("Fold Image Found")
		clickx=eyes.imageLocation[0]/2
		clicky=eyes.imageLocation[1]/2
		print("ACTION Folding")
		pyautogui.click(x=clickx,y=clicky)
		return True
	return False

def call():
	if findImage('/Users/ryan/Desktop/bigPP/Assets/Call.png',.85):
		print("Call Image Found")
		clickx=eyes.imageLocation[0]/2
		clicky=eyes.imageLocation[1]/2
		print("ACTION Calling")
		pyautogui.click(x=clickx,y=clicky)
		return True
	return False

def rebet(value):
	if findImage('/Users/ryan/Desktop/bigPP/Assets/Rebet.png',.85):
		print("Rebet Image Found")
		if findImage('/Users/ryan/Desktop/bigPP/Assets/AddAmount.png',.85):
				print("AddAmount Image Found")
				clickx=eyes.imageLocation[0]/2
				clicky=eyes.imageLocation[1]/2
				print("ACTION Adding")
				pyautogui.click(x=clickx,y=clicky)
				pyautogui.typewrite(value)
				if findImage('/Users/ryan/Desktop/bigPP/Assets/Rebet.png',.85):
					clickx=eyes.imageLocation[0]/2
					clicky=eyes.imageLocation[1]/2
					print("ACTION Rebetting")
					pyautogui.click(x=clickx,y=clicky)
					return True
	return False

def bet(value):
	if findImage('/Users/ryan/Desktop/bigPP/Assets/Bet.png',.85):
		print("Bet Image Found")
		if findImage('/Users/ryan/Desktop/bigPP/Assets/AddAmount.png',.85):
				print("AddAmount Image Found")
				clickx=eyes.imageLocation[0]/2
				clicky=eyes.imageLocation[1]/2
				print("ACTION Adding")
				pyautogui.click(x=clickx,y=clicky)
				pyautogui.typewrite(value)
				if findImage('/Users/ryan/Desktop/bigPP/Assets/Bet.png',.85):
					clickx=eyes.imageLocation[0]/2
					clicky=eyes.imageLocation[1]/2
					print("ACTION Betting")
					pyautogui.click(x=clickx,y=clicky)
					return True
	return False

def check():
	if findImage('/Users/ryan/Desktop/bigPP/Assets/Check.png',.85):
		print("Check Image Found")
		clickx=eyes.imageLocation[0]/2
		clicky=eyes.imageLocation[1]/2
		print("ACTION Checking")
		pyautogui.click(x=clickx,y=clicky)
		return True
	return False
