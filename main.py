import time

import keyboard

from ItemManager import getItem
from InterfaceManager import searchItem, selectItem, passLine, asLevelChanged, closeInterfaceLevel

from config import *

# TODO pas oublier de rajouter les sleep

def onLevelChanged():
	# close the interface
	closeInterfaceLevel()


levelAsChange = True
item = None
disable = True


while user_level != 200:

	if keyboard.is_pressed('alt') and keyboard.is_pressed('p'):
		print("disabled")
		disable = True

	elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):
		print("enabled")
		disable = False

	if disable:
		print("disabled continue")
		time.sleep(1)
		continue

	if levelAsChange:
		next_item = getItem(user_level)
		if item is None or next_item.name != item.name:
			item = next_item
			searchItem(item)
			selectItem(item)
		levelAsChange = False

	passLine(item.nLine1)
	passLine(item.nLine2)

	time.sleep(sleep_time)

	levelAsChange = asLevelChanged()
	if levelAsChange:
		onLevelChanged()
		user_level += 1

