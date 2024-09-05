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
        self._index_iteracion = 0
        self.cabeza = cabeza

    def __next__(self) -> Any:
        """
        PARTE 2.1: IMPLEMENTAR ESTE METODO

        Método para que el iterador pueda encontrar el siguiente elemento
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        pass

    def __iter__(self) -> Self:
        """
        PARTE 2.2: IMPLEMENTAR ESTE MÉTODO

        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        """
        pass


class DCCustomDictionary(EstructuraSecuencialNodalLlaveValor):

    def agregar(self, llave: Any, valor: Any) -> None:
        '''
        PARTE 1.1: CORREGIR E IMPLEMENTAR CORRECTAMENTE ESTE METODO

        Metodo que nos permite agregar un nuevo NodoLlave[llave, valor] 
        a la estructura o actualizar el NodoLlave que posea la llave
        que entre a este metodo
        
        Dado a que ahora operamos sobre nuestra estructura DCCustomDictionary,
        Que cosas estarian malas en este metodo?
        Aqui hay 2 errores

        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        '''
        # Inicializamos el nuevo nodo
        nuevo = NodoLlave(llave, valor)

        # Si la lista está vacía (no hay cabeza)
        if self.cabeza is None:
            # El nuevo nodo es la cabeza y cola de la lista
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            # Agregamos el nuevo nodo como sucesor del nodo cola actual
            self.cola.siguiente = nuevo
            # Actualizamos la referencia al nodo cola
            self.cola = self.cola.siguiente
        self.largo += 1

    def obtener(self, llave: Any) -> Union[Any, None]:
        '''
        PARTE 1.2: IMPLEMENTAR ESTE MÉTODO

        Metodo que nos permite obtener el valor del
        NodoLlave que posea la llave que 
        ingresa como parametro

        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        '''
        pass

    def __iter__(self) -> Self:
        '''
        PARTE 2.3: IMPLEMENTAR ESTE MéTODO

        Método que transforma la estructura en un Iterable
        
        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        '''
        pass

    def __setitem__(self, llave: Any, valor: Any) -> None:
        '''
        PARTE 3.1: IMPLEMENTAR ESTE METODO

        Método que permite asignar un nuevo NodoLlave mediante la sintaxis:
            estructura[llave] = valor

        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        '''
        pass

    def __getitem__(self, llave: Any) -> Union[Any, None]:
        '''
        PARTE 3.2: IMPLEMENTAR ESTE MÉTODO

        Método que permite obtener un NodoLlave existente mediante la sintaxis:
            estructura[llave]

        COMPLETITUD: Este método DEBE IMPLEMENTARSE
        '''
        pass

    def __setattr__(self, name, value):
        '''
        No es necesario entender este metodo
        Lo importante es que este se encarga de
        que la clase no pueda tener ningun atributo
        con el nombre de:
            cola

        COMPLETITUD: Este metodo viene hecho. NO IMPLEMENTAR
        '''
        if name in ['cola']:
            raise AttributeError(f"El atributo '{name}' no esta permitido en esta clase.")
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

    # Completar usando 2 llaves que se vean iguales, 
    # pero sean distinto tipo de dato.