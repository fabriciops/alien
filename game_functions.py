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
                ship.moving_right = True
            
            if event.key == py.K_LEFT:
                #move para direita
                ship.moving_left = True
        
        elif event.type == py.KEYUP:
            if event.key == py.K_RIGHT:
                #move para direita
                ship.moving_right = False
            
            if event.key == py.K_LEFT:
                #move para direita
                ship.moving_left = False

def update_screen(ai_setting, screen, ship):

    # atualiza / redesenha    
    screen.fill(ai_setting.bg_color)
    ship.update()

    #Tela recente visível
    py.display.flip()