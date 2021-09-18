#! python3
import pywintypes
import pyautogui as pg, sys, PIL.ImageGrab, win32gui
from time import sleep
from pynput.keyboard import Key, Controller
from ahk import AHK

#Botão de procurar partida
xProcurarPartida = 856
yProcurarPartida = 841

#Botão de aceitar partida
xAceitarPartida = 943
yAceitarPartida = 727

#Coordenadas do primeiro campeão na loja
xCampeao1 = 575
yCampeao1 = 989

#Coordenada do primeiro espaço do banco
xBanco1 = 429
yBanco1 = 785

#Espaço no campo 1
xCampo1 = 609
yCampo1 = 521

#Espaço no campo 2
xCampo2 = 1206
yCampo2 = 519

#Espaço no campo 3
xCampo3 = 1356
yCampo3 = 657

#Botão de dar surrender
xClicarSurrender = 760
yClicarSurrender = 842

#Botão confirmar surrender
xConfirmarSurrender = 826
yConfirmarSurrender = 488

#Qualquer pixel que a tela do jogo cubra e que a tela do client não cubra
xPixelDesktop = 1411
yPixelDesktop = 29

#Botao de aceitar a recompensa das missões
xAceitarMissao = 978
yAceitarMissao = 850

keyboard = Controller()

ahk = AHK()

def clicarProcurarPartida():
    pg.moveTo(xProcurarPartida, yProcurarPartida, 1)
    ahk.click()
#

def clicarJogarNovamente():
    clicarProcurarPartida()
#

def clicarAceitarPartida():
    pg.moveTo(xAceitarPartida, yAceitarPartida, 1)
    ahk.click()
#

def subirNivel():
    ahk.key_press("f")
#

def comprarCampeao():
    pg.moveTo(xCampeao1, yCampeao1)
    ahk.click()
#

def moverCampeao():
    pg.moveTo(xBanco1, yBanco1, 1)
    ahk.click()
    pg.moveTo(xCampo1, yCampo1, 1)
    ahk.click()
#

def darSurrender():
    ahk.key_press("'")
    sleep(1)
    pg.moveTo(xClicarSurrender, yClicarSurrender, 1)
    ahk.click()
    sleep(1)
    pg.moveTo(xConfirmarSurrender, yConfirmarSurrender, 1)
    ahk.click()
#

def clicarAceitarMissao(nVezes=1):
        j = 0

        while(j < nVezes):
                pg.moveTo(xAceitarMissao, yAceitarMissao)
                ahk.click()
                sleep(8)
                j = j + 1
        #
#


#Salva instancia do client para que seja trazido para o foreground apos o fim do game
leagueClient = win32gui.FindWindow(0, "League of Legends")

pixelDesktop = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]
sleep(3)

try:
    while True:
        sleep(4)

        clicarProcurarPartida()

        #Enquanto a janela do jogo não abrir, continua clicando pra aceitar partida
        while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelDesktop):
            clicarAceitarPartida()
            sleep(1)
        #

        sleep(10)

        #Grava um pixel da tela de load
        pixelTelaLoad = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]

        #Compara o pixel gravado da tela de load com o pixel atual do mesmo lugar, para detectar quando o jogo começar
        while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelTelaLoad):
            pass
        #

        #Timer de 10 minutos para dar surrender
        #Realiza e realiza ações para fugir da detecção de afk
        x = 660
        while (x > 0):
            x = x - 1
            sleep(1)

            if(x==595):
                comprarCampeao()
                moverCampeao()
            #

            if(x==340):
                subirNivel()
                comprarCampeao()
            #

            if(x==244):
                subirNivel()
                comprarCampeao()
            #

            if(x==200):
                subirNivel()
                comprarCampeao()
            #

            if(x == 60):
                subirNivel()
            #            
        #

        darSurrender()

        sleep(10)

        clicarAceitarMissao(2)

        clicarJogarNovamente()

except KeyboardInterrupt:
    print('\n')
#