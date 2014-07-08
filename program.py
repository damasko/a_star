# -*- coding: utf-8 -*-

import pygame
from cursor import Cursor
from tablero import Tablero
from pathfinder import PathFinder


class Program(object):

    def __init__(self):

        self.tablero = Tablero(80, 80)

        self.screen = pygame.display.set_mode((len(self.tablero.matrix[0]) * 10,
                    len(self.tablero.matrix) * 10 + 32), pygame.DOUBLEBUF)

        pygame.display.set_caption("Pathfinder")

        self.clock = pygame.time.Clock()

        self.pausa = True
        self.velocidad = 100
        self.velocidad_algoritmo = 8

        # a star
        self.pathfinder = PathFinder(self.tablero)

        # cursor
        self.cursor = Cursor(self.tablero, self.pathfinder)

        #fuente
        pygame.font.init()
        self.fuente = pygame.font.SysFont("default", 24)
        self.texto = self.fuente.render("Pausado", True, (255, 0, 255))
        self.texto_algo = self.fuente.render("Velocidad: " + str(self.velocidad_algoritmo),
                                True, (255, 0, 255))



    def draw_matriz(self):

        for linea in self.tablero.matrix:
            for casilla in linea:

                if casilla.estado == "D":

                    pygame.draw.rect(self.screen, (100, 40, 0), casilla.rect)

                elif casilla.estado == "A":

                    pygame.draw.rect(self.screen, (255, 255, 0), casilla.rect)

                elif casilla.estado == "B":

                    pygame.draw.rect(self.screen, (0, 255, 100), casilla.rect)

                else:

                    pygame.draw.rect(self.screen, (20, 170, 170), casilla.rect)

        for posibles in self.pathfinder.open_list:
            pygame.draw.rect(self.screen, (0, 0, 0), posibles.rect)

        if self.pathfinder.encontrado:
            for casillas in self.pathfinder.ruta:
                pygame.draw.rect(self.screen, (0, 255, 0), casillas.rect)
        else:
            for analizados in self.pathfinder.closed_list:
                pygame.draw.rect(self.screen, (255, 255, 240), analizados.rect)

    def execute(self):

        self.salir = False

        while not self.salir:

            self.clock.tick(self.velocidad)

            # eventos de teclado

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.salir = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pausa = True

            # submenu

            if self.pausa:
                while self.pausa:

                    self.clock.tick(self.velocidad)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.pausa = False
                            self.salir = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:

                                self.pausa = False

                            if event.key == pygame.K_2:
                                if self.velocidad_algoritmo < 30:
                                    self.velocidad_algoritmo += 1
                            if event.key == pygame.K_1:
                                if self.velocidad_algoritmo > 0:
                                    self.velocidad_algoritmo -= 1

                            if event.key == pygame.K_d:
                                if self.cursor.modo_borrar:
                                    self.cursor.modo_borrar = False
                                    self.texto = self.fuente.render("Pausado",
                                                True, (255, 0, 255))
                                else:
                                    self.cursor.modo_borrar = True
                                    self.texto = self.fuente.render("Pausado  Modo borrar paredes",
                                                True, (255, 0, 255))

                            if event.key == pygame.K_r:
                                self.tablero.matrix = self.tablero.rellenaRandom()
                                self.pathfinder.reset()
                                self.tablero.reset_ab()

                    if pygame.key.get_pressed()[pygame.K_l] and pygame.key.get_pressed()[pygame.K_n]:

                        self.tablero = Tablero(80, 80)
                        self.pathfinder = PathFinder(self.tablero)
                        self.cursor = Cursor(self.tablero, self.pathfinder)

                    #updates
                    self.cursor.update()
                    self.cursor.changeState()

                    self.texto_algo = self.fuente.render("Velocidad: " + str(self.velocidad_algoritmo),
                                True, (255, 0, 255))

                    # draws
                    self.screen.fill((0, 0, 0))
                    self.draw_matriz()
                    self.screen.blit(self.texto, (8, self.screen.get_height() - 28))
                    self.screen.blit(self.texto_algo, (self.screen.get_width() - 200,
                                 self.screen.get_height() - 28))
                    pygame.draw.rect(self.screen, (250, 0, 0), self.cursor.rect)
                    pygame.display.update()

             #pathfinder

            #self.pathfinder.run2()
            for i in range(self.velocidad_algoritmo):
                self.pathfinder.run()  # el que funciona
            # updates
            self.cursor.update()

            # draws
            self.screen.fill((0, 0, 0))
            self.draw_matriz()
            pygame.display.update()