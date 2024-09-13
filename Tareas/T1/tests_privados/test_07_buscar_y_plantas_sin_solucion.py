import unittest
from dccultivo import Predio, DCCultivo
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestBuscarYPlantarSinSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso sin solución.
        Solo un predio en self.predios.
        plano_1 5x7 con código_predio = 1, incluye
            - bloque 4x4 con codigo_cultivo = 2 ya ubicado.
        codigo_cultivo = 5, dimensiones 4x4.
        """
        predio_1 = Predio("1", 5, 7)
        predio_1.plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_1)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=5, alto=4, ancho=4
        )
        resultado_esperado = False

        predio_1_esperado = Predio("1", 5, 7)
        predio_1_esperado.plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
            ["X", "X", "X", 2, 2, 2, 2],
        ]
        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_1_esperado)

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
        Caso sin solución.
        Solo un predio en self.predios.
        predio_2 6x7 con código_predio = 2.
        codigo_cultivo = 2, dimensiones 7x7
        """
        predio_2 = Predio("2", 6, 7)
        predio_2.plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_2)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=2, alto=7, ancho=7
        )
        resultado_esperado = False

        predio_2_esperado = Predio("2", 6, 7)
        predio_2_esperado.plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_2_esperado)

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
        Caso sin solución.
        Dos predios en self.predios.
        predio_3 6x5, código_predio = 3, incluye:
            - bloque 4x3 con código_cultivo = 2 ya ubicado
        predio_4 8x2, código_predio = 4, incluye:
            - bloque 1x2 con código_cultivo = 3 ya ubicado

        codigo_cultivo = 4, dimensiones 2x3
        """
        predio_3 = Predio(codigo_predio="3", alto=6, ancho=5)
        predio_3.plano = [
            ["X", "X", "X", "X", "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X"],
        ]

        predio_4 = Predio(codigo_predio="4", alto=8, ancho=2)
        predio_4.plano = [
            [3, 3],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_3)
        dccultivo.predios.append(predio_4)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=4, alto=2, ancho=3
        )
        resultado_esperado = False

        predio_3_esperado = Predio(codigo_predio="3", alto=6, ancho=5)
        predio_3_esperado.plano = [
            ["X", "X", "X", "X", "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X"],
        ]

        predio_4_esperado = Predio(codigo_predio="4", alto=8, ancho=2)
        predio_4_esperado.plano = [
            [3, 3],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
            ["X", "X"],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_3_esperado)
        dccultivo_esperado.predios.append(predio_4_esperado)

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
        Caso sin solución.
        Dos predios en self.predios
        predio_5 9x9, código_predio = 5, incluye:
            - bloque 6x6 con código_cultivo = 2 ya ubicado
            - bloque 2x9 con código_cultivo = 3 ya ubicado

        predio_6 8x6, código_predio = 6, incluye
            - bloque 5x2, código_predio = 4 ya ubicado
            - bloque 4x4, código_predio = 5 ya ubicado
        codigo_cultivo = 7, dimensiones 4x5
        """

        predio_5 = Predio(codigo_predio="5", alto=9, ancho=9)
        predio_5.plano = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]

        predio_6 = Predio(codigo_predio="6", alto=8, ancho=6)
        predio_6.plano = [
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            ["X", "X", "X", "X", 4, 4],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_5)
        dccultivo.predios.append(predio_6)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=7, alto=4, ancho=5
        )
        resultado_esperado = False

        predio_5_esperado = Predio(codigo_predio="5", alto=9, ancho=9)
        predio_5_esperado.plano = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            ["X", "X", "X", "X", 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]

        predio_6_esperado = Predio(codigo_predio="6", alto=8, ancho=6)
        predio_6_esperado.plano = [
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            [5, 5, 5, 5, 4, 4],
            ["X", "X", "X", "X", 4, 4],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_5_esperado)
        dccultivo_esperado.predios.append(predio_6_esperado)

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
