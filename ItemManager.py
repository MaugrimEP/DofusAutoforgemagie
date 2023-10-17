# liste de type (level, nom item)
# level étant le niveau à partir du quel on peut fm l'item
import typing
from config import *

class Item:
	def __init__(self, level: int, name: str, nLine1: int, nLine2: int):
		self.level = level
		self.name = name
		self.nLine1 = nLine1
		self.nLine2 = nLine2

	def getLines(self) -> typing.Tuple[int, int]:
		return self.nLine1, self.nLine2

	def __str__(self):
		return f"name:{self.name}, level:{self.level}, l1:{self.nLine1}, l2:{self.nLine2}"


# TO FEED
# change agi vita intel Force
items = []
with open(item_file, encoding='utf-8') as file:
	lines = file.readlines()
	for line in lines:
		print(line)
		_name, _level, _fml1, _fml2 = line.strip().split(';')
		items.append(Item(int(_level), _name, int(_fml1), int(_fml2)))

def getItem(_user_level: int) -> Item:
	item = [item for item in items[::-1]
	            if item.level <= _user_level][0]
	return item

