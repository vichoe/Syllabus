import unittest
from dccultivo import Predio, DCCultivo
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestBuscarYPlantarFacil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Ejemplo básico similar del enunciado parte 1. Solo un predio en self.predios.
        plano_1 6x7, código_predio = 21.
        codigo_cultivo = 2, dimensiones 2x2.
        """
        plano_1 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_1 = Predio(codigo_predio="21", alto=6, ancho=7)
        predio_1.plano = plano_1

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_1]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=2, alto=2, ancho=2
        )
        resultado_esperado = True

        plano_1_esperado = [
            [2, 2, "X", "X", "X", "X", "X"],
            [2, 2, "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_1_esperado = Predio(codigo_predio="21", alto=6, ancho=7)
        predio_1_esperado.plano = plano_1_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_1_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Ejemplo básico similar del enunciado parte 2. Dos predios en self.predios.
        plano_7 5x7, código_predio = 7.
        plano_3 7x8, código_predio = 3.
        codigo_cultivo = 9, dimensiones 2x3.
        """
        plano_7 = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_7 = Predio(codigo_predio="7", alto=5, ancho=7)
        predio_7.plano = plano_7

        plano_3 = [
            ["X", "X", 4, 4, "X", "X", 7, 7],
            ["X", "X", 4, 4, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            [1, "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, 5, 5, "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3 = Predio(codigo_predio="3", alto=7, ancho=8)
        predio_3.plano = plano_3

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_7, predio_3]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=9, alto=2, ancho=3
        )
        resultado_esperado = True

        plano_7_esperado = [
            [3, 3, 3, 9, 9, 9, "X"],
            [3, 3, 3, 9, 9, 9, "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_7_esperado = Predio(codigo_predio="7", alto=5, ancho=7)
        predio_7_esperado.plano = plano_7_esperado

        plano_3_esperado = [
            ["X", "X", 4, 4, "X", "X", 7, 7],
            ["X", "X", 4, 4, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            [1, "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, 5, 5, "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3_esperado = Predio(codigo_predio="3", alto=7, ancho=8)
        predio_3_esperado.plano = plano_3_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_7_esperado, predio_3_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Ejemplo básico similar del enunciado parte 3. Dos predios en self.predios.
        plano_2 5x7, código_predio = 2.
        plano_3 4x8, código_predio = 3.
        codigo_cultivo = 2, dimensiones 2x5.
        """
        plano_2 = [
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", 5, 5],
        ]
        predio_2 = Predio(codigo_predio="2", alto=5, ancho=7)
        predio_2.plano = plano_2

        plano_3 = [
            ["X", "X", 5, 5, 5, "X", 7, 7],
            ["X", "X", 5, 5, 5, "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3 = Predio(codigo_predio="3", alto=4, ancho=8)
        predio_3.plano = plano_3

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_2, predio_3]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=2, alto=2, ancho=5
        )
        resultado_esperado = True

        plano_2_esperado = [
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [2, 2, 2, 2, 2, "X", "X"],
            [2, 2, 2, 2, 2, 5, 5],
        ]
        predio_2_esperado = Predio(codigo_predio="2", alto=5, ancho=7)
        predio_2_esperado.plano = plano_2_esperado

        plano_3_esperado = [
            ["X", "X", 5, 5, 5, "X", 7, 7],
            ["X", "X", 5, 5, 5, "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3_esperado = Predio(codigo_predio="3", alto=4, ancho=8)
        predio_3_esperado.plano = plano_3_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_2_esperado, predio_3_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Caso complejo con cultivos ya agregados. Tres predios en self.predios.
        plano_56 6x7, código_predio = 56.
        plano_42 2x1, código_predio = 42.
        plano_1 4x4, código_predio = 13.
        codigo_cultivo = 9, dimensiones 4x3.
        """
        plano_56 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            [7, 2, 2, 2, 2, 4, 4],
            ["X", "X", "X", "X", "X", 4, 4],
            ["X", "X", "X", "X", "X", 3, 3],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", 1],
        ]
        predio_56 = Predio(codigo_predio="56", alto=6, ancho=7)
        predio_56.plano = plano_56

        plano_42 = [
            [7],
            [0],
        ]
        predio_42 = Predio(codigo_predio="42", alto=2, ancho=1)
        predio_42.plano = plano_42

        plano_1 = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", 0],
        ]
        predio_1 = Predio(codigo_predio="1", alto=4, ancho=4)
        predio_1.plano = plano_1

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_56, predio_42, predio_1]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=9, alto=4, ancho=3
        )
        resultado_esperado = True

        plano_56_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            [7, 2, 2, 2, 2, 4, 4],
            [9, 9, 9, "X", "X", 4, 4],
            [9, 9, 9, "X", "X", 3, 3],
            [9, 9, 9, "X", "X", "X", "X"],
            [9, 9, 9, "X", "X", "X", 1],
        ]
        predio_56_esperado = Predio(codigo_predio="56", alto=6, ancho=7)
        predio_56_esperado.plano = plano_56_esperado

        plano_42_esperado = [
            [7],
            [0],
        ]
        predio_42_esperado = Predio(codigo_predio="42", alto=2, ancho=1)
        predio_42_esperado.plano = plano_42_esperado

        plano_1_esperado = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", 0],
        ]
        predio_1_esperado = Predio(codigo_predio="1", alto=4, ancho=4)
        predio_1_esperado.plano = plano_1_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_56_esperado,
            predio_42_esperado,
            predio_1_esperado,
        ]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Caso de esquina. Solo un predio en self.predios.
        plano_9 6x5, código_predio = 9.
        codigo_cultivo = 8, dimensiones 3x3.
        """
        plano_9 = [
            [1, 1, 7, "X", 5],
            [1, 1, 6, 6, "X"],
            ["X", "X", "X", 3, 3],
            ["X", 4, "X", "X", "X"],
            [2, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        predio_9 = Predio(codigo_predio="9", alto=6, ancho=5)
        predio_9.plano = plano_9

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_9]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=8, alto=3, ancho=3
        )
        resultado_esperado = True

        plano_9_esperado = plano_9 = [
            [1, 1, 7, "X", 5],
            [1, 1, 6, 6, "X"],
            ["X", "X", "X", 3, 3],
            ["X", 4, 8, 8, 8],
            [2, "X", 8, 8, 8],
            ["X", "X", 8, 8, 8],
        ]
        predio_9_esperado = Predio(codigo_predio="9", alto=6, ancho=5)
        predio_9_esperado.plano = plano_9_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_9_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)
