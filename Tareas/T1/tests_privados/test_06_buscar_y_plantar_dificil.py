import unittest
from dccultivo import Predio, DCCultivo
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestBuscarYPlantarDificil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso ejemplo similar del enunciado. En primer predio no cabe, en segundo sí.
        plano_94 5x7, código_predio = 94
        plano_55 4x11, código_predio = 55
        plano_28 1x10, código_predio = 28
        codigo_cultivo = 6, dimensiones 1x9
        """
        plano_94 = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", 8],
        ]
        predio_94 = Predio(codigo_predio="94", alto=5, ancho=7)
        predio_94.plano = plano_94

        plano_55 = [
            [1, 1, 1, 1, 1, 1, "X", "X", "X", "X", "X"],
            [2, "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", 4, 4, "X", "X", "X", "X"],
        ]
        predio_55 = Predio(codigo_predio="55", alto=4, ancho=11)
        predio_55.plano = plano_55

        plano_28 = [
            ["X", "X", "X", "X", 7, "X", "X", "X", "X", "X"],
        ]
        predio_28 = Predio(codigo_predio="28", alto=1, ancho=10)
        predio_28.plano = plano_28

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_94, predio_55, predio_28]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=6, alto=1, ancho=9
        )
        resultado_esperado = True

        plano_94_esperado = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", 8],
        ]
        predio_94_esperado = Predio(codigo_predio="94", alto=5, ancho=7)
        predio_94_esperado.plano = plano_94_esperado

        plano_55_esperado = [
            [1, 1, 1, 1, 1, 1, "X", "X", "X", "X", "X"],
            [2, 6, 6, 6, 6, 6, 6, 6, 6, 6, "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", 4, 4, "X", "X", "X", "X"],
        ]
        predio_55_esperado = Predio(codigo_predio="55", alto=4, ancho=11)
        predio_55_esperado.plano = plano_55_esperado

        plano_28_esperado = [
            ["X", "X", "X", "X", 7, "X", "X", "X", "X", "X"],
        ]
        predio_28_esperado = Predio(codigo_predio="28", alto=1, ancho=10)
        predio_28_esperado.plano = plano_28_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_94_esperado,
            predio_55_esperado,
            predio_28_esperado,
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
    def test_1(self):
        """
        Caso repetición de código de cultivo.
        plano_4 3x3, código_predio = 4
        plano_5 3x1, código_predio = 5
        codigo_cultivo = 9, dimensiones 2x1
        """
        plano_4 = [
            ["X", "X", 9],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        predio_4 = Predio(codigo_predio="4", alto=3, ancho=3)
        predio_4.plano = plano_4

        plano_5 = [
            ["X"],
            ["X"],
            ["X"],
        ]
        predio_5 = Predio(codigo_predio="5", alto=3, ancho=1)
        predio_5.plano = plano_5

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_4, predio_5]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=9, alto=2, ancho=1
        )
        resultado_esperado = True

        plano_4_esperado = [
            ["X", "X", 9],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        predio_4_esperado = Predio(codigo_predio="4", alto=3, ancho=3)
        predio_4_esperado.plano = plano_4_esperado

        plano_5_esperado = [
            [9],
            [9],
            ["X"],
        ]
        predio_5_esperado = Predio(codigo_predio="5", alto=3, ancho=1)
        predio_5_esperado.plano = plano_5_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_4_esperado, predio_5_esperado]

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
    def test_2(self):
        """
        Caso complejo predios sin espacio.
        plano_7 11x8, código_predio = 7
        plano_9 4x4, código_predio = 9
        plano_10 3x6, código_predio = 10
        codigo_cultivo = 7, dimensiones 2x4
        """
        plano_7 = [
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
        ]
        predio_7 = Predio(codigo_predio="7", alto=11, ancho=8)
        predio_7.plano = plano_7

        plano_9 = [
            [9, 9, "X", "X"],
            [9, 9, 3, 0],
            ["X", 4, "X", "X"],
            ["X", 4, "X", "X"],
        ]
        predio_9 = Predio(codigo_predio="9", alto=4, ancho=4)
        predio_9.plano = plano_9

        plano_10 = [
            [2, 2, 9, 5, 5, "X"],
            ["X", "X", "X", "X", "X", 3],
            ["X", "X", "X", "X", 8, 0],
        ]
        predio_10 = Predio(codigo_predio="10", alto=3, ancho=6)
        predio_10.plano = plano_10

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_7, predio_9, predio_10]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=7, alto=2, ancho=4
        )
        resultado_esperado = True

        plano_7_esperado = [
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7],
        ]
        predio_7_esperado = Predio(codigo_predio="7", alto=11, ancho=8)
        predio_7_esperado.plano = plano_7_esperado

        plano_9_esperado = [
            [9, 9, "X", "X"],
            [9, 9, 3, 0],
            ["X", 4, "X", "X"],
            ["X", 4, "X", "X"],
        ]
        predio_9_esperado = Predio(codigo_predio="9", alto=4, ancho=4)
        predio_9_esperado.plano = plano_9_esperado

        plano_10_esperado = [
            [2, 2, 9, 5, 5, "X"],
            [7, 7, 7, 7, "X", 3],
            [7, 7, 7, 7, 8, 0],
        ]
        predio_10_esperado = Predio(codigo_predio="10", alto=3, ancho=6)
        predio_10_esperado.plano = plano_10_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_7_esperado,
            predio_9_esperado,
            predio_10_esperado,
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
    def test_3(self):
        """
        Caso complejo predios con cultivo ya plantado.
        plano_1 5x5, código_predio = 1
        plano_2 3x3, código_predio = 2
        plano_3 4x4, código_predio = 3
        codigo_cultivo = 3, dimensiones 1x1
        """
        plano_1 = [
            [1, 1, "X", "X", 9],
            ["X", 2, 2, "X", "X"],
            [5, 2, 2, 3, 3],
            ["X", "X", "X", 3, 3],
            [4, 4, "X", 0, "X"],
        ]
        predio_1 = Predio(codigo_predio="1", alto=5, ancho=5)
        predio_1.plano = plano_1

        plano_2 = [
            [2, 2, 2],
            [2, 2, 2],
            ["X", 3, "X"],
        ]
        predio_2 = Predio(codigo_predio="2", alto=3, ancho=3)
        predio_2.plano = plano_2

        plano_3 = [
            [0, 0, 8, "X"],
            [0, 0, "X", "X"],
            ["X", "X", "X", "X"],
            [5, 5, 5, 6],
        ]
        predio_3 = Predio(codigo_predio="3", alto=4, ancho=4)
        predio_3.plano = plano_3

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_1, predio_2, predio_3]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=3, alto=1, ancho=1
        )
        resultado_esperado = True

        plano_1_esperado = [
            [1, 1, "X", "X", 9],
            ["X", 2, 2, "X", "X"],
            [5, 2, 2, 3, 3],
            ["X", "X", "X", 3, 3],
            [4, 4, "X", 0, "X"],
        ]
        predio_1_esperado = Predio(codigo_predio="1", alto=5, ancho=5)
        predio_1_esperado.plano = plano_1_esperado

        plano_2_esperado = [
            [2, 2, 2],
            [2, 2, 2],
            ["X", 3, "X"],
        ]
        predio_2_esperado = Predio(codigo_predio="2", alto=3, ancho=3)
        predio_2_esperado.plano = plano_2_esperado

        plano_3_esperado = [
            [0, 0, 8, 3],
            [0, 0, "X", "X"],
            ["X", "X", "X", "X"],
            [5, 5, 5, 6],
        ]
        predio_3_esperado = Predio(codigo_predio="3", alto=4, ancho=4)
        predio_3_esperado.plano = plano_3_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_1_esperado,
            predio_2_esperado,
            predio_3_esperado,
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
        Caso de avanzar múltples predios para colocar cultivo.
        plano_1 3x1 código_predio = 1
        plano_7 1x3 código_predio = 7
        plano_4 1x1 código_predio = 4
        plano_8 2x2 código_predio = 8
        codigo_cultivo = 2, dimensiones 1x1
        """
        plano_1 = [
            [1],
            [1],
            [0],
        ]
        predio_1 = Predio(codigo_predio="1", alto=3, ancho=1)
        predio_1.plano = plano_1

        plano_7 = [
            [4, 2, "X"],
        ]
        predio_7 = Predio(codigo_predio="7", alto=1, ancho=3)
        predio_7.plano = plano_7

        plano_4 = [
            [5],
        ]
        predio_4 = Predio(codigo_predio="4", alto=1, ancho=1)
        predio_4.plano = plano_4

        plano_8 = [
            [1, 7],
            ["X", 9],
        ]
        predio_8 = Predio(codigo_predio="8", alto=2, ancho=2)
        predio_8.plano = plano_8

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_1, predio_7, predio_4, predio_8]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=2, alto=1, ancho=1
        )
        resultado_esperado = True

        plano_1_esperado = [
            [1],
            [1],
            [0],
        ]
        predio_1_esperado = Predio(codigo_predio="1", alto=3, ancho=1)
        predio_1_esperado.plano = plano_1_esperado

        plano_7_esperado = [
            [4, 2, "X"],
        ]
        predio_7_esperado = Predio(codigo_predio="7", alto=1, ancho=3)
        predio_7_esperado.plano = plano_7_esperado

        plano_4_esperado = [
            [5],
        ]
        predio_4_esperado = Predio(codigo_predio="4", alto=1, ancho=1)
        predio_4_esperado.plano = plano_4_esperado

        plano_8_esperado = [
            [1, 7],
            [2, 9],
        ]
        predio_8_esperado = Predio(codigo_predio="8", alto=2, ancho=2)
        predio_8_esperado.plano = plano_8_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_1_esperado,
            predio_7_esperado,
            predio_4_esperado,
            predio_8_esperado,
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
