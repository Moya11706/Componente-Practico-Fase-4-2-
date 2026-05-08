class Cliente:

    def __init__(self, nombre, documento):

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not documento.strip():
            raise ValueError("El documento no puede estar vacío")

        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Documento: {self.__documento}"

    def __str__(self):
        return f"{self.__nombre} ({self.__documento})"
