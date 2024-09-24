import unittest
from dccultivo import Predio
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestRegar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_3x3(self):
        """
        Se crea un plano de riego 3x3, se riega al centro con área 1 y
        se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="0", alto=3, ancho=3)
        predio.plano_riego = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        resultado_estudiante = predio.regar(coordenadas=[1, 1], area=1)

        resultado_esperado = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test_01_5x5_dos_riegos_sucesivos(self):
        """
        Se crea una plano de riego 5x5, se riega en (3,2) con área 2, en (4,2) con área 1 y
        se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="2", alto=5, ancho=5)
        predio.plano_riego = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[3, 2], area=2)
        resultado_estudiante_final = predio.regar(coordenadas=[4, 2], area=1)

        resultado_esperado = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 2, 2, 2, 1],
        ]
        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test_02_varios_riegos_sucesivos(self):
        """
        Sea crea un plano de riego 8x6, se prueban riegos sucesivos en distintos lugares
        con distintas áreas  y se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="3", alto=8, ancho=6)
        predio.plano_riego = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[2, 4], area=2)
        predio.regar(coordenadas=[3, 2], area=3)
        predio.regar(coordenadas=[5, 4], area=1)
        resultado_estudiante_final = predio.regar(coordenadas=[0, 0], area=2)

        resultado_esperado = [
            [2, 2, 2, 2, 2, 1],
            [2, 2, 3, 2, 2, 2],
            [2, 2, 2, 2, 2, 2],
            [1, 1, 2, 2, 2, 2],
            [1, 1, 1, 2, 3, 2],
            [1, 1, 1, 2, 2, 2],
            [1, 1, 1, 1, 2, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test_03_varios_riegos_sucesivos_2(self):
        """
        Sea crea un plano de riego 12x14, se prueban riegos sucesivos en distintos lugares
        con distintas áreas y se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="3", alto=12, ancho=14)
        predio.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[8, 2], area=1)
        predio.regar(coordenadas=[2, 3], area=2)
        predio.regar(coordenadas=[7, 2], area=4)
        predio.regar(coordenadas=[10, 10], area=4)
        predio.regar(coordenadas=[12, 0], area=2)
        resultado_estudiante_final = predio.regar(coordenadas=[2, 6], area=3)

        resultado_esperado = [
            [0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 2, 2, 3, 3, 3, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 2, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)
