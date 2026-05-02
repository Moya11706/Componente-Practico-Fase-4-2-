from abc import ABC, abstractmethod 
class Servicio (ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.nombre
    
    @abstractmethod
    def calcular_costo(self):
        pass
    @abstractmethod
    def descripcion(self):
        pass
class ServicioSala(Servicio):
    def __init__(self, horas):
        super().__init__("servicio de sala")
        self.horas = horas
    def calcular_costo(self):
        return self.horas * 50
    def descripcion (self):
        return f"Reserva de sala por {self.horas} horas"
    
    
        