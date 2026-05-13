from Entidad_Base import Entidad
from excepciones import ClienteInvalidoError

class Cliente(Entidad):
    def __init__(self, nombre, email, documento):
        super().__init__(codigo=documento)
        self._nombre = None
        self._email = None
        self._documento = None
        self.nombre = nombre
        self.email = email
        self.documento = documento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        try:
            valor = Entidad.validar_texto(valor, "nombre")
            if len(valor) < 2:
                raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres.")
            self._nombre = valor
        except ValueError as e:
            raise ClienteInvalidoError(str(e)) from e

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        try:
            valor = Entidad.validar_texto(valor, "email")
            if "@" not in valor:
                raise ClienteInvalidoError("El email debe contener '@'.")
            self._email = valor
        except ValueError as e:
            raise ClienteInvalidoError(str(e)) from e

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        try:
            valor = Entidad.validar_texto(valor, "documento")
            if len(valor) < 4:
                raise ClienteInvalidoError("El documento debe tener al menos 4 caracteres.")
            self._documento = valor
        except ValueError as e:
            raise ClienteInvalidoError(str(e)) from e

    def mostrar_info(self):
        return f"Cliente[{self.codigo}] - Nombre: {self.nombre} | Email: {self.email} | Documento: {self.documento}"

    def get_nombre(self):
        return self._nombre

    def __str__(self):
        return self.mostrar_info()
