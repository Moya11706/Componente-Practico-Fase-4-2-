from abc import ABC, abstractmethod
from uuid import uuid4


class Entidad(ABC):
    def __init__(self, codigo=None):
        if codigo is None or not str(codigo).strip():
            self._codigo = uuid4().hex[:8].upper()
        else:
            self._codigo = str(codigo).strip()

    
    @property
    def codigo(self):
        return self._codigo

    @staticmethod
    def validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        return valor.strip()

    @abstractmethod
    def mostrar_info(self):
        pass
