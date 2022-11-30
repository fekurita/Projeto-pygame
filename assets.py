import pygame
import os
from config import CARRO1_HEIGHT, CARRO1_WIDTH, FROG_WIDTH, FROG_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
CARRO1_IMG = 'carro1_img'
CARRO1_IMG = 'carro1_img'
CARRO1re_IMG = 'carro1re_img'
CARRO1re_IMG = 'carro1re_img'
CARRO2_IMG = 'carro2_img'
CARRO2_IMG = 'carro2_img'
CARRO2re_IMG = 'carro2re_img'
CARRO2re_IMG = 'carro2re_img'
CARRO3_IMG = 'carro3_img'
CARRO3_IMG = 'carro3_img'
CARRO3re_IMG = 'carro3re_img'
CARRO3re_IMG = 'carro3re_img'
FROG_IMG = 'frog_img'
SHIP_IMG = 'ship_img'
EXPLOSION_ANIM = 'explosion_anim'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'Backgroundfinal.png')).convert()
    assets[CARRO1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro1.png')).convert_alpha()
    assets[CARRO1_IMG] = pygame.transform.scale(assets['carro1_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))
    assets[CARRO1re_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro1 ré.png')).convert_alpha()
    assets[CARRO1re_IMG] = pygame.transform.scale(assets['carro1re_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))
    assets[CARRO2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro2.png')).convert_alpha()
    assets[CARRO2_IMG] = pygame.transform.scale(assets['carro2_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))   
    assets[CARRO2re_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro2 ré.png')).convert_alpha()
    assets[CARRO2re_IMG] = pygame.transform.scale(assets['carro2re_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))
    assets[CARRO3_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro3.png')).convert_alpha()
    assets[CARRO3_IMG] = pygame.transform.scale(assets['carro3_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))
    assets[CARRO3re_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'carro3 ré.png')).convert_alpha()
    assets[CARRO3re_IMG] = pygame.transform.scale(assets['carro3re_img'], (CARRO1_WIDTH, CARRO1_HEIGHT))
    assets[FROG_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'frog1.png')).convert_alpha()
    explosion_anim = []
    for i in range(3):
        # Os arquivos de animação são numerados de 0 a 3
        filename = os.path.join(IMG_DIR, 'froganim{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSION_ANIM] = explosion_anim
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    return assets
