from datetime import datetime

print("3) DIA DE LA SEMANA: desarrolla un programa que dada una fecha, determine el dia de la semana correspondiente ",
      "(Lunes, martes, miercoles, etc... )\n")

#date1 = input("Ingrese la fecha (YYYY-MM-DD): ")

date1 = "1991-10-18"

date1 = datetime.strptime(date1, "%Y-%m-%d")
print(date1.strftime('%Y-%m-%d'))

print(date1.strftime("%A"))