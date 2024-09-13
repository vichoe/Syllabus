import unittest
from dccultivo import DCCultivo
from tests_privados.timeout_function import timeout
import sys
import os

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestCrearPredio(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_cargar_archivo_no_existente(self):
        """
        Se comprueba que se retorna correctamente lo indicado
        """
        cultivo = DCCultivo()

        resultado_estudiante = cultivo.crear_predios(
            "soy_otro_archivo_que_no_existe.txt"
        )
        string_esperado = "Fallo en la carga de DCCultivo"

        self.assertIsInstance(resultado_estudiante, str)
        self.assertEqual(resultado_estudiante, string_esperado)

    @timeout(N_SECOND)
    def test_01_cargar_archivo_no_existente_sin_cambios(self):
        """
        Se comprueba que al cargar un archivo que no existe no cambie nada
        y que se retorne correctamente lo indicado
        """
        cultivo = DCCultivo()
        predios = cultivo.predios

        resultado_estudiante = cultivo.crear_predios(
            "soy_otro_archivo_que_no_existe.txt"
        )
        string_esperado = "Fallo en la carga de DCCultivo"

        self.assertIsInstance(resultado_estudiante, str)
        self.assertEqual(resultado_estudiante, string_esperado)
        self.assertListEqual(predios, cultivo.predios)

    @timeout(N_SECOND)
    def test_02_cargar_archivo_existente(self):
        """
        Se comprueba la correcta carga de los predios y
        que se retorne correctamente lo indicado
        """
        cultivo = DCCultivo()

        resultado_estudiante = cultivo.crear_predios(
            "predios_para_los_tests_privados.txt"
        )
        predios = cultivo.predios
        string_esperado = "Predios de DCCultivo cargados exitosamente"

        self.assertIsInstance(resultado_estudiante, str)
        self.assertEqual(resultado_estudiante, string_esperado)
        self.assertListEqual(
            ["1", 7, 4], [predios[0].codigo_predio, predios[0].alto, predios[0].ancho]
        )

        self.assertListEqual(
            ["2", 7, 8], [predios[1].codigo_predio, predios[1].alto, predios[1].ancho]
        )

        self.assertListEqual(
            ["3", 2, 9], [predios[2].codigo_predio, predios[2].alto, predios[2].ancho]
        )

        self.assertListEqual(
            ["4", 12, 11], [predios[3].codigo_predio, predios[3].alto, predios[3].ancho]
        )

        self.assertListEqual(
            ["5", 9, 12], [predios[4].codigo_predio, predios[4].alto, predios[4].ancho]
        )

    @timeout(N_SECOND)
    def test_03_predios_correctos_plano_normal(self):
        """
        Se comprueba que se hayan creado correctamente los planos normales de los predios
        y que se retorne correctamente lo esperado
        """
        cultivo = DCCultivo()

        resultado_estudiante = cultivo.crear_predios(
            "predios_para_los_tests_privados.txt"
        )
        predios = cultivo.predios
        string_esperado = "Predios de DCCultivo cargados exitosamente"

        self.assertIsInstance(resultado_estudiante, str)
        self.assertEqual(resultado_estudiante, string_esperado)
        # P1,7,4
        self.assertListEqual(
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
            ],
            predios[0].plano,
        )

        # P2,7,8
        self.assertListEqual(
            [
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
            ],
            predios[1].plano,
        )

        # P3,2,9
        self.assertListEqual(
            [
                ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ],
            predios[2].plano,
        )

        # P4,12,11
        self.assertListEqual(
            [
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ],
            predios[3].plano,
        )

        # P5,9,12
        self.assertListEqual(
            [
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ],
            predios[4].plano,
        )

    @timeout(N_SECOND)
    def test_04_predios_correctos_plano_riego(self):
        """
        Se comprueba que se hayan creado correctamente los planos de riego de los prefios
        y que se retorne correctamente lo esperado
        """
        cultivo = DCCultivo()

        resultado_estudiante = cultivo.crear_predios(
            "predios_para_los_tests_privados.txt"
        )
        predios = cultivo.predios
        string_esperado = "Predios de DCCultivo cargados exitosamente"

        self.assertIsInstance(resultado_estudiante, str)
        self.assertEqual(resultado_estudiante, string_esperado)
        # P1,7,4
        self.assertListEqual(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            predios[0].plano_riego,
        )

        # P2,7,8
        self.assertListEqual(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            predios[1].plano_riego,
        )

        # P3,2,9
        self.assertListEqual(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            predios[2].plano_riego,
        )

        # P4,12,11
        self.assertListEqual(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            predios[3].plano_riego,
        )

        # P5,9,12
        self.assertListEqual(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            predios[4].plano_riego,
        )
