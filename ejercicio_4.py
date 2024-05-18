import datetime

print("4) EDAD EN DIAS: Escribe un programa que calcule la edad de una persona en dias, dado la fecha de nacimiento y ",
      "la fecha actual") 

"""year1 = int(input("Ingrese el año de nacimiento: "))
mounth1 = int(input("Ingrese el mes de nacimiento: "))
day1 = int(input("Ingrese el dia de nacimiento: "))"""

year1 = 1991
mounth1 = 10
day1 = 18

ahora = datetime.datetime.now()
year2 = int(ahora.strftime("%Y"))

days = 365

def CalculateDaysBirth(year1, mounth1, day1, year2):
    dif_years = (year2 - year1) - 1
    days_years = dif_years * days
    datebir = datetime.datetime(year1, mounth1, day1)
    
    print(f"año 2: {year2}\nAños cumplidos: {dif_years}\nDias de años: {days_years}\nfecha nacimiento: {datebir}\nFecha actual: {ahora}")

    date1 = int(datebir.strftime("%j"))
    date_now = int(ahora.strftime("%j"))
    print(f"Dias año nacimiento: {date1}\nDias Ahora: {date_now}")

    birth_days = (days_years - date1 ) + date_now
    print(f"Dias de nacimiento - actual: {birth_days}")

if year1 < year2: 
    CalculateDaysBirth(year1, mounth1, day1, year2)