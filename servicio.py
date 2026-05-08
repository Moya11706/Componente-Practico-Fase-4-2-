class Servicio:

    def __init__(self, nombre, precio_hora):

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if precio_hora <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self.nombre = nombre
        self.precio_hora = precio_hora

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")

        return self.precio_hora * horas

    def mostrar_info(self):

        return (
            f"Servicio: {self.nombre} | "
            f"Precio por hora: ${self.precio_hora}"
        )



# RESERVA DE LA SALA


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_hora, capacidad):

        super().__init__(nombre, precio_hora)

        self.capacidad = capacidad

    def mostrar_info(self):

        return (
            f"Reserva de Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Precio: ${self.precio_hora}/hora"
        )



# ALQUILER DEL EQUIPO


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_hora, tipo_equipo):

        super().__init__(nombre, precio_hora)

        self.tipo_equipo = tipo_equipo

    def mostrar_info(self):

        return (
            f"Alquiler de Equipo: {self.nombre} | "
            f"Tipo: {self.tipo_equipo} | "
            f"Precio: ${self.precio_hora}/hora"
        )



# ASESORÍA TÉCNICA


class AsesoriaTecnica(Servicio):

    def __init__(self, nombre, precio_hora, especialista):

        super().__init__(nombre, precio_hora)

        self.especialista = especialista

    def mostrar_info(self):

        return(
            f"Asesoría Técnica: {self.nombre} | "
            f"Especialista: {self.especialista} | "
            f"Precio: ${self.precio_hora}/hora")
