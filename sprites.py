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
        #se ja pode se ja pode andar...
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
        if self.rect.top < 0:
            self.rect.top = 0

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
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        # se passar da tela
        if  self.rect.right < 0 and self.speedx<0 :
            self.rect.x = WIDTH
        if  self.rect.left>WIDTH  and self.speedx> 0:
            self.rect.right = 0




# Classe que representa uma explosão de meteoro
class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets[EXPLOSION_ANIM]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
