import unittest
from dccultivo import Predio
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestEliminarCultivo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso ejemplo similar enunciado, solo un cultivo en el predio. Todo el predio queda con "X".
        Plano 6x7, código_predio = 10.
        código_cultivo = 4.
        """

        plano = [
            [4, 4, 4, "X", "X", "X", "X"],
            [4, 4, 4, "X", "X", "X", "X"],
            [4, 4, 4, "X", "X", "X", "X"],
            [4, 4, 4, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="10", alto=6, ancho=7)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=4)
        resultado_esperado = 12

        predio_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Caso cultivo en una esquina.
        Plano 2x9, código_predio = 35.
        código_cultivo = 2.
        """

        plano = [
            ["X", "X", "X", 4, "X", "X", "X", "X", 2],
            ["X", 9, "X", 3, "X", "X", "X", "X", 2],
        ]
        predio = Predio(codigo_predio="35", alto=2, ancho=9)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=2)
        resultado_esperado = 2

        predio_esperado = [
            ["X", "X", "X", 4, "X", "X", "X", "X", "X"],
            ["X", 9, "X", 3, "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Caso múltiples cultivos complejo.
        Plano 10x10, código_predio = 65.
        código_cultivo = 0.
        """

        plano = [
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            [6, 6, "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", 9, 9, 9, "X", "X", "X", "X", "X"],
            ["X", "X", 9, 9, 9, 0, 0, 0, 0, "X"],
            ["X", "X", "X", "X", "X", 0, 0, 0, 0, "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="65", alto=10, ancho=10)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=0)
        resultado_esperado = 8

        predio_esperado = [
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            [6, 6, "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", 9, 9, 9, "X", "X", "X", "X", "X"],
            ["X", "X", 9, 9, 9, "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Caso de un cultivo en todo el predio. Predio final vacío.
        Plano 20x20, código_predio = 345.
        codigo_cultivo = 8.
        """

        plano = [[8 for _ in range(20)] for _ in range(20)]
        predio = Predio(codigo_predio="345", alto=20, ancho=20)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=8)
        resultado_esperado = 400

        predio_esperado = [["X" for _ in range(20)] for _ in range(20)]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Caso de cultivo en plano con solo una columna.
        Plano 10x1, código_predio = 41.
        codigo_cultivo = 5.
        """

        plano = [
            ["X"],
            ["X"],
            [4],
            [4],
            [0],
            [1],
            [5],
            [5],
            [5],
            ["X"],
        ]
        predio = Predio(codigo_predio="41", alto=10, ancho=1)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=5)
        resultado_esperado = 3

        predio_esperado = [
            ["X"],
            ["X"],
            [4],
            [4],
            [0],
            [1],
            ["X"],
            ["X"],
            ["X"],
            ["X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)
