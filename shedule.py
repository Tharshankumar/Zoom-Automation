
import schedule
import os
import time
import pyautogui
import ctypes

#Welcome
print("\nHello 👋 ,\nTo run this script You should Install the Zoom Application and your OS should be Windows\nThis tool supports only few screen Reselution and it is recomanded to keep the Screen Scale in 125%\n")


meeting_ID = input("Enter the Meeting ID : ")
password = input("If password is not there leve blanck : ")

day = input("Enter the day Eg:monday : ")
timea = input("Enter the time in HH:MM Format : ")


while meeting_ID == '':
	meeting_ID = input("Meeting ID is required to join the meeting: ")
while day == '':
	day = input("Enter the day Eg:monday : ")
while timea == '':
	timea = input("Enter the time in HH:MM Format : ")


zoom_path = os.path.join("C:/Users/"+os.getlogin()+"/AppData/Roaming/Zoom/bin/Zoom.exe")

#Screen Resolution
screen_width, screen_height = pyautogui.size()
size = f"{screen_width}_{screen_height}"

#Screen Scale
scale = ctypes.windll.shcore.GetScaleFactorForDevice(0)
scale = f'{scale}'

#Clicks
click_join1 = 'Pic/'+size+'/'+scale+'/join1.png'
click_join2 = 'Pic/'+size+'/'+scale+'/join2.png'
click_join3 = 'Pic/'+size+'/'+scale+'/pjoin.png'
click_join1A = 'Pic/'+size+'/'+scale+'/join1A.png'

def open_zoom ():
	if zoom_path :
		print("The zoom is ready to launch")
		os.startfile(zoom_path)
		time.sleep(10)
		pyautogui.hotkey("WIN" , "up")
		print("The Zoom Application has lanched sucessfully")
	else :
		print("The zoom.exe file is missing please reinstall in the default path")
		return False

def join_Meet():
		if pyautogui.locateOnScreen(click_join1):
			pyautogui.click(click_join1)
			time.sleep(4)
			pyautogui.typewrite(meeting_ID)
			time.sleep(3)
		elif pyautogui.locateOnScreen(click_join1A) :
				print("There is a meeting ongoing please end or leave the meeting to join the meeting")
				return False
		
		if pyautogui.locateOnScreen(click_join2):
			pyautogui.click(click_join2)
		else:
			print('The Meeting ID or the link does not work. please check the meeting ID or the link or there is an issue restart the zoom.exe')
			return False

def join_password():
	pyautogui.typewrite(password)
	time.sleep(8)
	pyautogui.click(click_join3)
	print("The zoom meet has started have a greate day")

def doing():
	while True:
		open_zoom()
		time.sleep(30)
		join_Meet()
		time.sleep(15)
		if password == '':
			break
		else:
			join_password()

def schedule_meeting():
	schedule.every().day.at(timea).do(doing)

schedule_meeting()

while schedule.jobs:
	schedule.run_pending()
	time.sleep(1)
	
