#! python3
import pywintypes
import pyautogui as pg, sys, PIL.ImageGrab, win32gui
from time import sleep
from pynput.keyboard import Key, Controller
from ahk import AHK

#xMouse = 425
#yMouse = 266

#Em cima da carta
xCima = 328
yCima = 173

#embaixo
xBaixo = 634
yBaixo = 612

#botão salvar
xSalvar = 583
ySalvar = 638

keyboard = Controller()

ahk =  AHK()

def printarCartas():
    x=8

    while (x > 0):
        x = x - 1
        ahk.mouseClickDrag, L, 328, 173, 634, 612
        keyboard.press("PRTSC")
    #

printarCartas()