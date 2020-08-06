import time
import threading
from pynput import mouse, keyboard


delay = 0.001 #seconds
button = mouse.Button.left
pKey = keyboard.Key.space #key to press
#Need to implement dynamically to only take one one key for both mouse and keyboard
start_stop_key = keyboard.Key.f8 #main key to start and stop the action
exitKey = keyboard.Key.esc
posKey = keyboard.Key.f2

print('Start/Stop Key: F8')
print('End Program: Esc')



#class to create the mouse thread object
class ClickPress(threading.Thread):
	#inherits from threading
	def __init__(self, delay, button, pKey):
		super(ClickPress, self).__init__()
		self.delay = delay
		self.button = button
		self.pKey = pKey
		self.running = False
		self.program_running = True

	def startClicking(self):
		self.running = True

	def stopClicking(self):
		self.running = False

	def exit(self):
		self.stopClicking()
		self.program_running = False
		
	def keyPress(self):
		keyboardPresser.press(self.pKey)
	
	def mouseClick(self):
		mouseClicker.click(self.button)

	def run(self):
		action = self.mouseClick # Controls if its a mouse blick or key click
		while self.program_running:
			while self.running:
				action()
				time.sleep(self.delay)
			time.sleep(0.1)


mouseClicker = mouse.Controller()
keyboardPresser = keyboard.Controller()
actionThread = ClickPress(delay, button, pKey)
actionThread.start()


#when a key is pressed on the keyboard does whats inside
def on_press(key):
	if key == start_stop_key:
		if actionThread.running:
			actionThread.stopClicking()
		else:
			actionThread.startClicking()
	elif key == exitKey:
		actionThread.exit()
		listener.stop()


#Calls the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()