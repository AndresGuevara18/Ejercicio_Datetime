#Importa las clases necesarias de la librería datetime.
from datetime import datetime, timedelta

print("7) CALCULAR LA FECHA DE INICIO DE LA SEMANA: escribe un programa que tome una fecha y devuelva la fecha del primer dia ",
      "de la semana correspondiente")

#date1 = input("Ingrese la fecha (YYYY-MM-DD):  ")

date1 = "2024-05-17"

# Convertir la cadena de fecha en un objeto datetime
date1 = datetime.strptime(date1, "%Y-%m-%d")
print(date1.strftime('%Y-%m-%d'))

print(f"{date1.day}\n")

# Calcular el primer día de la semana (asumiendo que la semana empieza el lunes)
#El método weekday() en la clase datetime del módulo datetime se utiliza para obtener el día de la semana de un objeto datetime. 
#El valor devuelto es un número entero que representa el día de la semana, donde: 0 corresponde a lunes (Monday) 
#hasta 6 corresponde a domingo (Sunday)

#print(date1.weekday())#numero dia de la semana
start_of_week = date1 - timedelta(days=date1.weekday())
print(start_of_week.strftime('%Y-%m-%d'))
print(start_of_week.day)
