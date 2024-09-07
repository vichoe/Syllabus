class Vehiculo:
    identificador = 0

    def __init__(self, rendimiento: int, marca: str, energia=111.5, *args, **kwargs) -> None:
        self.rendimiento = rendimiento
        self.marca = marca
        if energia < 0:
            energia = float(0)
            # cmtre me costo entender que si el valor de energia empezaba bajo cero, LO TENIA QUE SETTEAR ACA AAAAAAA
        self.energia = energia
        self.identificador = Vehiculo.identificador
        Vehiculo.identificador += 1
    
    @property
    def autonomia(self) -> float:
        return self._energia * self.rendimiento
    
    @property
    def energia(self) -> float:
        return self._energia
    
    @energia.setter
    def energia(self, n):
        n = round(n, 1)
        if n < 0:
            n = 0
        self._energia = n

class AutoBencina(Vehiculo):
    def __init__(self, bencina_favorita: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # por darme autoferiados no sabia q era args y kwargs...
        self.bencina_favorita = bencina_favorita

    def recorrer(self, kilometros) -> str:
        # voy a checkar si la autonomia del auto le da para poder recorrer los kilometros, si no imposible
        if self.autonomia >= kilometros:
            gasto = kilometros / self.rendimiento
        else: 
            kilometros = self.autonomia
            gasto = kilometros / self.rendimiento
        self.energia -= gasto
        gasto = round(gasto, 1)
        return f"Anduve {kilometros}Km y eso consume {gasto}L de bencina"

# Voy a poner un parentesis aqui. Estuve MEDIA HORA pensando pq no me heredaba la clase Vehiculo, y resulta que se me olvido poner los parentesis despues de class AutoBencina....

class AutoElectrico(Vehiculo):
    def __init__(self, vida_util_bateria: int=5, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vida_util_bateria = vida_util_bateria
    
    def recorrer(self, kilometros) -> str:
        if self.autonomia >= kilometros:
            gasto = kilometros / self.rendimiento
        else:
            kilometros = self.autonomia
            gasto = kilometros / self.rendimiento
        gasto = round(gasto, 1)
        self.energia -= gasto
        return f"Anduve {kilometros}Km y eso consume {gasto}W de energia electrica"

class Camioneta(AutoBencina):
    def __init__(self, capacidad_maleta: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.capacidad_maleta = capacidad_maleta

class Telsa(AutoElectrico):
    def recorrer (self, kilometros):
        return super().recorrer(kilometros) + " de forma muy inteligente"

# Otro parentesis, ESTABA DEFINIENDO LA CLASE COMO UN __INIT__ Y NO SABIA PQ NO FUNCIONABA

class FaitHibrido(AutoBencina, AutoElectrico):
    def __init__(self, *args, **kwargs) -> None:
        AutoBencina.__init__(self, *args, *kwargs)
        AutoElectrico.__init__(self, vida_util_bateria=5, *args, **kwargs)
    
    def recorrer(self, kilometros) -> str:
        # primero separamos los dos casos!
        if kilometros <= 10:
            return AutoElectrico.recorrer(self, kilometros)
        else:
            return AutoBencina.recorrer(self, 10) + " " + AutoElectrico.recorrer(self, kilometros - 10)