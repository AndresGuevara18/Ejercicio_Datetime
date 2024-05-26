from datetime import datetime

print("8) DIFERENCIA DE AÑOS: crea un programa que tome dos fechas como entrada y calcule la diferencia en años entre ellas")

"""fecha1 = input("Ingrese la primer fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""
fecha1 = "1991-10-18"
fecha2 = "2024-05-22"

fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
fecha2 = datetime.strptime(fecha2, "%Y-%m-%d")

print(f"fecha 1: {fecha1} ----  fecha 2: {fecha2}")

year1 = fecha1.year
year2 = fecha2.year

print(f"Año 1: {year1} ----  Año 2: {year2}")

if year1 < year2:
    print(year2 - year1)
else:
    print(year1 - year2)
