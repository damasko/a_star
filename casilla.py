# -*- coding: utf-8 -*-

import pygame


class Casilla(object):

    def __init__(self, x, y):

        super(Casilla, self).__init__()

        self.rect = pygame.rect.Rect(x, y, 8, 8)
        self.estado = "D"
        self.x = 0
        self.y = 0
        self.parent = None
        self.d_man = 0
        self.g = 0
        self.f = 0
        #self.dist = 0
