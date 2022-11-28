import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Frog, Carro, Explosion

#dicionario velocidade e local carros
ruavel = [[380,-2,WIDTH],[380,-2,WIDTH*1.5],[348,1,0],[348,1,0-WIDTH*0.5],[316,-3,WIDTH],[316,-3,WIDTH*1.5],[284,1,0],[284,1,0-WIDTH*0.5],[220,2,0],[220,2,0-WIDTH*0.5],[188,-1,WIDTH],[188,-1,WIDTH*1.5],[156,3,0],[156,3,0-WIDTH*0.5],[124,-2,WIDTH],[124,-2,WIDTH*1.5],[92,1,0],[92,1,0-WIDTH*0.5],[60,-1,WIDTH],[60,-1,WIDTH*1.5]]

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_bullets'] = all_bullets

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
        all_meteors.add(Carros)

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

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
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
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

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
