#! usr/bin/env Python3

import pygame
import pygame.image
from pygame.locals import *
from random import randrange

pygame.init()
pygame.display.set_caption("PyCamp")
camp_logo = pygame.image.load('img/camp_logo.png')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 540), 0, 32)

danger_green = pygame.image.load('img/danger_green.png').convert_alpha()
danger_yellow = pygame.image.load('img/danger_yellow.png').convert_alpha()
danger_red = pygame.image.load('img/danger_red.png').convert_alpha()
danger_black = pygame.image.load('img/danger_black.png').convert_alpha()
die_screen = pygame.image.load('img/die_screen.png').convert_alpha()

bg = pygame.image.load('img/bg.png').convert_alpha()
fundo = pygame.image.load('img/fin.png').convert_alpha()
selector = pygame.image.load('img/selector.png').convert_alpha()
selection2 = pygame.image.load('img/selection2.png').convert_alpha()
selector_position = [238, 11]
fundo_position = [-100, 0]

floor = dict(surface=pygame.image.load("img/floor.png").convert_alpha(), x=[238, 303, 368, 433, 498, 563, 628, 693],
             y=[11, 76, 141, 206, 271, 336, 401, 466])

explosao = {
    'surface': pygame.image.load('img/explosao.png').convert_alpha(),
    'rect': Rect(0, 0, 65, 65)
}

select = {
    'surface': pygame.image.load('img/mode.png').convert_alpha(),
    'position': (340, 360)
}

lista = [(303, 11), (368, 76), (238, 141), (433, 141), (303, 206), (498, 206), (563, 206), (368, 271), (628, 271),
         (433, 336), (498, 336), (693, 336), (563, 401), (628, 466), (303, 76), (563, 141), (628, 141), (238, 206),
         (628, 206), (303, 271), (433, 271), (693, 271), (238, 401), (368, 401), (498, 401), (368, 466), (693, 76),
         (368, 141), (498, 141), (693, 206), (563, 271), (303, 336), (563, 336), (303, 401), (498, 466), (368, 11),
         (433, 76), (563, 76), (303, 141), (693, 141), (433, 206), (368, 336), (693, 401), (433, 11), (238, 76),
         (628, 401)]

selection = pygame.image.load('img/star.png').convert_alpha()
sel_position = [390, 376]
tank = {
    'surface': pygame.image.load('img/tank2.png'),
    'position': [238, 11],
    'rotate': 180,
    'speed': 1,
    'stat': 0
}

life = {
    'surface': pygame.image.load('img/life.png').convert_alpha(),
    'position': (72, 20),
    'rect': Rect(0, 0, 96, 27)
}
life_die = pygame.image.load('img/die_life.png').convert_alpha()


def camp():
    x = 0
    y = 0
    for ind in range(1, 65):
        screen.blit(floor['surface'], (floor['x'][x], floor['y'][y]))
        x += 1
        if x == 8:
            y += 1
            x = 0


def bang():
    pygame.mixer.music.load('sons/explosion.mp3')
    pygame.mixer.music.play(0, 0)


def pause_func() -> object:
    pause = pygame.image.load('img/screen_pause.png').convert_alpha()
    screen.blit(pause, (300, 20))


padrao = [()]


def padrao_normal(padrao, para):
    if para == 0:
        for i in range(0, 12):
            padrao[i] = lista[randrange(0, 45)]
    if para == 1:
        for i in range(0, 20):
            padrao[i] = lista[randrange(0, 45)]

noBombOne = [(303, 11), (303, 76), (238, 76)]
noBombTwo = [(628, 466), (628, 401), (694, 401)]
sel_position2 = [340, 273]
direction = [0, 0, 0, 0]
die_position = [(0, 0), (0, 0), (0, 0)]

sel_position3 = [403, 293]
start = 0
player = 0
close_pad = 0
ok = 0
cod_boom = 0
fim = 0
x_position = 0
i = 1
num_die = 0
selec = 0
cont = 1
pos_fim = 0
win = 0
paused = False
mode = 0


