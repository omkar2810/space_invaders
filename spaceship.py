import pygame


class space:

    def __init__(self, url, size, x_co, y_co):

        self.spaceship = pygame.image.load("ui.png")
        self.spaceship = pygame.transform.scale(self.spaceship, size)
        self.spaceship_left = x_co
        self.spaceship_right = y_co
