import sys
from setting import Setting

import pygame as py

def run_game():

    #Iniciaza o jogo e cria um objeto para a tela
    ai_setting = Setting()
    screen = py.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))

    while True:
        # Event do teclado
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit

        screen.fill(ai_setting.bg_color)

        #Tela recente visível
        py.display.flip()

run_game()