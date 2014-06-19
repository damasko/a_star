# -*- coding: utf-8 -*-
from casilla import Casilla
#from maze import *


class Tablero(object):

    def __init__(self, tamx, tamy):

        self.existe_a = False
        self.existe_b = False
        #self.ini = None
        self.matrix = self.crea_tablero(tamx, tamy)
        #self.matrix = maze(50, 50)

    def crea_tablero(self, tamx, tamy):

        x = 2
        y = 2
        matriz = []
        for i in range(tamy):
            linea = []
            for j in range(tamx):
                casilla = Casilla(x, y)
                casilla.x = j
                casilla.y = i
                if i == 0 or j == 0 or i == tamy - 1 or j == tamx - 1:
                    casilla.estado = "P"
                linea.append(casilla)
                x += 10
            matriz.append(linea)
            x = 2
            y += 10

        return matriz

