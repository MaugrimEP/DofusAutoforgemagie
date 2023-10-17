import sys, os
import time

clicl1 = (1272, 244)
clicl2 = (1328, 317)
clilc4 = (1640, 619)
clicl3 = (1521, 616)
cliclprive = (1321, 289)

from pynput.mouse import Button, Controller
mouse = Controller()
import keyboard
slpt = 0.05
activated = False

while True:
        if keyboard.is_pressed('o'):
                mouse.position = clicl1
                mouse.click(Button.left)
                time.sleep(slpt)
                mouse.position = clicl2
                mouse.click(Button.left)
                time.sleep(slpt)
                mouse.position = clilc4
                mouse.click(Button.left)
                mouse.position = clicl3
                mouse.click(Button.left)


        if keyboard.is_pressed('p'):
                mouse.position = clicl1
                mouse.click(Button.left)
                time.sleep(slpt)
                mouse.position = cliclprive
                mouse.click(Button.left)
                time.sleep(slpt)
                mouse.position = clilc4
                mouse.click(Button.left)
                mouse.position = clicl3
                mouse.click(Button.left)
        time.sleep(slpt)
