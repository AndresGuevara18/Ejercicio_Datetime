import datetime

print("3) DIA DE LA SEMANA: desarrolla un programa que dada una fecha, determine el dia de la semana correspondiente ",
      "(Lunes, martes, miercoles, etc... )\n")

# year1 = int(input("Ingrese el año: "))
# mounth1 = int(input("Ingrese el mes: "))
# day1 = int(input("Ingrese el dia: "))

year1 = 2024
mounth1 = 5
day1 = 16

date1 = datetime.datetime(year1, mounth1, day1)
print(date1)

print(date1.strftime("%A"))