from datetime import datetime, timedelta

print("2) SUMA DE DÍAS: Crea un programa que tome una fecha y un número de días como entrada, luego imprime la fecha resultante después de agregar ese número de días\n")

# Leer la fecha de inicio y el número de días (puedes descomentar las líneas siguientes si deseas ingresar los valores manualmente)
# fecha1 = input("Ingrese la fecha (YYYY-MM-DD):")
# num_days = int(input("Ingrese los días: "))

# Usar valores predefinidos para propósitos de demostración
fecha1 = "2024-05-02"
num_days = 30

# Convertir la cadena de fecha en un objeto datetime
fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
year1 = fecha1.year

print(f"Fecha: {fecha1.strftime('%Y-%m-%d')} --- Año: {year1}")

# Función para sumar días a una fecha e imprimir la nueva fecha
def add_days(fecha, dias):
    nueva_fecha = fecha + timedelta(days=dias)
    
    print(f"Dias: {dias}\nFecha resultante: {datetime.strftime(nueva_fecha, '%Y-%m-%d')}")
    return nueva_fecha

# Calcular e imprimir la nueva fecha
add_days(fecha1, num_days)

"""year1 = 2015
mounth1 = 8
day1 = 15

#day2 = -551
day2_sub = int(input("Ingrese los dias que desea restar: "))

def AddDays(year1, mounth1, day1, day2_sub):
    date1 = datetime.datetime(year1, mounth1, day1)
    print(date1)

    sumar = date1 + datetime.timedelta(days= day2_sub)#time delta para sumar o restar en fechas
    print(sumar)
    
def SubtractDays(year1, mounth1, day1, day2_sub):
    date2 = datetime.datetime(year1, mounth1, day1)
    print(date2)
    print("antes de restar")

    restar1 = date2 + datetime.timedelta(days= day2_sub)#time delta para sumar o restar en fechas
    print(f"resta  = {date2} - {datetime.timedelta(days= day2_sub)}")
    print(restar1)


if day2_sub > 0:
    print(f"mas de  0: {day2_sub}")
    AddDays(year1, mounth1, day1, day2_sub)
else:
    print(f"menos de  0: {day2_sub}")
    SubtractDays(year1, mounth1, day1, day2_sub)"""