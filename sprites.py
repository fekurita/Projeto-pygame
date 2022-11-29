import random
import pygame
from config import WIDTH, HEIGHT
from assets import FROG_IMG,CARRO1_IMG,CARRO2_IMG,CARRO3_IMG, EXPLOSION_ANIM


class Frog(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FROG_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT 
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        #Só pode se mexer a cada 100 ms
        self.last_move = pygame.time.get_ticks()
        self.move_ticks = 150

    def anda(self,speedx,speedy):
        #Verifica se já pode andar
        now=pygame.time.get_ticks()
        elapsed_ticks = now-self.last_move
        #se ja pode andar...
        if elapsed_ticks>self.move_ticks:
            #marca tick da nova imagem
            self.last_move=now
            self.rect.x += speedx
            self.rect.y += speedy
       

    def update(self):

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom < 10:
            self.rect.bottom  = HEIGHT

class Carro(pygame.sprite.Sprite):
    def __init__(self, assets,rua,vel,ini):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        if vel ==1 or vel ==-1:
            self.image = assets[CARRO1_IMG]
        if vel ==2 or vel ==-2:
            self.image = assets[CARRO2_IMG]
        if vel == 3 or vel == -3:
            self.image = assets[CARRO3_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = ini
        self.rect.y = rua
        self.speedx = vel

    def update(self):
        # Atualizando a posição do carro
        self.rect.x += self.speedx
        # se passar da tela
        if  self.rect.right < 0 and self.speedx<0 :
            self.rect.x = WIDTH
        if  self.rect.left>WIDTH  and self.speedx> 0:
            self.rect.right = 0
