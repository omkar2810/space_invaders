import pygame


class bullet(object):

    state = 1

    def __init__(self, x_coo, y_coo, image_url):
        self.x = x_coo
        self.y = y_coo
        self.obj = pygame.image.load(image_url)
        self.obj = pygame.transform.scale(self.obj, (100, 100))

    def __del__(self):
        print "deleting bullet"

    def update(self):
        self.y -= self.spd


class bullet1(bullet):

    def __init__(self, x_coo, y_coo, image_url, speed):
        super(bullet1, self).__init__(x_coo, y_coo, image_url)
        self.spd = speed


class bullet2(bullet):

    def __init__(self, x_coo, y_coo, image_url, speed):
        super(bullet2, self).__init__(x_coo, y_coo, image_url)
        self.spd = speed
