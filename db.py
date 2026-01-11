import sqlite3


class ConexionDB:
    def abrir_Conexion(self):
        try:
            self.conexion = sqlite3.connect("db_frases.sqlite")
            return self.conexion
        except Exception as error:
            print(f"Error al abrir la conexion {error}")

    def ingresarInfoCSV(self, datos):
        try:
            conexion = self.abrir_Conexion()
            cursor = conexion.cursor()
            cursor.executemany("insert into frases(contenido)values(?)", datos)
            conexion.commit()
        except Exception as error:
            print(f"Error insertar Registros del csv en la db {error}")
        finally:
            conexion.close()
