import datetime

print("5) NUMERO DE DIAS EN UN MES: crea una funcion que tome un mes y un año como entrada y devuelve el numero de dias en ese mes",
      "tener en cuenta el año bisiesto")

from datetime import datetime, timedelta

def numero_de_dias_en_un_mes(mes, año):
    # Calcula la fecha del primer día del mes siguiente
    if mes == 12:
        mes_siguiente = 1
        año_siguiente = año + 1
    else:
        mes_siguiente = mes + 1
        año_siguiente = año
    
    # Fecha del primer día del mes siguiente
    primer_dia_mes_siguiente = datetime(año_siguiente, mes_siguiente, 1)
    # Fecha del último día del mes actual
    ultimo_dia_mes_actual = primer_dia_mes_siguiente - timedelta(days=1)
    
    return ultimo_dia_mes_actual.day

# Ejemplo de uso
mes = 2
año = 2024
print(f"El número de días en el mes {mes} del año {año} es: {numero_de_dias_en_un_mes(mes, año)}")


"""#Importar el módulo calendar: Este módulo tiene varias funciones útiles para trabajar con fechas.
import calendar

#Definir la función numero_de_dias_en_un_mes: Esta función toma dos parámetros: mes y año.
def numero_de_dias_en_un_mes(mes, año):
    # calendar.monthrange devuelve una tupla del primer día del mes y el número de días en el mes
    #Utilizar calendar.monthrange: Esta función toma el año y el mes como argumentos y devuelve una tupla. El primer elemento 
    #de la tupla es el día de la semana del primer día del mes (que no nos interesa para este problema) y el segundo elemento es el número de días en el mes.
    #Desglose
    #    -calendar.monthrange(año, mes) devuelve una tupla (primer_dia_semana, numero_de_dias):
    #    -primer_dia_semana: El día de la semana del primer día del mes (0 es lunes, 6 es domingo).
    #    -numero_de_dias: El número de días en el mes.
    #    -En el contexto de tu problema, sólo te interesa el número de días en el mes (numero_de_dias). Como no necesitas el primer valor (primer_dia_semana), utilizas el subrayado (_) para ignorarlo.
    _, num_dias = calendar.monthrange(año, mes)#_, En este caso específico, se está utilizando para ignorar el primer valor devuelto por la función calendar.monthrange.
    return num_dias

# Ejemplo de uso
mes = 2
año = 2024
print(f"El número de días en el mes {mes} del año {año} es: {numero_de_dias_en_un_mes(mes, año)}")"""

"""
print(numero_de_dias_en_un_mes(1, 2023))  # Enero 2023: 31 días
print(numero_de_dias_en_un_mes(2, 2023))  # Febrero 2023: 28 días (no bisiesto)
print(numero_de_dias_en_un_mes(2, 2024))  # Febrero 2024: 29 días (bisiesto)
print(numero_de_dias_en_un_mes(4, 2024))  # Abril 2024: 30 días
"""

