class Reserva:
    def __init__(self, cliente, servicio, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.estado = "pendiente"
    def confirmar(self):
        self.estado = "confirmada"
        print("Reserva confirmada")
    def cancelar(self):
        self.estado = "cancelada"
        print("Reserva cancelada")
    def mostrar_reserva(self):
        print("Cliente:", self.cliente.get_nombre())
        print("Servicio:", self.servicio)
        print("Fecha:", self.fecha)
        print("Costo total:", self.servicio.calcular_costo())
        print("Estado:", self.estado)