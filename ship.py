import pygame as py

class Ship():

    def __init__(self, ai_setting, screen):
        #Inicar espaçonave

        self.screen = screen
        self.ai_setting = ai_setting

        #carregar imagem
        self.image = py.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #acrescenta um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        #flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        
        #Configurações = ai_setting atributo que há em configurações = ship_speed_factor
        #Atualiza a posição da nave de acordo com a flag de movimento
        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor
        
        #Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        #Desenha na posição atual
        self.screen.blit(self.image, self.rect)
    
    
