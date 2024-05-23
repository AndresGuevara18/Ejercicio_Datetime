from datetime import datetime

print("3) DIA DE LA SEMANA: desarrolla un programa que dada una fecha, determine el dia de la semana correspondiente ",
      "(Lunes, martes, miercoles, etc... )\n")

# year1 = int(input("Ingrese el año: "))
# mounth1 = int(input("Ingrese el mes: "))
# day1 = int(input("Ingrese el dia: "))

date1 = input("Ingrese la fecha (YYYY-MM-DD): ")

date1 = datetime.strptime(date1, "%Y-%m-%d")
print(date1)

print(date1.strftime("%A"))