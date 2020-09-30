import sys
import pygame as py

def check_events(ship):

    #Eventos de tecla
    for event in py.event.get():

        if event.type == py.QUIT:
            sys.exit
        
        elif event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                #move para direita
                ship.rect.centerx += 1

def update_screen(ai_setting, screen, ship):

    # atualiza / redesenha    
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    #Tela recente visível
    py.display.flip()