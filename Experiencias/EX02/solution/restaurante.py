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
            # nombre, precio = item.split(",")
            # self.caja.ingresar_producto(nombre, precio)

            # Segunda versión.
            # Esta arregla el TypeError, pero lanza un Value Error.
            # nombre, precio = item.split(",")
            # precio = int(precio)
            # self.caja.ingresar_producto(nombre, precio)

            # Tercera versión.
            # Esta arreglará el ValueError, pero lanza otro en un siguiente elemento.
            # nombre, precio = item.split(",")
            # precio = float(precio)
            # self.caja.ingresar_producto(nombre, precio)

            # Versión Final:
            # Esta cubre cualquier caso en general.
            # ¿Puede hacerse con if/else? Por supuesto, pero esta clase es para mostrar
            # try/except, así que esta solución lo usa.
            nombre, precio = item.split(",")
            try:
                # Intentamos cargar el producto con el valor como float.
                precio = float(precio)
                self.caja.ingresar_producto(nombre, precio)
            except ValueError:
                # Si es un value error, damos un mensaje un poco más explicativo.
                print(
                    f"\nError: el precio \"{precio}\" del producto {nombre} "
                    "no puede ser convertido a número flotante positivo.")
                print(
                    f"El producto {nombre} no se agregará al stock de productos.\n")
            except Exception as e:
                # Ponemos la excepción genérica en caso de que ocurra algún error desconocido.
                # OJO: la excepción genérica se usa solo como última opción, y debido a que
                # estamos trabajando con un módulo externo de comportamiento desconocido.
                print(
                    "Error: ocurrió la siguiente excepcion al tratar de cargar el archivo.")
                print(e)
                print(
                    f"El producto {nombre} no se agregará al stock de productos.")
            else:
                # Si el try funcionó, imprimimos un mensaje que confirme la acción
                print(
                    f"El producto {nombre} se agregó correctamente "
                    f"al stock de productos con un precio de {precio}.")

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

        ## PARTE 2 Y 3: COMPLETAR ##
        # ¿Qué error nos lanza al probar la sección 1.2?
        # Una vez arreglado lo anterior, ¿Qué error nos lanzará al probar la sección 1.3?
        # self.caja.procesar_compra(
        #     cliente['nombre'], cliente['compras'], cliente['rut'])

        # PARTE 2: Deberíamos encontrar un FileNotFound error al no tener la carpeta
        # donde almacenar las boletas.
        # Podemos hacer 3 cosas:
        #       - Crear a mano la carpeta antes de correr el programa (¿Por qué no escala esto?)
        #       - Con os.makedirs() generar la carpeta antes de ejecutar el método
        #           (¿Estamos seguros que siempre será el mismo nombre de carpeta?)
        #       - Agregar un try/except del cual obtendremos el nombre de la carpeta necesario. (Haremos este)
        # Así que en el bloque try probaremos el método, si hay error crearemos la carpeta y reintentaremos la operación.
        # Si no hay error, pongo un bloque else para avisar que la operación fue exitosa.
        try:
            # Intentamos la línea anterior
            self.caja.procesar_compra(
                cliente['nombre'], cliente['compras'], cliente['rut'])
        # Viendo el nombre del error que nos salió, haremos un flujo para capturar el FileNotFoundError
        except FileNotFoundError as e:
            # dir(e) nos muestra métodos y properties de una clase. Podemos espiarlo para ver algo de interés
            # (En este caso, notamos unas properties llamadas "filename")
            # print(dir(e))

            # Recopilamos la ruta que nos falló
            nombre_ruta = e.filename
            # Con esto, obtenemos la ruta al directorio (sin el archivo final)
            path_al_archivo = os.path.dirname(nombre_ruta)
            # Creo el archivo
            os.makedirs(path_al_archivo)

            # Hago un nuevo intento del método
            # ¿Por qué me llamo a mi mismo?
            # Para poder entrar al try de nuevo sin tener que hacer try's nesteados.
            self.cliente_comprar(cliente)

        # PARTE 3: El segundo cliente debería lanzar un KeyError. Agregamos ese bloque extra al método.
        # Como no tenemos una forma fácil de ver los productos cargados en cualquier momento dado,
        # manejaremos el caso donde se pida algo que no es de los productos con un try/except
        except KeyError as e:
            # De nuevo dir(e) nos mostrará algo útil: una propery args, cuyo valor es la llave que falló.
            # print(dir(e))

            # Encontramos la llave fallida
            elemento_fallido = e.args[0]
            # Añadimos un mensaje de qué hará el programa
            print(
                f"No se encontró el producto {elemento_fallido}. Se eliminará de la canasta.")
            # Hacemos una copia del cliente sin ese elemento en sus compras y hago un nuevo intento
            # de este método
            cliente_nuevo = copy.deepcopy(cliente)
            cliente_nuevo["compras"].remove(elemento_fallido)

            self.cliente_comprar(cliente_nuevo)
        else:
            # Este else se activa si logré procesar la compra sin levantar errores.
            print(
                "La compra fue realizada exitosamente. Tu boleta se ha descargado como archivo .txt")

    def cerrar_por_el_dia(self) -> None:
        """
        Método que cierra la caja por el día y da las estadísticas de las compras diarias.
        Cualquier nueva compra corresponde al día siguiente

        PARTE 4: El método funciona perfectamente cuando gente compra en un día.
        ¿Pero qué pasa en un día sin ventas? 
        Deberemos arreglarlo con un try/Except o un if/else.
        """
        ## PARTE 4: COMPLETAR ##
        # Habrá un ZeroDivisionError en días sin compras por el método cuadrar_caja().
        # Así que envolveremos todo en un try/except/finally.
        # ¿Podría hacerse con un if/else? Por supuesto, pero así probamos el finally.

        # Código original.
        # self.caja.cuadrar_caja()
        # self.caja.cerrar_caja()

        try:
            # Trato de cuadrar la caja
            self.caja.cuadrar_caja()
        except ZeroDivisionError:
            # Como no hubieron clientes, lo mencionamos en un texto adicional
            print("No hubieron clientes hoy, así que la caja se mantuvo igual.")
        finally:
            # Sin importar si hubieron clientes o no, pasamos de día
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
