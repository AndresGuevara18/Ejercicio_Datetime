import datetime

print("5) NUMERO DE DIAS EN UN MES: crea una funcion que tome un mes y un año como entrada y devuelve el numero de dias en ese mes",
      "tener en cuenta el año bisiesto")

from datetime import datetime, timedelta

def numero_de_dias_en_un_mes(mes, año):
    # Calcula la fecha del primer día del mes siguiente
    #Aquí se determina cuál será el primer día del mes siguiente. Si el mes es diciembre (12), el siguiente mes será enero (1) 
    #del próximo año (año + 1). Para cualquier otro mes, simplemente incrementa el mes (mes + 1).
    if mes == 12:
        mes_siguiente = 1
        año_siguiente = año + 1
    else:
        mes_siguiente = mes + 1
        año_siguiente = año
    
    # Fecha del primer día del mes siguiente
    #Crea una fecha para el primer día del mes siguiente usando datetime.
    primer_dia_mes_siguiente = datetime(año_siguiente, mes_siguiente, 1)
    print(primer_dia_mes_siguiente)
    # Fecha del último día del mes actual
    #Resta un día al primer día del mes siguiente para obtener el último día del mes actual. timedelta(days=1) 
    #representa un intervalo de un día.
    ultimo_dia_mes_actual = primer_dia_mes_siguiente - timedelta(days=1)
    print(ultimo_dia_mes_actual)
    
    return ultimo_dia_mes_actual.day

# Ejemplo de uso
mes = 10
año = 2024
print(f"El número de días en el mes {mes} del año {año} es: {numero_de_dias_en_un_mes(mes, año)}")


