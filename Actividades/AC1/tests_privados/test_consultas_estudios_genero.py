import unittest
import main
from utilidades import Anime


class VerificarConsultasEstudiosGenero(unittest.TestCase):

    def test_tipo_dato_caso_vacio(self):
        """
        Verifica que lo retornado sea una lista cuando no llegan estudios
        """
        # animes_por_estreno
        estudios = main.estudios_con_genero("Comedia")
        self.assertIsInstance(estudios, list)

    def test_tipo_dato_caso_no_vacio(self):
        """
        Verifica que lo retornado sea una lista.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})

        # animes_por_estreno
        estudios = main.estudios_con_genero("Comedia", sunrise=[anime_1, anime_2])
        self.assertIsInstance(estudios, list)

    def test_resultado_caso_no_match_1_estudio(self):
        """
        Verifica el contenido cuando el género no está en ningún estudio
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})

        # animes_por_estreno
        estudios = main.estudios_con_genero("Horror", sunrise=[anime_1, anime_2])
        respuesta_esperada = []
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_match_1_estudio(self):
        """
        Verifica el contenido cuando el género no está en ningún estudio
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})

        # animes_por_estreno
        estudios = main.estudios_con_genero("Comedia", sunrise=[anime_1, anime_2])
        respuesta_esperada = ["sunrise"]
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_match_total_2_estudios(self):
        """
        Verifica la respuesta esperada cuando hay 2 estudios, y el género hace match con ambos.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise New", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise New", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Aventura", sunrise_new=[anime_1, anime_2], ghibli=[anime_3]
        )
        respuesta_esperada = ["sunrise_new", "ghibli"]
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_match_parcial_2_estudios(self):
        """
        Verifica la respuesta esperada cuando hay 2 estudios, y el género hace match con uno.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Fantasía", sunrise=[anime_1, anime_2], ghibli=[anime_3]
        )
        respuesta_esperada = ["ghibli"]
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_no_match_2_estudios(self):
        """
        Verifica la respuesta esperada cuando hay 2 estudios, pero el género no está en ninguno
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Isekai", sunrise=[anime_1, anime_2], ghibli=[anime_3]
        )
        respuesta_esperada = []
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_no_match_varios_estudios(self):
        """
        Verifica que lo retornado sea una lista.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})
        anime_4 = Anime("Amapolas", 1, 3, 2111, "Ghibli", {"Romance"})
        anime_5 = Anime(
            "Hunter x Hunter", 62, 9, 1999, "Nippon Animation",
            {"Aventura", "Comedia", "Shonen", "Acción"}
        )

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Isekai",
            sunrise=[anime_1, anime_2],
            ghibli=[anime_3, anime_4],
            Nippon_animation=[anime_5],
        )
        respuesta_esperada = []
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_match_total_varios_estudios(self):
        """
        Verifica que lo retornado sea una lista.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia", "Romance"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})
        anime_4 = Anime("Amapolas", 1, 3, 2111, "Ghibli", {"Romance"})
        anime_5 = Anime(
            "Hunter x Hunter", 62, 9, 1999, "Nippon Animation",
            {"Aventura", "Comedia", "Shonen", "Acción"}
        )

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Aventura",
            sunrise=[anime_1, anime_2],
            ghibli=[anime_3, anime_4],
            Nippon_animation=[anime_5],
        )
        respuesta_esperada = ["ghibli", "Nippon_animation", "sunrise"]
        self.assertCountEqual(estudios, respuesta_esperada)

    def test_resultado_caso_match_parcial_varios_estudios(self):
        """
        Verifica que lo retornado sea una lista.
        """
        anime_1 = Anime(
            "BnH", 24, 6, 2016, "Sunrise new 2", {"Acción", "Aventura", "Comedia", "Romance"}
        )
        anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise new 2", {"Parodia"})
        anime_3 = Anime("ChihiroViaje", 1, 9, 2111, "Ghibli", {"Fantasía", "Aventura"})
        anime_4 = Anime("Amapolas", 1, 3, 2111, "Ghibli", {"Romance"})
        anime_5 = Anime(
            "Hunter x Hunter", 62, 9, 1999, "Nippon Animation",
            {"Aventura", "Comedia", "Shonen", "Acción"}
        )

        # animes_por_estreno
        estudios = main.estudios_con_genero(
            "Parodia",
            sunrise_new_2=[anime_1, anime_2],
            ghibli=[anime_3, anime_4],
            madhouse=[anime_5],
        )
        respuesta_esperada = ["sunrise_new_2"]
        self.assertCountEqual(estudios, respuesta_esperada)
