#SERVICIOS ESPECIALES 
class Servicio:
    def __init__(self, nombre, precio_origonal):
        self._nombre = nombre
        self._precio_base = precio_original

    def verificar_disponibilidad(self):
        pass


class ErrorServicioInvalido(Exception):
    pass

class ReservaSala(Servicio):
    def __init__(self, nombre: str, precio_original: float, capacidad: int):
        if not isinstance(capacidad, int) or capacidad < 1:
            raise ErrorServicioInvalido(f"Capacidad inválida: {capacidad}")
        super().__init__(nombre, precio_original)
        self._capacidad = capacidad

    
    def capacidad(self) -> int:
        return self._capacidad

    def calcular_costo(self, horas: float, descuento: float = 0.0, **kwargs) -> float:
        self.verificar_disponibilidad()

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ErrorServicioInvalido(f"Horas inválidas: {horas}")
        if not (0 <= descuento <= 100):
            raise ErrorServicioInvalido(f"Descuento inválido: {descuento}")

        costo = self._precio_base * horas * (1-descuento / 100)
        logger.debug(f"Sala '{self._nombre}': {horas}h × ${self._precio_base:,.0f} - {descuento}% = ${costo:,.0f}")
        return round(costo, 2)

    def describir(self) -> str:
        return f"Sala de reuniones | Capacidad: {self._capacidad} personas"


class AlquilerEquipo(Servicio):
    IVA = 0.19

    def __init__(self, nombre: str, precio_base: float, tipo_equipo: str):
        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ErrorServicioInvalido("El tipo de equipo no puede estar vacío.")
        super().__init__(nombre, precio_base)
        self._tipo_equipo = tipo_equipo.strip()

    
    def tipo_equipo(self) -> str:
        return self._tipo_equipo

    def calcular_costo(self, horas: float, con_seguro: bool = False, **kwargs) -> float:
        self.verificar_disponibilidad()

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ErrorServicioInvalido(f"Horas inválidas: {horas}")

        costo_base = self._precio_base * horas
        costo_iva = costo_base * self.IVA
        recargo_seguro = costo_base * 0.10 if con_seguro else 0.0
        costo_final = costo_base + costo_iva + recargo_seguro

        logger.debug(f"Equipo '{self._nombre}': {horas}h × ${self._precio_base:,.0f} + IVA + seguro={'Sí' if con_seguro else 'No'} = ${costo_final:,.0f}")
        return round(costo_final, 2)

    def describir(self) -> str:
        return f"Alquiler de equipo | Tipo: {self._tipo_equipo} | IVA incluido: {int(self.IVA * 100)}%"


class AsesoriaTecnica(Servicio):
    NIVELES = {
        "básico":     1.0,
        "intermedio": 1.5,
        "avanzado":   2.0,
    }

    def __init__(self, nombre: str, precio_base: float, especialidad: str):
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorServicioInvalido("La especialidad no puede estar vacía.")
        super().__init__(nombre, precio_base)
        self._especialidad = especialidad.strip()

    
    def especialidad(self) -> str:
        return self._especialidad

    def calcular_costo(self, horas: float, nivel: str = "básico", **kwargs) -> float:
        self.verificar_disponibilidad()

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ErrorServicioInvalido(f"Horas inválidas: {horas}")

        nivel_lower = nivel.lower().strip()
        if nivel_lower not in self.NIVELES:
            raise ErrorServicioInvalido(f"Nivel '{nivel}' no válido. Opciones: {list(self.NIVELES.keys())}")

        costo = self._precio_base * horas * self.NIVELES[nivel_lower]
        logger.debug(f"Asesoría '{self._nombre}': {horas}h × ${self._precio_base:,.0f} × {self.NIVELES[nivel_lower]} ({nivel}) = ${costo:,.0f}")
        return round(costo, 2)

    def describir(self) -> str:
        niveles_str = " | ".join(f"{n}: x{m}" for n, m in self.NIVELES.items())
        return f"Asesoría Técnica | Especialidad: {self._especialidad} | Niveles: [{niveles_str}]"



from abc import ABC, abstractmethod 
class Servicio (ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    
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
    
    
        
