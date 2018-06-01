import pygame
import time
from alien import *
from bullet import *
from spaceship import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 50)
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

running = True
score = 0
bullet_list = []

ship = space("ui.png", (100, 100), 400, 700)
cur_alien = alien()
new_alien = alien()
creation_time = time.time()

while running:                       # main game loop

    screen.fill((0, 0, 0))
    screen.blit(ship.spaceship, (ship.spaceship_left, ship.spaceship_right))
    score_update = 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                if(ship.spaceship_left >= 50):
                    ship.spaceship_left -= 100

            elif event.key == pygame.K_d:
                if ship.spaceship_left <= 650:
                    ship.spaceship_left += 100

            elif event.key == pygame.K_SPACE:
                bullet_list.append(
                    bullet1(ship.spaceship_left, ship.spaceship_right - 50, "re.png", 2))

            elif event.key == pygame.K_s:
                bullet_list.append(
                    bullet2(ship.spaceship_left, ship.spaceship_right - 50, "blue.png", 4))

            elif event.key == pygame.K_q:
                running = False

    if time.time() - creation_time >= 10:
        cur_alien = alien()
        creation_time = time.time()

    if alien.alien_no > 0:
        if (time.time() - cur_alien.start_time > 8):
            alien.alien_no -= 1

        else:
            screen.blit(cur_alien.obj, (cur_alien.x, cur_alien.y))

    if alien.flag == 1:

        if time.time() - new_alien.start_time > 5:
            alien.flag = 0
        else:
            screen.blit(new_alien.obj, (new_alien.x, new_alien.y))

    for j in range(len(bullet_list)):

        i = bullet_list[j - 1]
        i.update()

        if(i.y < 0):
            del bullet_list[j - 1]
        else:
            for i in bullet_list:
                screen.blit(i.obj, (i.x, i.y))

    if alien.alien_no > 0:

        for i in bullet_list:

            if abs(i.x - cur_alien.x) <= 50 and abs(i.y - cur_alien.y) <= 50:

                if i.spd == 2:

                    alien.alien_no -= 1
                    if score_update:
                        score = score + 1
                        flag = 1

                elif i.spd == 4:

                    new_alien = alien()
                    new_alien.x = cur_alien.x
                    new_alien.y = cur_alien.y
                    new_alien.obj = pygame.image.load("jire.png")
                    new_alien.obj = pygame.transform.scale(
                        new_alien.obj, (100, 100))
                    alien.alien_no = 0
                    alien.flag = 1

    if alien.flag == 1:

        for i in bullet_list:
            if abs(i.x - new_alien.x) <= 50 and abs(i.y - new_alien.y) <= 50:

                if i.spd == 2:
                    alien.flag = 0
                    if score_update:
                        score = score + 1

    scoretext = myfont.render(
        "Score {0}".format(score), False, (255, 255, 255))
    screen.blit(scoretext, (300, 400))
    pygame.display.update()
    clock.tick(50)
