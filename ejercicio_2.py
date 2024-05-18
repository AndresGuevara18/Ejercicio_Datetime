import datetime

print("2) SUMA DE DIAS: crea un programa que tome una fecha y un numero de dias como entrada, luego imprime la fecha resultante",
      " despues de agregar ese numero de dias\n")

# year1 = int(input("Ingrese el año: "))
# mounth1 = int(input("Ingrese el mes: "))
# day1 = int(input("Ingrese el dia: "))

# day2 = int(input("Ingrese el dia: "))

year1 = 2015
mounth1 = 8
day1 = 15

#day2 = -551
day2_sub = int(input("Ingrese los dias que desea restar: "))

def AddDays(year1, mounth1, day1, day2_sub):
    date1 = datetime.datetime(year1, mounth1, day1)
    print(date1)

    sumar = date1 + datetime.timedelta(days= day2_sub)#time delta para sumar o restar en fechas
    print(sumar)
    
def SubtractDays(year1, mounth1, day1, day2_sub):
    date2 = datetime.datetime(year1, mounth1, day1)
    print(date2)
    print("antes de restar")

    restar1 = date2 + datetime.timedelta(days= day2_sub)#time delta para sumar o restar en fechas
    print(f"resta  = {date2} - {datetime.timedelta(days= day2_sub)}")
    print(restar1)


if day2_sub > 0:
    print(f"mas de  0: {day2_sub}")
    AddDays(year1, mounth1, day1, day2_sub)
else:
    print(f"menos de  0: {day2_sub}")
    SubtractDays(year1, mounth1, day1, day2_sub)