import datetime

print("1) DIFERENCIA DE DIAS: escriba un programa que tome dos fechas como entrada y calcule la diferencia en dias entre ellas")

"""year1 = int(input("Ingrese el año: "))
mounth1 = int(input("Ingrese el mes: "))
day1 = int(input("Ingrese el dia: "))

year2 = int(input("\nIngrese el año: "))
mounth2 = int(input("Ingrese el mes: "))
day2 = int(input("Ingrese el dia: "))"""

"""year1 = 1991
mounth1 = 10
day1 = 18

year2 = 2024
mounth2 = 5
day2 = 17

days = 365

#Si la primer fecha es MENOR que la segunda
def CalculateDaysSmaller(year1, mounth1, day1, year2, mounth2, day2):
    dif_year = (year2 - year1) 
    days_years_tot = dif_year * days 

    print(f"años: {dif_year}   dias de años:  {days_years_tot}")

    date1 = datetime.datetime(year1, mounth1, day1)
    date2 = datetime.datetime(year2, mounth2, day2)
    
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days = (days_years_tot - date1_days  ) + date2_days
    
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days}\n DIAS TOTAL: {total_days}")

#si la primer fecha MAYOR que la segunda
def CalculateDaysGreater(year1, mounth1, day1, year2, mounth2, day2):
    dif_year = (year1 - year2) - 1
    days_years_tot = dif_year * days 

    print(f"años: {dif_year}   dias de años:  {days_years_tot}")

    date1 = datetime.datetime(year1, mounth1, day1)
    date2 = datetime.datetime(year2, mounth2, day2)
    
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days = (days_years_tot - date2_days  ) + date1_days
    
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days}\n DIAS TOTAL: {total_days}")

#si el primer mes es MENOR que el segundo
def CalculateMounthSmaller(year1, mounth1, day1, year2, mounth2, day2):
    date1 = datetime.datetime(year1, mounth1, day1)
    date2 = datetime.datetime(year2, mounth2, day2)
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days =  date2_days  - date1_days

    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#Si el primer mes es MAYOR que el segundo
def CalculateMounthGreater(year1, mounth1, day1, year2, mounth2, day2):
    date1 = datetime.datetime(year1, mounth1, day1)
    date2 = datetime.datetime(year2, mounth2, day2)
    print(f"fecha 1: {date1} --- fecha 2: {date2}")
    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days =  date1_days  - date2_days
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#Si el primer dia es MENOR que el segundo
def CalculateDaysDays(year1, mounth1, day1, year2, mounth2, day2):
    date1 = datetime.datetime(year1, mounth1, day1)
    date2 = datetime.datetime(year2, mounth2, day2)
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days =  date2_days  - date1_days

    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#CONDICIONAL
if year1 == year2:
    if mounth1 == mounth2:
        if day1 < day2:
           CalculateDaysDays(year1, mounth1, day1, year2, mounth2, day2) 
    elif mounth1 < mounth2:
        CalculateMounthSmaller(year1, mounth1, day1, year2, mounth2, day2)
    else:
        CalculateMounthGreater(year1, mounth1, day1, year2, mounth2, day2)
elif year1 < year2:
    CalculateDaysSmaller(year1, mounth1, day1, year2, mounth2, day2)
else:
    CalculateDaysGreater(year1, mounth1, day1, year2, mounth2, day2)"""



#1 por la IA
#Importamos la clase datetime desde el módulo datetime.
from datetime import datetime

#Definir la función diferencia_de_dias:
def diferencia_de_dias(fecha1, fecha2):#Parámetros: #La función toma dos fechas como cadenas de caracteres en el formato "YYYY-MM-DD".
    # Convertir las cadenas de entrada en objetos datetime
    #Conversión a datetime: Utilizamos datetime.strptime para convertir las cadenas de fecha en objetos datetime.
    
    #%Y: Año con cuatro dígitos (por ejemplo, 2024)
    #%m: Mes con dos dígitos (01 a 12)
    #%d: Día del mes con dos dígitos (01 a 31)
    #El formato "%Y-%m-%d" especifica que las fechas de entrada deben estar en el formato "Año-Mes-
    fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")#
    fecha2 = datetime.strptime(fecha2, "%Y-%m-%d")
    
    # Calcular la diferencia en días
    #Calcular la diferencia: Calculamos la diferencia en días entre las dos fechas restándolas y tomando el valor absoluto de la diferencia en días usando .days.
    #abs(...) devuelve el valor absoluto de la diferencia en días.
    #.days extrae el número de días de la diferencia.
    #La función abs (abreviatura de "absolute value") se usa para asegurar que la diferencia en días sea siempre un número positivo. Esto es útil porque no importa en qué orden se ingresen las fechas; queremos la cantidad de días entre ellas sin preocuparnos por cuál es anterior o posterior
    #Uso de abs: Garantiza que la diferencia en días sea siempre positiva, sin importar el orden de las fechas ingresadas.
    diferencia = abs((fecha2 - fecha1).days)
    
    return diferencia

# Solicitar al usuario que ingrese las fechas en el formato adecuado
fecha1 = input("Ingrese la primera fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")

# Calcular y mostrar la diferencia en días
dias_diferencia = diferencia_de_dias(fecha1, fecha2)
print(f"La diferencia en días entre {fecha1} y {fecha2} es de {dias_diferencia} días.")