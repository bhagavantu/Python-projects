import pyautogui
import time
time.sleep(5)

distance=200

while distance > 0:

	pyautogui.dragRel(distance, 0, duration=0.5) # right
	
	pyautogui.dragRel(0,distance, duration=0.5) #down

	pyautogui.dragRel(-distance, 0, duration=0.5) # left

	
	pyautogui.dragRel(0, -distance, duration=0.5) # up

