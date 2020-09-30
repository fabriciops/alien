import pygame as py

class Ship():

    def __init__(self, screen):
        #Inicar espaçonave

        self.screen = screen

        #carregar imagem
        self.image = py.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #Desenha na posição atual
        self.screen.blit(self.image, self.rect)
