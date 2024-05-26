from datetime import datetime, timedelta

print("6) PROXIMA FECHA DE UN DIA DE LA SEMANA: desarrolla un programa que, dada una fecha y un dia de la semana, calcule la ",
      "proxima fecha en la que ocurra ese dia en la semana")

# Ejemplo de uso
"""fecha_inicial = input("Introduce la fecha inicial (YYYY-MM-DD): ")
dia_semana = input("Introduce el día de la semana: ")"""


def proxima_fecha_dia_semana(fecha_inicial, dia_semana):
    # Convertir la cadena de fecha a un objeto datetime
    fecha_inicial = datetime.strptime(fecha_inicial, '%Y-%m-%d')
    
    # Diccionario para mapear nombres de días de la semana a índices
    dias_semana = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'domingo': 6
    }
    
    # Obtener el índice del día de la semana buscado
    #La función lower() en Python se utiliza para convertir todos los caracteres de una cadena de texto a minúsculas. 
    dia_semana_buscado = dias_semana[dia_semana.lower()]
    
    # Calcular la diferencia de días hasta el próximo día de la semana
    #La función weekday() es un método del objeto datetime en Python que devuelve el día de la semana de una fecha específica. 
    #Los días de la semana se representan como enteros donde el lunes es 0 y el domingo es 6.

    #El uso del operador % 7 garantiza que la diferencia de días sea siempre un número positivo en el rango de 0 a 6. Esto es 
    #importante porque queremos un número de días que sea válido en el contexto de una semana (máximo 6 días de diferencia).
    diferencia_dias = (dia_semana_buscado - fecha_inicial.weekday() + 7) % 7 #% pra diferencia entre el valor obtenido de 
    if diferencia_dias == 0:
        diferencia_dias = 7  # Si la diferencia es 0, significa que es hoy, así que se busca el próximo
    
    # Calcular la próxima fecha
    proxima_fecha = fecha_inicial + timedelta(days=diferencia_dias)
    
    return proxima_fecha.strftime('%Y-%m-%d')


fecha_inicial = "2024-05-02"
dia_semana = "jueves"

proxima_fecha = proxima_fecha_dia_semana(fecha_inicial, dia_semana)

print(f"La próxima fecha que es {dia_semana} después de {fecha_inicial} es {proxima_fecha}.")