while True:
    time_passed = clock.tick(30)
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    if start == 0:
        fundo_position[0] -= 0.9
        f = fundo_position[0]

        t = sel_position[0]
        screen.blit(fundo, fundo_position)
        screen.blit(camp_logo, (180, 70))
        screen.blit(select['surface'], (select['position'][0], select['position'][1]))
        screen.blit(selection, sel_position)

        if pressed_keys[K_DOWN]:
            if sel_position[1] == 376:
                sel_position[0] = 310
                sel_position[1] += 35
                player = 0
                selec = 1
        if pressed_keys[K_UP]:
            if sel_position[1] == 411:
                sel_position[0] = 390
                sel_position[1] -= 35
                player = 1
                selec = 0

        if selec == 0:
            if sel_position[0] < 400:
                sel_position[0] += 2
        else:
            if sel_position[0] < 322:
                sel_position[0] += 1

        if pressed_keys[K_SPACE]:
            start = 1
            if sel_position[1] == 376:
                mode = 0
            else:
                mode = 1
        if f <= -1800:
            fundo_position[0] = -2

    if start == 1:
        if num_die == 0 and mode == 0:
            if close_pad == 0:
                padrao = [()] * 12
                padrao_normal(padrao, para=0)
            if(noBombOne in padrao) or (noBombOne[0] and noBombOne[2] in padrao) or (noBombTwo in padrao):
                close_pad = 0
                padrao = [()] * 36
                padrao_normal(padrao, para=1)
            close_pad += 1
        elif num_die == 0 and mode == 1:
            if close_pad == 0:
                padrao = [()] * 20
                padrao_normal(padrao, para=1)
            if (noBombOne in padrao) or (noBombOne[0] and noBombOne[2] in padrao) or (noBombTwo in padrao):
                close_pad = 0
                padrao = [()] * 20
                padrao_normal(padrao, para=1)
            close_pad += 1
        screen.blit(bg, (0, 0))
        camp()
        if num_die != 0:
            if die_position[0] != (0, 0):
                screen.blit(pygame.image.load('img/floor_explosion.png'), (die_position[0]))
                life['rect'][2] = 64
            if die_position[1] != (0, 0):
                screen.blit(pygame.image.load('img/floor_explosion.png'), (die_position[1]))
                life['rect'][2] = 32
            if die_position[2] != (0, 0):
                screen.blit(pygame.image.load('img/floor_explosion.png'), (die_position[2]))
                life['rect'][2] = 0
        if (pressed_keys[K_SPACE] or pressed_keys[K_d]) and fim == 0 and not paused:
            ok = 1
        if close_pad == 1:
            close_pad += 1
        r = tank['rotate']
        t = tank['position'][0]
        s = tank['position'][1]
        tank_position = (t, s)
        pd = tank['position'][0] + 65, tank['position'][1]
        pe = tank['position'][0] - 65, tank['position'][1]
        pc = tank['position'][0], tank['position'][1] - 65
        pb = tank['position'][0], tank['position'][1] + 65

        if ok == 1:
            selector = pygame.image.load('img/ok.png').convert_alpha()
        else:
            selector = pygame.image.load('img/selector.png').convert_alpha()

        if tank['position'] != selector_position and fim != 1:
            screen.blit(selector, selector_position)

        if pressed_keys[K_UP] and ok == 0 and s >= 76 and fim != 1 and not paused:
            selector_position[1] = tank['position'][1] - 65
            selector_position[0] = tank['position'][0]
            direction = [1, 0, 0, 0]
        elif pressed_keys[K_DOWN] and ok == 0 and s <= 401 and fim != 1 and not paused:
            selector_position[1] = tank['position'][1] + 65
            selector_position[0] = tank['position'][0]
            direction = [0, 1, 0, 0]

        if pressed_keys[K_LEFT] and ok == 0 and t >= 303 and fim != 1 and not paused:
            selector_position[0] = tank['position'][0] - 65
            selector_position[1] = tank['position'][1]
            direction = [0, 0, 1, 0]
        elif pressed_keys[K_RIGHT] and ok == 0 and t <= 628 and fim != 1 and not paused:
            selector_position[0] = tank['position'][0] + 65
            selector_position[1] = tank['position'][1]
            direction = [0, 0, 0, 1]

        if direction[0] == 1 and ok == 1:
            tank['position'][1] -= tank['speed']
            tank['rotate'] = 360

        if direction[1] == 1 and ok == 1:
            tank['position'][1] += tank['speed']
            tank['rotate'] = 180

        if direction[2] == 1 and ok == 1:
            tank['position'][0] -= tank['speed']
            tank['rotate'] = 90

        if direction[3] == 1 and ok == 1:
            tank['position'][0] += tank['speed']
            tank['rotate'] = 272

        if tank['position'] == selector_position:
            direction = [0, 0, 0, 0]
            ok = 0
            free = 0

        if pressed_keys[K_SPACE] and tank['position'] == selector_position and not paused:
            if (pd in padrao and pb in padrao) or (pc in padrao and pe in padrao) or (
                            pb in padrao and pe in padrao) or (pc in padrao and pd in padrao):
                screen.blit(danger_black, (tank['position']))
            elif (pe in padrao) or (pd in padrao):
                screen.blit(danger_red, (tank['position']))
            elif (pb in padrao) or (pc in padrao):
                screen.blit(danger_yellow, (tank['position']))
            else:
                screen.blit(danger_green, (tank['position']))

        screen.blit(pygame.transform.rotate(tank['surface'], (tank['rotate'])),
                    (tank['position'][0], tank['position'][1]))
        screen.blit(pygame.image.load('img/painel.png'), (10, 0))
        screen.blit(life_die, (life['position']))
        screen.blit(life['surface'], (life['position']), (life['rect']))

        if pressed_keys[K_p] and direction == [0, 0, 0, 0]:
            paused = True

        if paused == 1 and direction == [0, 0, 0, 0]:
            pause_func()
            if pressed_keys[K_1]:
                paused = 0
            elif pressed_keys[K_2]:
                start = 0
                paused = 0
                num_die = 0
                close_pad = 0
                fim = 0
                win = 0
                cont = 0
                pos_fim = 0
                close_pad = 0
                tank['position'] = [238, 11]
                selector_position = [238, 11]
                tank['rotate'] = 180
                die_position = [(0, 0), (0, 0), (0, 0)]
                num_die = 0
                i = 1
                cod_boom = 0
                explosao['rect'] = [0, 0, 65, 65]
                x_position = 0
                life['rect'][2] = 96
            elif pressed_keys[K_3]:
                pygame.quit()
                exit(0)

        if tank_position in padrao:
            if num_die == 3:
                fim = 1

            if x_position < 3 and i == 1:
                die_position[x_position] = tank_position
                i += 1
                x_position += 1
                num_die += 1
                bang()

            if cod_boom <= 11:
                screen.blit(explosao['surface'], tank_position, explosao['rect'])
                explosao['rect'][0] += 66
                cod_boom += 1

            if num_die < 3 and cod_boom == 11:
                i = 1
                tank['position'] = [238, 11]
                tank['rotate'] = 180
                selector_position = [238, 11]
                cod_boom = 0
                explosao['rect'] = [0, 0, 65, 65]

        if (tank['position'] == [693, 466]) and (num_die < 3):
            pos_fim = 1
            if tank['rotate'] != 272:
                tank['rotate'] = 272
        if (pos_fim == 1) and (cont < 130):
            tank['position'][0] += tank['speed']
            cont += 1

        if tank['position'][0] > 693:
            fim = 1
            win = 1

        if fim == 1:
            free = 1
            if win == 1:
                screen.blit(pygame.image.load('img/win_screen.png'), (250, 150))
                screen.blit(pygame.image.load('img/star.png'), sel_position2)
                win = 0
            else:
                screen.blit(die_screen, (250, 150))
                screen.blit(pygame.image.load('img/star.png'), sel_position2)

            if pressed_keys[K_SPACE] and sel_position2[1] == 273:
                fim = 0
                win = 0
                cont = 0
                pos_fim = 0
                close_pad = 0
                tank['position'] = [238, 11]
                selector_position = [238, 11]
                tank['rotate'] = 180
                die_position = [(0, 0), (0, 0), (0, 0)]
                num_die = 0
                i = 1
                cod_boom = 0
                explosao['rect'] = [0, 0, 65, 65]
                x_position = 0
                life['rect'][2] = 96
            elif pressed_keys[K_SPACE] and sel_position2[1] != 275:
                pygame.quit()
                exit(0)

            if pressed_keys[K_DOWN]:
                if sel_position2[1] == 273:
                    sel_position2[1] += 25
                    sel_position2[0] += 60

            if pressed_keys[K_UP]:
                if sel_position2[1] != 273:
                    sel_position2[1] -= 25
                    sel_position2[0] -= 60

            sel_position2[0] += 1

            if sel_position2[0] == 350 and sel_position2[1] == 273:
                sel_position2[0] = 340
            elif sel_position2[0] == 410 and sel_position2[1] == 298:
                sel_position2[0] = 400

    pygame.display.update()
