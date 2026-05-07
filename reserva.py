import abc
import datetime
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

# -------------------------------
# Excepciones personalizadas
# -------------------------------
class ClienteInvalidoError(Exception):
    """Error lanzado cuando un cliente es inválido."""
    pass

class ServicioNoDisponibleError(Exception):
    """Error lanzado cuando un servicio no está disponible."""
    pass

class ReservaError(Exception):
    """Error lanzado cuando ocurre un problema en la reserva."""
    pass

# -------------------------------
# Manejo de logs
# -------------------------------
def registrar_evento(mensaje):
    """Registra eventos y errores en un archivo de logs."""
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")
# -------------------------------
# Clase SistemaReservas
# -------------------------------
class SistemaReservas:
    def __init__(self):
        self._clientes = []
        self._servicios = []
        self._reservas = []

    def agregar_cliente(self, cliente):
        try:
            self._clientes.append(cliente)
            registrar_evento(f"Cliente agregado: {cliente}")
        except ClienteInvalidoError as e:
            registrar_evento(f"Error cliente: {e}")

    def agregar_servicio(self, servicio):
        self._servicios.append(servicio)
        registrar_evento(f"Servicio agregado: {servicio}")

    def crear_reserva(self, cliente, servicio, fecha):
        try:
            if servicio not in self._servicios:
                raise ServicioNoDisponibleError("El servicio no está disponible.")
            reserva = Reserva(cliente, servicio, fecha)
            self._reservas.append(reserva)
            registrar_evento(f"Reserva creada: {reserva}")
        except (ReservaError, ServicioNoDisponibleError) as e:
            registrar_evento(f"Error reserva: {e}")
        except Exception as e:
            registrar_evento(f"Error inesperado: {e}")
        else:
            print("Reserva creada exitosamente.")
        finally:
            print("Operación de reserva finalizada.")
# """"""""""""""""""""""""""""""""""
# Clase abstracta Servicio      -
# -------------------------------
class Servicio(abc.ABC):
    """Clase abstracta que define un servicio genérico."""

    def __init__(self, nombre, precio):
        self._nombre = nombre      # Encapsulación: atributo privado
        self._precio = precio

    @abc.abstractmethod
    def descripcion(self):
        """Método abstracto que debe implementarse en clases derivadas."""
        pass

    def __str__(self):
        return f"{self._nombre} - ${self._precio}"
