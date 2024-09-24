import funciones
import inspect
import re
import unittest
from utilidades import Pelicula


class ComandoProhibidoError(BaseException):
    def __init__(self, comandos: list, prohibido: bool = True, *args: object) -> None:
        if prohibido:
            mensaje = 'Se utiliza alguno de estos elementos en la función: '
        else:
            mensaje = 'No se utiliza alguno de estos elementos esperado en la función: '
        mensaje += ', '.join(comandos)
        super().__init__(mensaje, *args[2:])


def usa_comando_prohibido(func, comandos):
    '''
    Comprueba el uso de un comando prohibido en el código.
    En caso de encontrarlo, levanta una excepción.
    '''

    codigo_fuente = inspect.getsource(func).replace('\\', ' ')
    codigo = codigo_fuente.strip()
    for comando in comandos:
        expresion = rf'{comando}([^\n]\s+)'
        if re.search(expresion, codigo):
            raise ComandoProhibidoError(comandos)


def usa_metodo_prohibido(func, comandos):
    '''
    Comprueba el uso de un método prohibido en el código.
    En caso de encontrarlo, levanta una excepción.
    '''

    codigo_fuente = inspect.getsource(func).replace('\\', ' ')
    codigo = codigo_fuente.strip()
    for comando in comandos:
        expresion = rf'{comando}\s*\('
        if re.search(expresion, codigo):
            raise ComandoProhibidoError(comandos)


class TestObtenerStrTitulo(unittest.TestCase):

    def generador_peliculas(self, variacion):
        '''
        Función generadora que retorna distintas instancias de película.
        '''

        if variacion == 1:
            yield Pelicula(16, 'Interstelar', 'Christopher Nolan', 2014, 8.6)
        elif variacion == 2:
            yield Pelicula(8, 'Buenos muchachos', 'Martin Scorsese', 1990, 8.7)
            yield Pelicula(13, 'Los infiltrados', 'Martin Scorsese', 2006, 8.5)
        elif variacion == 3:
            yield Pelicula(5, 'El club de la pelea', 'David Fincher', 1999, 8.8)
            yield Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5)
            yield Pelicula(19, 'El Gran Gatsby', 'Baz Luhrmann', 2013, 7.2)
        elif variacion == 4:
            yield Pelicula(4, 'Batman: el caballero de la noche', 'Christopher Nolan', 2008, 9.0)
            yield Pelicula(17, 'Lo que el viento se llevo', 'Victor Fleming', 1939, 8.1)
            yield Pelicula(6, 'El origen', 'Christopher Nolan', 2010, 8.8)
            yield Pelicula(7, 'Matrix', 'Lana Wachowski', 1999, 8.7)
            yield Pelicula(5, 'El club de la pelea', 'David Fincher', 1999, 8.8)
            yield Pelicula(20, 'Red Social', 'David Fincher', 2010, 7.7)

    def test_obtener_str_titulos_1(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 1 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(1))
        titulos_esperado = 'Interstelar'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_2(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 2 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(2))
        titulos_esperado = 'Buenos muchachos, Los infiltrados'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_3(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 3 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(3))
        titulos_esperado = 'El club de la pelea, Casablanca, El Gran Gatsby'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_4(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 4 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(4))
        titulos_esperado = 'Batman: el caballero de la noche, Lo que el viento se llevo, El origen, Matrix, El club de la pelea, Red Social'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_vacio(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string vacío
        cuando no se le pasan películas.
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(5))
        titulos_esperado = ''
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])
