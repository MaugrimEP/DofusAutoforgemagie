import time
import typing

from ItemManager import Item
from pynput.mouse import Button, Controller
import keyboard
import math
from PIL import ImageGrab
from config import *

def _proxy(function, *args, **kwargs):
	res = function(*args, **kwargs)
	time.sleep(sleep_time)
	return res

# clef, position
dico_data = {
	'searchBar': (1755, 736),
	'deleteResearch': (1889, 734),
	'first_item': (1682, 289),
	'fusion_button': (1485, 320),
	'close_level_up': (1236, 581),
	'marteau_jaune': (986, 600),
	'level_up': (986, 600),
	'line1': (1559, 390),
	'line2': (1563, 422),
	'line3': (1564, 454),
	'line4': (1562, 481),
	'line5': (1563, 511),
	'line6': (1560, 537),
	'line7': (1565, 571),
	'line8': (1561, 600),
}
# size in pixel, from the center
level_up_square_size = 16
targetLevelUpColor = (220.5576171875, 198.9970703125, 61.859375)
targetLevelUpDistanceThreshold = 100

mouse = Controller()

def searchItem(item: Item):
	positionErase = dico_data['deleteResearch']
	clic(positionErase, 1)
	position = dico_data['searchBar']
	clic(position, 1)
	enterText(item.name)
	time.sleep(2)

def selectItem(item: Item):
	position = dico_data['first_item']
	clic(position, 2)  # we double clic first item

def clic(position: typing.Tuple[int, int], nb: int):
	mouse.position = position
	_proxy(mouse.click, Button.left, nb)

def ctrlClic(position: typing.Tuple[int, int], nb: int):
	mouse.position = position
	keyboard.press('ctrl')
	mouse.click(Button.left, nb)
	# _proxy(mouse.click, Button.left, nb)
	time.sleep(1)
	keyboard.release('ctrl')


def erase():
	_proxy(keyboard.press_and_release, 'del')

def enterText(texte: str):
	_proxy(keyboard.write, texte)

def passLine(nbLine: int):
	positionLine = dico_data[f'line{nbLine}']
	ctrlClic(positionLine, 2)
	fusionButtonPosition = dico_data['fusion_button']
	clic(fusionButtonPosition, 7)

def asLevelChanged():
	px, py = dico_data['level_up']
	box = (px - level_up_square_size, py - level_up_square_size, px + level_up_square_size, py + level_up_square_size)

	image = ImageGrab.grab(box)
	r = 0
	g = 0
	b = 0
	
	for i in range(0, 2 * level_up_square_size):
		for j in range(0, 2 * level_up_square_size):
			_r, _g, _b = image.getpixel((i, j))
			r += _r
			g += _g
			b += _b

	r /= (level_up_square_size * 2)**2
	g /= (level_up_square_size * 2)**2
	b /= (level_up_square_size * 2)**2

	distance = math.sqrt((r - targetLevelUpColor[0])**2 +
	                     (g - targetLevelUpColor[1])**2 +
	                     (b - targetLevelUpColor[2])**2)
	return distance < targetLevelUpDistanceThreshold

def closeInterfaceLevel():
	positionClose = dico_data['close_level_up']
	clic(positionClose, 1)
