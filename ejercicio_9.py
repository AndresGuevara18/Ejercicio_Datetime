from datetime import datetime, timedelta

print("9) INTERVALO DE FECHAS: Desarrolla un programa que tome dos fechas como entrada y devuelva todas las fechas ",
      "dentro de ese rango")

"""date1 = input("Ingrese la primer fecha (YYYY-MM-DD): ")
date2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""

date1 = "2004-01-01"
date2 = "2024-05-23"

def obtener_fachas_rango(date1, date2):
      # Convertir las cadenas de entrada en objetos datetime
      date1 = datetime.strptime(date1, "%Y-%m-%d")
      date2 = datetime.strptime(date2, "%Y-%m-%d")

      # Inicializar una lista para almacenar las fechas en el rango
      fechas_rango = []

      # Usar un bucle para iterar desde la fecha de inicio hasta la fecha de fi
      primer_fecha = date1

      while primer_fecha <= date2:
            #agregar cada fecha a la lista
            fechas_rango.append(primer_fecha.strftime('%Y-%m-%d'))
            #avanzando un día con timedelta(days=1)
            primer_fecha += timedelta(days=1)
      
      return fechas_rango

fechas = obtener_fachas_rango(date1, date2)


print("Las fechas son:\n")

for i in fechas:
      print(i)

