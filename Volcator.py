#   Me traigo el modulo csv
import csv
from db import ConexionDB

#   Lista auxiliar en donde guardo las frases
datos = []
#   Abro el csv para traerme el contenido
with open("frasesEnArchivos.csv", mode="r", encoding="utf-8") as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        if fila:
            datos.append(fila[0])
#   Elementos formateados para meterlos en la db
datos_formateados = [(elemento,) for elemento in datos]
conexion = ConexionDB()
resultados = conexion.ingresarInfoCSV(datos_formateados)
print("Datos Ingresados")
