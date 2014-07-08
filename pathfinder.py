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
        self.para = False

        #
        self.ejecuta = True
        self.g_total = 0
        self.f_total = 0

    def reset(self):

        self.open_list = []
        self.closed_list = []
        self.ruta = []
        self.encontrado = False
        self.existe_a = False
        self.existe_b = False
        self.actual = None
        self.primera = True
        self.para = False


    def run(self):
        # intento de implementar A*

        if self.ini is not None and self.fin is not None and not self.para:

            if not self.reconstruye:
                if self.primera:

                    self.actual = self.ini
                    self.calc_valores(self.actual, self.actual.x, self.actual.y)
                    #self.actual.g = 10
                    self.primera = False

                if not self.encontrado:
                    try:
                        self.check_neight()
                    except:
                        pass

                    self.closed_list.append(self.actual)
                    if self.elige_casilla():
                        self.open_list.pop(0)
                    else:
                        print "Ninguna ruta para llegar al objetivo"

                else:

                    self.reconstruye_ruta()
                    self.para = True

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

                            if casilla not in self.open_list:
                                self.calc_valores(casilla, x, y)

                                self.open_list.append(casilla)

                        else:

                            self.encontrado = True

                x += 1
            y += 1

    def elige_casilla(self):

        if not self.open_list:
            self.encontrado = True
            self.reconstruye = True
            return False
        else:
            self.open_list = sorted(self.open_list, key=attrgetter("f"))
            self.actual = self.open_list[0]
            return True

    def reconstruye_ruta(self):
        #self.closed_list = sorted(self.closed_list, key=attrgetter("g"))
        casilla = self.closed_list[-1]
        while casilla != self.ini:

            self.ruta.append(casilla)
            casilla = casilla.parent

        self.open_list = []

    def calc_valores(self, celula, x, y):

        celula.parent = self.actual
        celula.d_man = ((abs(celula.x - self.fin.x)
                    + abs(celula.y - self.fin.y))) * 10

        if x == y or x + y == 4:

            celula.g = celula.parent.g + 14

        else:
            celula.g = celula.parent.g + 10

        celula.f = celula.d_man + celula.g

        #celula.g = (abs(celula.x - self.ini.x) * 10
                    #+ abs(celula.y - self.ini.y) * 14)
        #celula.g = celula.parent.g + 10

        #print celula.f


    def run2(self):

        # impementacion segun wikipedia, no funciona bien ya que algo se me pasa,
        # y el algoritmo no tiene "incentivo" de coger la ruta mas corta, es decir
        # falla en la prioridad de la distancia Manhattan

        if self.ini is not None and self.fin is not None:

            if self.primera:

                self.ini.g = 0
                self.open_list.append(self.ini)
                self.primera = False

            else:

                if self.open_list and not self.encontrado:
                    self.open_list = sorted(self.open_list, key=attrgetter("f"))
                    self.actual = self.open_list[0]
                    if self.actual == self.fin:

                        self.ejecuta = False
                        self.encontrado = True

                    self.open_list.pop(0)

                    self.closed_list.append(self.actual)
                    self.check_neight2()

    def check_neight2(self):

        x = 0
        y = 0

        for i in range(self.actual.y - 1, self.actual.y + 2):
            x = 0
            for j in range(self.actual.x - 1, self.actual.x + 2):

                casilla = self.tablero.matrix[i][j]
                if casilla.estado != "P":

                    g_tentativa = self.actual.g + (self.actual.g - casilla.g)

                    if casilla not in self.closed_list:

                        if x == y or x + y == 4:
                            casilla.g = self.actual.g + 14
                        else:
                            casilla.g = self.actual.g + 10
                        dist = ((abs(casilla.x - self.actual.x) +
                                abs(casilla.y - self.actual.y)))

                        g_tentativa = self.actual.g + casilla.g + dist

                        if casilla not in self.open_list or g_tentativa < self.actual.g:

                            self.ruta.append(self.actual)
                            casilla.g = g_tentativa
                            casilla.f = casilla.g + ((abs(self.ini.x - self.fin.x)
                                                + abs(self.ini.y - self.fin.y))) * 10

                            if casilla not in self.open_list:
                                self.open_list.append(casilla)

                x += 1
            y += 1


    def calc_valores2(self, celula, x, y):

        celula.parent = self.actual

        #celula.d_man = ((abs(celula.x - self.fin.x)
                    #+ abs(celula.y - self.fin.y)))*10

        if x == y or x + y == 4:
            celula.g = celula.parent.g + 14
        else:
            celula.g = celula.parent.g + 10

        #celula.f = celula.d_man + celula.g

## Muy muy lol

  #def run2(self):

        #if self.ini is not None and self.fin is not None:

            ##if self.ejecuta:
            #if self.primera:
                #print "asdas"
                #self.actual = self.ini
                #self.open_list.append(self.actual)
                #self.primera = False
            #else:

                #if not self.encontrado and self.open_list:
                    #self.open_list = sorted(self.open_list, key=attrgetter("f"))
                    #self.actual = self.open_list[0]
                    #if self.actual == self.fin:

                        #self.ejecuta = False
                        #self.encontrado = True


                    #self.open_list.pop(0)

                    #self.closed_list.append(self.actual)
                    #self.check_neight2()

    #def check_neight2(self):

        #x = 0
        #y = 0
        #for i in range(self.actual.y - 1, self.actual.y + 2):
            #x = 0
            #for j in range(self.actual.x - 1, self.actual.x + 2):

                #casilla = self.tablero.matrix[i][j]
                #if casilla.estado != "P":

                    #if casilla not in self.closed_list:

                        #g_tentativa = self.actual.g + (self.actual.g - casilla.g)

                        #if casilla not in self.open_list or g_tentativa < self.actual.g:

                            #self.ruta.append(self.actual)
                            #casilla.g = g_tentativa
                            #casilla.f = casilla.g + ((abs(self.ini.x - self.fin.x)
                                                #+ abs(self.ini.y - self.fin.y))) * 10

                            #if casilla not in self.open_list:
                                #self.open_list.append(casilla)

                #x += 1
            #y += 1


    #def calc_valores2(self, celula, x, y):

        #celula.parent = self.actual

        ##celula.d_man = ((abs(celula.x - self.fin.x)
                    ##+ abs(celula.y - self.fin.y)))*10

        #if x == y or x + y == 4:
            #celula.g = celula.parent.g + 14
        #else:
            #celula.g = celula.parent.g + 10

        ##celula.f = celula.d_man + celula.g
