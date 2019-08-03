import pyautogui
import schedule
import datetime

screen='/users/ryan/Desktop/screen.png'

def getScreen():
	pyautogui.screenshot(screen)
	print ("Screen Updated:",datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))

schedule.every(1).second.do(getScreen)
while 1:
	schedule.run_pending()
