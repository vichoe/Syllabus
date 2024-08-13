

class Predio:
    def __init__(self, codigo_predio: str, alto: int, ancho: int) -> None:
        self.codigo_predio = codigo_predio
        self.alto = alto
        self.ancho = ancho
        self.plano = []
        self.plano_riego = []

    def crear_plano(self, tipo: str) -> None:
        pass

    def plantar(
        self, codigo_cultivo: int, coordenadas: list, alto: int, ancho: int
    ) -> None:
        pass

    def regar(self, coordenadas: list, area: int) -> None:
        pass

    def eliminar_cultivo(self, codigo_cultivo: int) -> int:
        pass


class DCCultivo:
    def __init__(self) -> None:
        self.predios = []

    def crear_predios(self, nombre_archivo: str) -> str:
        pass

    def buscar_y_plantar(self, codigo_cultivo: int, alto: int, ancho: int) -> bool:
        pass

    def buscar_y_regar(self, codigo_predio: str, coordenadas: list, area: int) -> None:
        pass

    def detectar_plagas(self, lista_plagas: list[list]) -> list[list]:
        pass
