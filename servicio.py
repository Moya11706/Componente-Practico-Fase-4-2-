import abc

class Servicio(abc.ABC):

    def __init__(self, nombre, precio_hora):

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if precio_hora <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self._nombre = nombre
        self._precio_hora = precio_hora

    # 🔹 Getter (encapsulación)
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio_hora

    # 🔹 Método con polimorfismo
    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")

        if descuento < 0 or descuento > 100:
            raise ValueError("Descuento inválido")

        costo = self._precio_hora * horas
        costo_final = costo - (costo * (descuento / 100))

        return round(costo_final, 2)

    # 🔹 Método abstracto
    @abc.abstractmethod
    def describir(self):
        pass

    def __str__(self):
        return f"{self._nombre} - ${self._precio_hora}/hora"


# -------------------------
# RESERVA DE SALA
# -------------------------

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_hora, capacidad):
        super().__init__(nombre, precio_hora)

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero")

        self.capacidad = capacidad

    def describir(self):
        return f"Sala con capacidad para {self.capacidad} personas"


# -------------------------
# ALQUILER DE EQUIPO
# -------------------------

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_hora, cantidad):
        super().__init__(nombre, precio_hora)

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.cantidad = cantidad

    def describir(self):
        return f"Alquiler de {self.cantidad} equipos"


# -------------------------
# ASESORÍA TÉCNICA
# -------------------------

class AsesoriaTecnica(Servicio):

    def __init__(self, nombre, precio_hora, especialista):
        super().__init__(nombre, precio_hora)

        if not especialista.strip():
            raise ValueError("El especialista no puede estar vacío")

        self.especialista = especialista

    def describir(self):
        return f"Asesoría con especialista: {self.especialista}"
