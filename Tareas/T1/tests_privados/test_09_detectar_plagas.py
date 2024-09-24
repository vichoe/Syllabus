import unittest
from dccultivo import Predio, DCCultivo
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestDetectarPlagas(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso simple. Un predio, una plaga. Se elimina una plaga.
        plano_4 5x4, código_predio = 4
        lista_plagas = [["4", [3,3]]]
        """
        plano_4 = [
            ["X", 3, 3, "X"],
            [7, "X", 8, 8],
            ["X", "X", 8, 8],
            ["X", "X", 8, 8],
            ["X", 5, 5, "X"],
        ]
        predio_4 = Predio(codigo_predio="4", alto=5, ancho=4)
        predio_4.plano = plano_4

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_4]

        resultado_estudiante = dccultivo.detectar_plagas(lista_plagas=[["4", [3, 3]]])
        resultado_esperado = [["4", 6]]

        plano_4_esperado = [
            ["X", 3, 3, "X"],
            [7, "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", 5, 5, "X"],
        ]
        predio_4_esperado = Predio(codigo_predio="4", alto=5, ancho=4)
        predio_4_esperado.plano = plano_4_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_4_esperado]

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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso de eliminación efectiva 2 plagas en diferentes predios.
        plano_B4 5x5, código_predio = B4
        plano_C2 2x2, código_predio = C2
        plano_D1 6x7, código_predio = D1
        lista_plagas = [["B4", [4,4]], ["C2", [0,0]], ["D1", [3,6]]]
        """
        plano_B4 = [
            [3, "X", 2, 2, 1],
            ["X", "X", 4, 4, 1],
            [7, 7, "X", 0, 0],
            [7, 7, "X", 5, 5],
            [8, 8, 8, 8, 8],
        ]
        predio_B4 = Predio(codigo_predio="B4", alto=5, ancho=5)
        predio_B4.plano = plano_B4

        plano_C2 = [
            [1, 0],
            [1, 2],
        ]
        predio_C2 = Predio(codigo_predio="C2", alto=2, ancho=2)
        predio_C2.plano = plano_C2

        plano_D1 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", 8, 8],
        ]
        predio_D1 = Predio(codigo_predio="D1", alto=6, ancho=7)
        predio_D1.plano = plano_D1

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_B4, predio_C2, predio_D1]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[["B4", [4, 4]], ["C2", [0, 0]], ["D1", [3, 6]]]
        )
        resultado_esperado = [["C2", 2], ["B4", 5]]

        plano_B4_esperado = [
            [3, "X", 2, 2, 1],
            ["X", "X", 4, 4, 1],
            [7, 7, "X", 0, 0],
            [7, 7, "X", 5, 5],
            ["X", "X", "X", "X", "X"],
        ]
        predio_B4_esperado = Predio(codigo_predio="B4", alto=5, ancho=5)
        predio_B4_esperado.plano = plano_B4_esperado

        plano_C2_esperado = [
            ["X", 0],
            ["X", 2],
        ]
        predio_C2_esperado = Predio(codigo_predio="C2", alto=2, ancho=2)
        predio_C2_esperado.plano = plano_C2_esperado

        plano_D1_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", 8, 8],
        ]
        predio_D1_esperado = Predio(codigo_predio="D1", alto=6, ancho=7)
        predio_D1_esperado.plano = plano_D1_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_B4_esperado,
            predio_C2_esperado,
            predio_D1_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso eliminación muchas plagas en un mismo predio.
        plano_0 4x7, código_predio = 0
        plano_Z 15x15, código_predio = Z
        lista_plagas = [["0", [1,2]], ["Z", [3,9]], ["0", [3, 5], ["Z", [7, 8]], ["Z", [11, 0]]]
        """
        plano_0 = [
            [4, "X", 2, "X", "X", "X", "X"],
            [1, "X", 7, 7, "X", "X", 0],
            [1, "X", 7, 7, 9, 9, 9],
            ["X", "X", 7, 7, 9, 9, 9],
        ]
        predio_0 = Predio(codigo_predio="0", alto=4, ancho=7)
        predio_0.plano = plano_0

        plano_Z = [[3 for _ in range(15)] for _ in range(15)]
        predio_Z = Predio(codigo_predio="Z", alto=15, ancho=15)
        predio_Z.plano = plano_Z

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_0, predio_Z]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[
                ["0", [1, 2]],
                ["Z", [3, 9]],
                ["0", [3, 5]],
                ["Z", [7, 8]],
                ["Z", [11, 0]],
            ]
        )
        resultado_esperado = [["0", 12], ["Z", 225]]

        plano_0_esperado = [
            [4, "X", 2, "X", "X", "X", "X"],
            [1, "X", "X", "X", "X", "X", 0],
            [1, "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_0_esperado = Predio(codigo_predio="0", alto=4, ancho=7)
        predio_0_esperado.plano = plano_0_esperado

        plano_Z_esperado = [["X" for _ in range(15)] for _ in range(15)]
        predio_Z_esperado = Predio(codigo_predio="Z", alto=15, ancho=15)
        predio_Z_esperado.plano = plano_Z_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_0_esperado, predio_Z_esperado]

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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso de empate en eliminación de plagas en diferentes predios.
        plano_V 3x4, código_predio = V
        plano_K 4x3, código_predio = K
        plano_A 10x1, código_predio = A
        lista_plagas = [["V", [1, 1]], ["K", [3, 2]], ["A", [0, 0], "V", [2, 1]]]
        """
        plano_V = [
            [1, 1, 1, 1],
            ["X", 8, "X", "X"],
            ["X", 3, 3, 3],
        ]
        predio_V = Predio(codigo_predio="V", alto=3, ancho=4)
        predio_V.plano = plano_V

        plano_K = [
            ["X", 0, 7],
            ["X", 4, 7],
            ["X", 2, 7],
            ["X", 5, 7],
        ]
        predio_K = Predio(codigo_predio="K", alto=4, ancho=3)
        predio_K.plano = plano_K

        plano_A = [[0], [1], [2], [3], ["X"], [5], [6], [7], [8], [9]]
        predio_A = Predio(codigo_predio="A", alto=10, ancho=1)
        predio_A.plano = plano_A

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_V, predio_K, predio_A]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[["V", [1, 1]], ["K", [3, 2]], ["A", [0, 0]], ["V", [2, 1]]]
        )
        resultado_esperado = [["A", 1], ["K", 4], ["V", 4]]

        plano_V_esperado = [
            [1, 1, 1, 1],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        predio_V_esperado = Predio(codigo_predio="V", alto=3, ancho=4)
        predio_V_esperado.plano = plano_V_esperado

        plano_K_esperado = [
            ["X", 0, "X"],
            ["X", 4, "X"],
            ["X", 2, "X"],
            ["X", 5, "X"],
        ]
        predio_K_esperado = Predio(codigo_predio="K", alto=4, ancho=3)
        predio_K_esperado.plano = plano_K_esperado

        plano_A_esperado = [["X"], [1], [2], [3], ["X"], [5], [6], [7], [8], [9]]
        predio_A_esperado = Predio(codigo_predio="A", alto=10, ancho=1)
        predio_A_esperado.plano = plano_A_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_V_esperado,
            predio_K_esperado,
            predio_A_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso múltiples predios, múltiples plagas.
        plano_0Z 2x1, código_predio = 0Z
        plano_D 2x1, código_predio = D
        plano_B 2x1, código_predio = B
        plano_C 3x1, código_predio = C
        lista_plagas = [["0Z", [0, 0]], ["D", [1, 0]], ["B", [1, 0]], ["C", [0, 0]], ["0Z", [1, 0]]]
        """
        plano_0Z = [[0], [3]]
        predio_0Z = Predio(codigo_predio="0Z", alto=2, ancho=1)
        predio_0Z.plano = plano_0Z

        plano_D = [[9], [1]]
        predio_D = Predio(codigo_predio="D", alto=2, ancho=1)
        predio_D.plano = plano_D

        plano_B = [["X"], [3]]
        predio_B = Predio(codigo_predio="B", alto=2, ancho=1)
        predio_B.plano = plano_B

        plano_C = [[2], ["X"], ["X"]]
        predio_C = Predio(codigo_predio="C", alto=3, ancho=1)
        predio_C.plano = plano_C

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_D, predio_B, predio_C, predio_0Z]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[
                ["0Z", [0, 0]],
                ["D", [1, 0]],
                ["B", [1, 0]],
                ["C", [0, 0]],
                ["0Z", [1, 0]],
            ]
        )
        resultado_esperado = [["B", 1], ["C", 1], ["D", 1], ["0Z", 2]]

        plano_0Z_esperado = [["X"], ["X"]]
        predio_0Z_esperado = Predio(codigo_predio="0Z", alto=2, ancho=1)
        predio_0Z_esperado.plano = plano_0Z_esperado

        plano_D_esperado = [[9], ["X"]]
        predio_D_esperado = Predio(codigo_predio="D", alto=2, ancho=1)
        predio_D_esperado.plano = plano_D_esperado

        plano_B_esperado = [["X"], ["X"]]
        predio_B_esperado = Predio(codigo_predio="B", alto=2, ancho=1)
        predio_B_esperado.plano = plano_B_esperado

        plano_C_esperado = [["X"], ["X"], ["X"]]
        predio_C_esperado = Predio(codigo_predio="C", alto=3, ancho=1)
        predio_C_esperado.plano = plano_C_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_D_esperado,
            predio_B_esperado,
            predio_C_esperado,
            predio_0Z_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
