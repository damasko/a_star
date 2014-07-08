# -*- coding: utf-8 -*-


import pygame


class Cursor(object):

    def __init__(self, tablero, pathfinder):

        self.rect = pygame.rect.Rect(0, 0, 6, 6)
        self.puntero = pygame.rect.Rect(0, 0, 1, 1)
        pygame.mouse.set_visible(False)
        self.modo_borrar = False
        self.tablero = tablero
        self.pathfinder = pathfinder

    def update(self):

        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.puntero.x, self.puntero.y = self.rect.centerx, self.rect.centery

    def changeState(self):

        for fila in self.tablero.matrix:
            for cell in fila:
                if pygame.mouse.get_pressed()[0]:
                    if self.puntero.colliderect(cell.rect):

                        if not self.pathfinder.existe_a:

                            if cell.estado != "B":
                                cell.estado = "A"
                                cell.g = 10
                                self.pathfinder.ini = cell
                                self.pathfinder.existe_a = True
                                self.pathfinder.encontrado = False
                                self.pathfinder.reconstruye = False

                        else:

                            if cell.estado == "A":
                                cell.estado = "D"
                                cell.g = 0
                                self.pathfinder.ini = None
                                self.pathfinder.existe_a = False
                                self.pathfinder.reset()

                if pygame.mouse.get_pressed()[2]:

                    if self.puntero.colliderect(cell.rect):

                        if not self.pathfinder.existe_b:

                            if cell.estado != "A":
                                cell.estado = "B"
                                self.pathfinder.fin = cell
                                self.pathfinder.existe_b = True
                                self.pathfinder.encontrado = False
                                self.pathfinder.reconstruye = False


                        else:

                            if cell.estado == "B":
                                cell.estado = "D"
                                self.pathfinder.fin = None
                                self.pathfinder.existe_b = False
                                self.pathfinder.reset()

                if pygame.mouse.get_pressed()[1]:

                    if self.rect.colliderect(cell.rect):
                        if cell.estado != "A" and cell.estado != "B":
                            if self.modo_borrar:
                                cell.estado = "D"
                            else:
                                cell.estado = "P"

