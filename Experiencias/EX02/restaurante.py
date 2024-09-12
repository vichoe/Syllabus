from dccaja import CajaTienda

import copy
import os
import pickle


class Restaurante:
    """
    Clase que representa nuestro restaurante.
    Sus métodos hacen uso de la caja registradora externa.
    """

    def __init__(self, nombre: str) -> None:
        """
        Solo necesitamos almacenar el nombre del Restaurante
        y una instancia de la Caja Registradora.

        NO MODIFICAR
        """
        self.nombre = nombre
        self.caja = CajaTienda(0)

    def _desencriptar_archivo(self, ruta_archivo: str) -> list:
        """
        Este método desencripta el archivo con los productos.
        Spoiler: en unas semanas más sabrás cómo funciona este método ;)

        NO MODIFICAR
        """
        with open(ruta_archivo, "rb") as archivo:
            contenido_desencriptado = pickle.load(archivo)
            return contenido_desencriptado.split("\n")

    def cargar_inventario(self, ruta_productos: str) -> None:
        """
        Método que recibe una ruta al archivo con productos y los carga 
        en la caja registradora.

        PARTE 1: Debemos modificar este método, agregando try/except o if/else
        según corresponda, para que se pueda ejecutar a pesar de los errores que
        levanta el módulo caja.
        """
        print("Cargando productos al inventario...\n")

        productos = self._desencriptar_archivo(ruta_productos)

        ### ------- COMPLETAR/MEJORAR ------- ###
        for item in productos:
            # Código original.
            # Esta versión lanzará un TypeError
            nombre, precio = item.split(",")
            self.caja.ingresar_producto(nombre, precio)

        print("\nCarga de productos finalizada.")

    def cliente_comprar(self, cliente: dict) -> None:
        """
        Este método procesa la lista de compras de un cliente.

        PARTE 2: Debemos modificarlo para que funcione con la primera compra del restaurante,
        agregando los elementos faltantes que necesite. ¿Qué elementos? Veamos el detalle del
        error para descubrirlo.

        PARTE 3: Debemos seguir modificando el elemento para que funcione aunque hayan errores en 
        los pedidos. ¿Qué errores? Veamos el detalle del error para descubrirlo.
        """
        # PARTE 2 y 3: COMPLETAR
        # ¿Qué error nos lanza al probar la sección 1.2?
        # Una vez arreglemos lo anterior, ¿Qué error nos lanzará al probar la sección 1.3?
        self.caja.procesar_compra(
            cliente['nombre'], cliente['compras'], cliente['rut'])

    def cerrar_por_el_dia(self) -> None:
        """
        Método que cierra la caja por el día y da las estadísticas de las compras diarias.
        Cualquier nueva compra corresponde al día siguiente

        PARTE 4: El método funciona perfectamente cuando gente compra en un día.
        ¿Pero qué pasa en un día sin ventas? 
        Deberemos arreglarlo con un try/Except o un if/else.
        """
        # PARTE 4: COMPLETAR

        self.caja.cuadrar_caja()
        self.caja.cerrar_caja()


if __name__ == "__main__":
    # Inicializamos nuestra tienda
    miTienda = Restaurante("El DCCarrito de la esquina")

    ### PARTE 1: Cargar elementos en la lista de productos ###
    # Probaremos el Cargar elementos en la lista de productos
    print("PROBANDO PARTE 1: Carga de productos...\n", 15 * "*")

    ruta_productos = os.path.join("data", "productos.topsecret")
    miTienda.cargar_inventario(ruta_productos)

    input(15 * "*" + "\n> Presiona enter para probar la siguiente sección")

    ###  PARTE 2: Simular el paso del primer cliente de la tienda ###
    print("\nPROBANDO PARTE 2: Paso del primer cliente...\n", 15 * "*")

    cliente_1 = {
        "nombre": "Arturo Vidal",
        "rut": "12345567-3",
        "compras": ["Pizza individual", "Lasaña"],
    }
    miTienda.cliente_comprar(cliente_1)

    input(15 * "*" + "\n> Presiona enter para probar la siguiente sección")

    ### PARTE 3: Simular el paso de otros cliente que quiere comprar cosas no existentes ###
    print("\nPROBANDO PARTE 3: Paso de un segundo cliente...\n", 15 * "*")

    cliente_2 = {
        "nombre": "Ricardo Meruane",
        "rut": "9876543-2",
        "compras": ["Cazuela de pollo", "Nóctulo"]
    }
    miTienda.cliente_comprar(cliente_2)

    input(15 * "*" + "\n> Presiona enter para probar la siguiente sección")

    ### PARTE 4: Cerrar y cuadrar caja ###
    print("\nPROBANDO PARTE 4: Cerrar la caja tras un día con compras...\n", 15 * "*")

    miTienda.cerrar_por_el_dia()

    input(15 * "*" + "\n> Presiona enter para probar un día sin compras")

    # Por lo que podemos ver, todo salió bien.
    # ¿Pero qué pasará con un día sin compras?

    print("\nPROBANDO PARTE 4: Cerrar la caja tras un día SIN compras...\n", 15 * "*")

    miTienda.cerrar_por_el_dia()

    ### FINAL ###
    print("\n¡Lograste hacer funcionar la caja del Restaurante! Tiqui tiqui ti")
