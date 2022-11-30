import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, GREEN
from assets import load_assets, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Frog, Carro
import time

#dicionario velocidade e local carros
ruavel = [[380,-2,WIDTH],[380,-2,WIDTH*1.5],[348,1,0],[348,1,0-WIDTH*0.5],[316,-3,WIDTH],[316,-3,WIDTH*1.5],[284,1,0],[284,1,0-WIDTH*0.5],[220,2,0],[220,2,0-WIDTH*0.5],[188,-1,WIDTH],[188,-1,WIDTH*1.5],[156,3,0],[156,3,0-WIDTH*0.5],[124,-2,WIDTH],[124,-2,WIDTH*1.5],[92,1,0],[92,1,0-WIDTH*0.5],[60,-1,WIDTH],[60,-1,WIDTH*1.5]]

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de carros
    all_sprites = pygame.sprite.Group()
    all_carros = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_carros'] = all_carros

    # Criando o jogador
    player = Frog(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    for coord in ruavel:
        rua = coord[0]
        vel = coord[1]
        ini = coord[2]
        Carros = Carro(assets,rua,vel,ini)
        all_sprites.add(Carros)
        all_carros.add(Carros)

    DONE = 0
    PLAYING = 1
    DYING = 2
    state = PLAYING

    keys_down = {}
    Ymax = 435
    T = False
    score = 0
    lives = 3
    placar = False

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.anda(-32,0)
                    if event.key == pygame.K_RIGHT:
                        player.anda(32,0)
                    if event.key == pygame.K_UP:
                        player.anda(0,-32)
                    if event.key == pygame.K_DOWN:
                        player.anda(0,32)
                # Verifica se soltou alguma tecla.
                
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos carros
        all_sprites.update()

        if state == PLAYING:
            #score do jogo
            if Ymax == 435 and player.rect.y<435:
                Ymax = player.rect.y
                score +=1000
            if Ymax == -13:
                if player.rect.y==19:
                    T = False
                if player.rect.y == 435:
                    Ymax = 435
            if Ymax<435:
                if player.rect.y<Ymax:
                    Ymax = player.rect.y
                    score +=1000
            # Verifica se houve colisão entre carro e sapo
            hits = pygame.sprite.spritecollide(player, all_carros, False, pygame.sprite.collide_mask)
            if len(hits) > 0:
                player.kill()
                lives -= 1
                Ymax = 435
                score -=200
                state = DYING
                keys_down = {}
                dying_tick = pygame.time.get_ticks()
                dying_duration =500
        elif state == DYING:
            now = pygame.time.get_ticks()
            if now - dying_tick > dying_duration:
                if lives <= 0:
                    state = DONE
                    placar = True
                else:
                    state = PLAYING
                    player = Frog(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        if placar == True:
            text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, GREEN)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  HEIGHT/2)
            window.blit(text_surface, text_rect)
            pygame.display.update()
            time.sleep(3)
        
        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
