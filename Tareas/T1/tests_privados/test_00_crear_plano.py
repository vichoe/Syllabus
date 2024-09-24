import unittest
from dccultivo import Predio
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestCrearPlano(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_plano_4x4(self):
        """
        Plano 4x4, se verifica que se haya creado el plano normal, el de riego y
        que se retorne lo esperado
        """

        predio = Predio(codigo_predio="0", alto=4, ancho=4)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_01_plano_6x5(self):
        """
        Plano 6x5, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="1", alto=6, ancho=5)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_02_plano_12x3(self):
        """
        Plano 12x3, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="2", alto=12, ancho=3)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_03_plano_14x15(self):
        """
        Plano 14x15, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="3", alto=14, ancho=15)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)
