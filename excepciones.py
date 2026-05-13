class ClienteInvalidoError(Exception):
    """Error lanzado cuando un cliente es inválido."""
    pass


class ServicioNoDisponibleError(Exception):
    """Error lanzado cuando un servicio no está disponible."""
    pass


class ReservaError(Exception):
    """Error lanzado cuando ocurre un problema en la reserva."""
    pass

__all__ = ["ClienteInvalidoError", "ServicioNoDisponibleError", "ReservaError"]
