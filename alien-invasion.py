from setting import Setting
from ship import Ship
import game_functions as gf

import pygame as py

def run_game():

    #Iniciaza o jogo e cria um objeto para a tela
    ai_setting = Setting()
    screen = py.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    py.display.set_caption("Alien Invasion")

    #Cria uma espaçonave
    ship = Ship(ai_setting, screen)
    
    while True:
        # Event do teclado
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)

run_game()