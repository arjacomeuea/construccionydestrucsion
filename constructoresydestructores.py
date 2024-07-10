class FileHandler:
    def __init__(self, filename, mode):
        """
        Constructor que inicializa el objeto FileHandler.
        Abre un archivo en el modo especificado.

        :param filename: Nombre del archivo a abrir.
        :param mode: Modo en el que abrir el archivo (e.g., 'r', 'w', 'a').
        """
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode)
        print(f"Archivo '{self.filename}' abierto en modo '{self.mode}'.")

    def write(self, content):
        """
        Escribe contenido en el archivo.

        :param content: Contenido a escribir en el archivo.
        """
        if 'w' in self.mode or 'a' in self.mode:
            self.file.write(content)
            print(f"Contenido escrito en el archivo '{self.filename}'.")
        else:
            print(f"No se puede escribir en el archivo '{self.filename}' en modo '{self.mode}'.")

    def read(self):
        """
        Lee el contenido del archivo.

        :return: Contenido del archivo.
        """
        if 'r' in self.mode:
            return self.file.read()
        else:
            print(f"No se puede leer el archivo '{self.filename}' en modo '{self.mode}'.")
            return None

    def __del__(self):
        """
        Destructor que cierra el archivo cuando el objeto FileHandler se destruye.
        """
        self.file.close()
        print(f"Archivo '{self.filename}' cerrado.")


# Demostración del uso de constructores y destructores
if __name__ == "__main__":
    # Crear una instancia de FileHandler para escribir en un archivo
    writer = FileHandler("example.txt", "w")
    writer.write("Hola, mundo!\n")
    del writer  # Esto llamará al destructor y cerrará el archivo

    # Crear una instancia de FileHandler para leer del archivo
    reader = FileHandler("example.txt", "r")
    content = reader.read()
    print(f"Contenido del archivo: {content}")
    del reader  # Esto llamará al destructor y cerrará el archivo
