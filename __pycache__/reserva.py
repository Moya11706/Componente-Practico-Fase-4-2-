from excepciones import ReservaError
import datetime

class Reserva:
    def __init__(self, cliente, servicio, fecha, horas=1):
        # Validaciones
        if cliente is None:
            raise ReservaError("El cliente no puede ser nulo")

        if servicio is None:
            raise ReservaError("El servicio no puede ser nulo")

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores a 0")

        if not isinstance(fecha, datetime.date):
            raise ReservaError("La fecha debe ser válida")

        # Atributos privados (encapsulación)
        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._horas = horas
        self._estado = "pendiente"

    # -------------------------
    # PROPIEDADES (GETTERS)
    # -------------------------

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @property
    def horas(self):
        return self._horas

    @property
    def estado(self):
        return self._estado

    # -------------------------
    # MÉTODOS DE NEGOCIO
    # -------------------------

    def confirmar(self):
        self._estado = "confirmada"

    def cancelar(self):
        self._estado = "cancelada"

    def calcular_total(self):
        return self._servicio.calcular_costo(self._horas)

    # -------------------------
    # REPRESENTACIÓN
    # -------------------------

    def mostrar_reserva(self):
        return (
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio}\n"
            f"Fecha: {self._fecha}\n"
            f"Horas: {self._horas}\n"
            f"Costo total: ${self.calcular_total()}\n"
            f"Estado: {self._estado}"
        )

    def __str__(self):
        return self.mostrar_reserva()