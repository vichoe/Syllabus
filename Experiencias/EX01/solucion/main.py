from typing import Any, Union, Self

from clases_bases import NodoLlave, EstructuraSecuencialNodalLlaveValor


class IteradorDCCustomDictionary:
    """
    Esta clase la veremos en la Parte 2. Omitir por ahora.
    """

    def __init__(self, cabeza: NodoLlave) -> None:
        """
        Método que tiene como objetivo definir los
        atributos de una instancia

        COMPLETITUD: Este metodo viene hecho. NO IMPLEMENTAR
        """
        # NOTE: Aca explicar que es necesario este atributo para la Parte 2,
        # ya que sera el que nos permita tener un estado
        # interno al momento de iterar
        self._index_iteracion = 0
        self.cabeza = cabeza

    def __next__(self) -> Any:
        """
        PARTE 2.1: IMPLEMENTAR ESTE METODO

        Método para que el iterador pueda encontrar el siguiente elemento
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        if self._index_iteracion == 0:
            self.nodo_iteracion = self.cabeza

        if not self.nodo_iteracion:
            self.nodo_iteracion = self.cabeza
            self._index_iteracion = 0
            raise StopIteration("Llegamos al final")
        else:
            self._index_iteracion += 1
            valor = self.nodo_iteracion.valor
            self.nodo_iteracion = self.nodo_iteracion.siguiente
            return valor

    def __iter__(self) -> Self:
        """
        PARTE 2.2: IMPLEMENTAR ESTE MÉTODO

        Método que transforma la estructura en un Iterable
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        return self


class DCCustomDictionary(EstructuraSecuencialNodalLlaveValor):

    def agregar(self, llave: Any, valor: Any) -> None:
        """
        PARTE 1.1: CORREGIR E IMPLEMENTAR CORRECTAMENTE ESTE MÉTODO

        Metodo que nos permite agregar un nuevo NodoLlave[llave, valor] 
        a la estructura o actualizar el NodoLlave que posea la llave
        que entre a este metodo

        Método que tiene como objetivo poder agregar
        un nuevo NodoLlave en la estructura con
        una llave y valor determinados

        COMPLETITUD: Este método DEBE SER CORREGIDO E IMPLEMENTADO

        ERRORES:
            1.- No se verifica la existencia de la llave en la estructura
            2.- self.cola no existe, por lo tanto esta mal implementada
                la agregación del nodo (es necesario iterar sobre nodos)
        """
        nuevo_nodo = NodoLlave(llave, valor)
        nuevo_hash = nuevo_nodo.llave

        # Si la llave existe, actualizamos el valor de dicho nodo
        if self._verificar_existencia(nuevo_hash):
            nodo_existente = self._obtener_nodo(nuevo_hash)
            # Este checkeo es innecesario ya que con el de si existe
            # en las llaves bastaría
            if nodo_existente:
                nodo_existente.valor = nuevo_nodo.valor
                return None

        # Si no, agregamos el nuevo nodo al iterable

        # Primero, verificamos si esta vacío el iterable,
        # y si es asi, lo agregamos al comienzo
        nodo_actual = self.cabeza
        if not nodo_actual:
            self.cabeza = nuevo_nodo
            self.largo += 1
            return None

        # De lo contrario, iteramos sobre los nodos
        # para poder agregarlo al final de ellos
        for _ in range(self.largo - 1):
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        self.largo += 1
        return None

    def obtener(self, llave: Any) -> Union[Any, None]:
        """
        PARTE 1.2: IMPLEMENTAR ESTE METODO
        """

        '''
        Metodo que nos permite obtener el valor del
        NodoLlave que posea la llave que 
        ingresa como parametro
        '''

        """
        Desafío parte 2:
            Las siguientes 2 lineas son necesarias para implementar
            completamente el desafío
            # nodo_fantasma = NodoLlave(llave, None)
            # llave = nodo_fantasma.llave
        """
        nodo_buscado = self._obtener_nodo(llave)
        if nodo_buscado:
            return nodo_buscado.valor
        return nodo_buscado

    def __iter__(self) -> Self:
        """
        PARTE 2.3: IMPLEMENTAR ESTE MÉTODO

        Método que transforma la estructura en un Iterable
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        return IteradorDCCustomDictionary(self.cabeza)

    def __setitem__(self, llave: Any, valor: Any) -> None:
        """
        PARTE 3.1: IMPLEMENTAR ESTE MÉTODO

        Método que permite asignar un nuedo NodoLlave mediante la sintaxis:
            estructura[llave] = valor
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        self.agregar(llave, valor)

    def __getitem__(self, llave: Any) -> Union[Any, None]:
        """
        PARTE 3.2: IMPLEMENTAR ESTE MÉTODO

        Método que permite obtener un NodoLlave existente mediante la sintaxis:
            estructura[llave]
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        return self.obtener(llave)

    def __setattr__(self, name, value):
        """
        No es necesario entender este método
        Lo importante es que este se encarga de
        que la clase no pueda tener ningún atributo
        con el nombre de:
            cola
        """
        if name in ["cola"]:
            raise AttributeError(
                f"El atributo '{name}' no esta permitido en esta clase."
            )
        super().__setattr__(name, value)


if __name__ == "__main__":
    ### Parte 1.1 ###
    my_dict = DCCustomDictionary()
    
    my_dict.agregar(1, "Valor Inicial")
    my_dict.agregar(5.6, 2)
    my_dict.agregar(3, 2)
    my_dict.agregar("3", 50)
    my_dict.agregar([1, 2, 3], [1, 2, 3])
    my_dict.agregar(([1, 2, 3],), [3, 2, 1])

    print(f"Largo de mi DCCustomDictionary: {len(my_dict)}")
    print(f"Elementos en mi DCCustomDictionary:\n\t{my_dict}\n")
    
    ### Parte 1.2 ###

    print(f'Obtenemos el valor asociado a la llave: {5.6} → {my_dict.obtener(5.6)}')
    print(f'Obtenemos el valor asociado a la llave: {3} → {my_dict.obtener(3)}')
    print(f'Obtenemos el valor asociado a la llave: "3" → {my_dict.obtener("3")}\n')

    ### Parte 2 ###
    iterador_my_dict = iter(my_dict)
    print(iterador_my_dict)

    print(f'next(iterador): {next(iterador_my_dict)}\n')


    # Iteramos sobre los valores de nuestra estructura
    for idx, valor in enumerate(my_dict):
        print(f"En el nodo con posicion: {idx} tenemos el valor: {valor}")
    print("\n")

    ### Parte 3 ###

    # Modificamos el valor de la llave 3 con la siguiente sintaxis
    mi_llave = 3
    my_dict[mi_llave] = 100
    # Accedemos a su valor con siguiente sintaxis
    print(f"El nuevo valor para la llave: {mi_llave} es: {my_dict[3]}\n")

    ### Desafio ###

    # Aca podemos ver el "problema" que mencionamos
    # relacionado a tratar todas las llaves como str
    my_dict.agregar(3, 2)
    my_dict.agregar("3", 50)
