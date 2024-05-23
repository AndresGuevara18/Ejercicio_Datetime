from datetime import datetime, timedelta

print("10) FECHA DE VENCIMIENTO: Escribe un programa que tome una fecha de inicio y un numero de dias como entrada y calcule ",
      "la fecha de vencimiento añadiendo esos dias a la fecha de inicio")

"""date1 = input("Ingrese la fecha (YYYY-MM-DD): ")
days = int(input("Ingrese el numero de dias: "))"""

date1 = "2024-05-23"
days_more = 25

date1 = datetime.strptime(date1, "%Y-%m-%d")
print(date1)

fecha_vencimiento = date1 + timedelta(days=days_more)

print(f"Fecha vencimiento: {fecha_vencimiento}")



