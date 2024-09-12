from typing import Any, Union
from abc import ABC, abstractmethod
from hashlib import sha256


class Nodo:
    """
    Esta clase representa un nodo de una Estructura Secuencial
    """

    def __init__(self, valor: Any = None) -> None:
        """
        Inicializa la estructura del nodo
        """
        self.valor = valor
        self.siguiente = None  # Al crear un nodo,
                               # la referencia al siguiente 
                               # nodo comienza vacía

    def __repr__(self) -> str:
        return f"Nodo[{self.valor}]"


class NodoLlave(Nodo):
    """
    Esta clase representa un nodo
    de una EstructuraSecuencialNodalLlaveValor
    """

    def __init__(self, llave: Any = None, valor: Any = None) -> None:
        super().__init__(valor)
        self._llave = llave

    @property
    def llave(self) -> Any:
        return self._llave
        # Aca va la solución al desafío:
        # Deben reemplazar return self._llave por
        # return self._generar_hash_llave()

    @llave.setter
    def llave(self, valor: Any) -> None:
        self._llave = valor

    # Explicar este metodo en el Desafío:
    #   Ahora la property es un hash
    def _generar_hash_llave(self) -> str:
        """
        Método "privado" que tiene como objetivo obtener
        el hash de la llave del NodoLlave

        COMPLETITUD: Este método viene hecho. NO IMPLEMENTAR
        """
        """
        Aca hacemos un poco de "trampa", ya que transformamos todos los tipos
        a string para poder asegurarnos de que exista un hash
        Que "problema" conllevaría esto?
        """
        llave_str = str(self._llave)
        return sha256(llave_str.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        llave_display = self.llave
        if isinstance(self.llave, str):
            llave_display = f'"{self.llave}"'
        return f"Nodo[{llave_display} : {self.valor}]"


class EstructuraSecuencialNodalLlaveValor(ABC):
    """
    Clase abstracta que representa
    una estructura secuencial
    en base a NodosLlave
    """

    def _verificar_existencia(self, llave: str) -> bool:
        """
        Método "privado" que tiene como objetivo poder
        obtener el NodoLlave relacionado a alguna 
        llave especifica
        COMPLETITUD: Este método viene hecho. NO IMPLEMENTAR
        """
        nodo_actual = self.cabeza
        if nodo_actual is None:
            return False
        while nodo_actual != None:
            if nodo_actual.llave == llave:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def _obtener_nodo(self, llave: str) -> Union[NodoLlave, None]:
        """
        Método "privado" que tiene como objetivo poder obtener 
        el NodoLlave relacionado a alguna llave especifica

        COMPLETITUD: Este método viene hecho. NO IMPLEMENTAR
        """
        if not self._verificar_existencia(llave):
            return None

        nodo_actual = self.cabeza

        for _ in range(self.largo):
            if nodo_actual is not None:
                if llave == nodo_actual.llave:
                    return nodo_actual
                nodo_actual = nodo_actual.siguiente
        return None

    def __init__(self) -> None:
        self.cabeza = None
        self.largo = 0

    @abstractmethod
    def agregar(self, llave: Any, valor: Any) -> None:
        pass

    @abstractmethod
    def obtener(self, llave: Any) -> Any:
        pass

    def __len__(self) -> int:
        """
        Metodo que tiene como objetivo 
        retornar el largo de la estructura
        cuando se utiliza la siguente sintaxis:
            len(estructura)

        COMPLETITUD: Este metodo viene hecho. NO IMPLEMENTAR
        """
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            nodo_actual = nodo_actual.siguiente
            contador += 1
        self.largo = contador
        return self.largo

    def __repr__(self) -> str:
        """
        Metodo que tiene como objetivo retornar
        una representacion legible de la estructura
        cuando se utiliza la siguiente sintaxis:
            print(estructura)

        COMPLETITUD: Este metodo viene hecho. NO IMPLEMENTAR
        """
        string = ""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            string = f"{string}{nodo_actual} → "
            nodo_actual = nodo_actual.siguiente
        return string
