#Importamos la clase datetime desde el módulo datetime.
from datetime import datetime

print("1) DIFERENCIA DE DIAS: escriba un programa que tome dos fechas como entrada y calcule la diferencia en dias entre ellas")

#Definir la función diferencia_de_dias:
def diferencia_de_dias(fecha_i, fecha_x):#Parámetros: #La función toma dos fechas como cadenas de caracteres en el formato "YYYY-MM-DD".
    # Convertir las cadenas de entrada en objetos datetime
    #Conversión a datetime: Utilizamos datetime.strptime para convertir las cadenas de fecha en objetos datetime.
    
    #%Y: Año con cuatro dígitos (por ejemplo, 2024)
    #%m: Mes con dos dígitos (01 a 12)
    #%d: Día del mes con dos dígitos (01 a 31)
    #El formato "%Y-%m-%d" especifica que las fechas de entrada deben estar en el formato "Año-Mes-
    fecha_i = datetime.strptime(fecha_i, "%Y-%m-%d")
    fecha_x = datetime.strptime(fecha_x, "%Y-%m-%d")

    print(f"Primer fecha: {fecha_i.strftime('%Y-%m-%d')}\nSegunda fecha: {fecha_x.strftime('%Y-%m-%d')}\n")
    
    # Calcular la diferencia en días
    #Calcular la diferencia: Calculamos la diferencia en días entre las dos fechas restándolas y tomando el valor absoluto de la diferencia en días usando .days.
    #abs(...) devuelve el valor absoluto de la diferencia en días.
    #.days extrae el número de días de la diferencia.
    #La función abs (abreviatura de "absolute value") se usa para asegurar que la diferencia en días sea siempre un número positivo. Esto es útil porque no importa en qué orden se ingresen las fechas; queremos la cantidad de días entre ellas sin preocuparnos por cuál es anterior o posterior
    #Uso de abs: Garantiza que la diferencia en días sea siempre positiva, sin importar el orden de las fechas ingresadas.
    diferencia = abs((fecha_x - fecha_i).days)
    print(f"La diferencia en días entre {fecha1} y {fecha2} es de => {diferencia} días.")
    return diferencia

# Solicitar al usuario que ingrese las fechas en el formato adecuado
"""fecha1 = input("Ingrese la primera fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""

#Variables prueba
fecha1 = "1991-10-18"
fecha2 = "2024-05-26"

# Cllamado funcion
diferencia_de_dias(fecha1, fecha2)