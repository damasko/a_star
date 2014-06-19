# -*- coding: utf-8 -*-
import math
from operator import attrgetter


class PathFinder(object):

    def __init__(self, tablero):

        #elementos de A*
        self.tablero = tablero
        self.open_list = []  # lista de casillas a ser comprobadas
        self.closed_list = []  # lista de casillas que forman parte de la ruta
        self.ruta = []
        self.existe_a = False
        self.existe_b = False
        self.actual = None
        self.ini = None
        self.fin = None
        self.primera = True
        self.encontrado = False
        self.recontruye = False

    def run(self):
        # intento de implementar A*

        if self.ini is not None and self.fin is not None and not self.recontruye:

            if self.primera:

                self.actual = self.ini
                self.actual.g = 10
                self.primera = False

            if not self.encontrado:

                self.check_neight()
                self.closed_list.append(self.actual)
                self.elige_casilla()
                self.open_list.pop(0)
                #print len(self.open_list)
            else:

                self.reconstruye_ruta()
                self.recontruye = True

    def reset(self):

        self.open_list = []
        self.closed_list = []
        self.ruta = []
        self.encontrado = False
        self.actual = None
        self.primera = True
        self.recontruye = False

    def check_neight(self):

        x = 0
        y = 0
        for i in range(self.actual.y - 1, self.actual.y + 2):
            x = 0
            for j in range(self.actual.x - 1, self.actual.x + 2):

                casilla = self.tablero.matrix[i][j]
                if casilla != self.actual:

                    if casilla.estado != "P" and casilla not in self.closed_list:

                        if casilla != self.fin:
                            self.calc_valores(casilla)
                            if x == y or x + y == 4:
                                casilla.g = casilla.parent.g + 1.4
                            else:
                                casilla.g = casilla.parent.g + 1.0

                            casilla.f = casilla.d_man + casilla.g
                            if casilla not in self.open_list:

                                self.open_list.append(casilla)

                        else:

                            self.encontrado = True

                x += 1
            y += 1

    def elige_casilla(self):

        self.open_list = sorted(self.open_list, key=attrgetter("f"))
        self.actual = self.open_list[0]

    def reconstruye_ruta(self):

        #self.closed_list = sorted(self.closed_list, key=attrgetter("f"))
        casilla = self.closed_list[-1]

        while casilla != self.ini:
            self.ruta.append(casilla)
            casilla = casilla.parent

        self.open_list = []

    def calc_valores(self, celula):

        celula.parent = self.actual

        celula.d_man = (abs(celula.x - self.fin.x)
                    + abs(celula.y - self.fin.y))

        #celula.g = (abs(celula.x - self.ini.x) * 10
                    #+ abs(celula.y - self.ini.y) * 14)
        #celula.g = celula.parent.g + 10

        #print celula.f


