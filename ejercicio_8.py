from datetime import datetime

print("8) DIFERENCIA DE AÑOS: crea un programa que tome dos fechas como entrada y calcule la diferencia en años entre ellas")

"""fecha1 = input("Ingrese la primer fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""
fecha1 = "2000-10-18"
fecha2 = "1995-05-22"

fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
fecha2 = datetime.strptime(fecha2, "%Y-%m-%d")

print(f"fecha 1: {fecha1.strftime('%Y-%m-%d')} ----  fecha 2: {fecha2.strftime('%Y-%m-%d')}")

year1 = fecha1.year
year2 = fecha2.year

print(f"Año 1: {year1} ----  Año 2: {year2}")

if year1 < year2:
    print(year2 - year1)
else:
    print(year1 - year2)



"""
# Fechas de entrada
fecha1 = "1991-10-18"
fecha2 = "2024-05-22"

# Convertir las cadenas de entrada en objetos datetime
fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
fecha2 = datetime.strptime(fecha2, "%Y-%m-%d")

# Imprimir las fechas analizadas
print(f"Fecha 1: {fecha1.strftime('%Y-%m-%d')} ----  Fecha 2: {fecha2.strftime('%Y-%m-%d')}")

# Extraer los años
año1 = fecha1.year
año2 = fecha2.year

# Calcular la diferencia en años
diferencia_en_años = año2 - año1

# Ajustar si la segunda fecha no ha alcanzado el mismo mes y día que la primera fecha
if (fecha2.month, fecha2.day) < (fecha1.month, fecha1.day):
    diferencia_en_años -= 1

print(f"Diferencia en años: {diferencia_en_años}")

"""