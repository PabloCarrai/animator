import sqlite3


class ConexionDB:
    def abrir_Conexion(self):
        try:
            self.conexion = sqlite3.connect("db_frases.sqlite")
            self.cursor = self.conexion.cursor()
            return self.cursor
        except Exception as error:
            print(f"Error al abrir la conexion {error}")
