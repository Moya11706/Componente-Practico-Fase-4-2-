from entidad import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):
    def __init__(self, nombre, documento):
        super().__init__(codigo=documento)
        self._nombre = None
        self._documento = None
        self.nombre = nombre
        self.documento = documento

  
    def nombre(self):
        return self._nombre

 
    def nombre(self, valor):
        try:
            valor = Entidad.validar_texto(valor, "nombre")
            if len(valor) < 2:
                raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres.")
            self._nombre = valor
        except ValueError as e:
            raise ClienteInvalidoError(str(e)) from e

   
    def documento(self):
        return self._documento

 
    def documento(self, valor):
        try:
            valor = Entidad.validar_texto(valor, "documento")
            if len(valor) < 4:
                raise ClienteInvalidoError("El documento debe tener al menos 4 caracteres.")
            self._documento = valor
        except ValueError as e:
            raise ClienteInvalidoError(str(e)) from e

    def mostrar_info(self):
        return f"Cliente[{self.codigo}] - Nombre: {self.nombre} | Documento: {self.documento}"

    def __str__(self):
        return self.mostrar_info()
