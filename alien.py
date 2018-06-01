import pygame
import time
import random


class alien:
    alien_no = 0
    flag = 0

    def __init__(self):
        xco = random.randint(1, 8)
        yco = random.randint(1, 2)
        self.x = (xco - 1) * 100
        self.y = (yco - 1) * 100
        self.obj = pygame.image.load("hit.png")
        self.obj = pygame.transform.scale(self.obj, (100, 100))
        self.start_time = time.time()
        alien.alien_no += 1
        # print "creating alien", self.start_time, self.x, self.y

    def __del__(self):
        pass
