from datetime import datetime

print("1) DIFERENCIA DE DIAS: escriba un programa que tome dos fechas como entrada y calcule la diferencia en dias entre ellas")

"""fecha1 = input("Ingrese la primera fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""

"""#DaysSmaller
date1 = "1991-10-18"
date2 = "2024-05-17"
"""

"""#DaysGreater
date1 = "2024-05-17"
date2 = "1991-10-18"
"""

"""#MounthSmaller
date1 = "2022-05-17"
date2 = "2022-06-27"
"""

#MounthGreater
date1 = "2022-06-27"
date2 = "2022-06-17"

date1 = datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

print(f"Fecha 1: {date1} --- Fecha 2: {date2}")

year1 = int(date1.strftime("%Y"))
mounth1 = int(date1.strftime("%m"))
day1 = int(date1.strftime("%d"))

year2 = int(date2.strftime("%Y"))
mounth2 = int(date2.strftime("%m"))
day2 = int(date2.strftime("%d"))

print(f"Año 1 : {year1} Mes: {mounth1}  Dia {day1}--- Año 2: {year2} Mes: {mounth2}  Dia {day2}")

days = 365

#Si la primer fecha es MENOR que la segunda
def CalculateDaysSmaller(year1, year2):
    dif_year = (year2 - year1) 
    days_years_tot = dif_year * days 

    print(f"años: {dif_year}   dias de años:  {days_years_tot}")
    
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days = (days_years_tot - date1_days  ) + date2_days
    
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days}\n DIAS TOTAL: {total_days}")

#si la primer fecha MAYOR que la segunda
def CalculateDaysGreater(year1, year2):
    dif_year = (year1 - year2)
    days_years_tot = dif_year * days 

    print(f"años: {dif_year}   dias de años:  {days_years_tot}")
    
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days = (days_years_tot - date2_days  ) + date1_days
    
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days}\n DIAS TOTAL: {total_days}")

#si el primer mes es MENOR que el segundo
def CalculateMounthSmaller(date1, date2):
    
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days =  date2_days  - date1_days

    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#Si el primer mes es MAYOR que el segundo
def CalculateMounthGreater(date1, date2):
    print(f"fecha 1: {date1} --- fecha 2: {date2}")
    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days =  date1_days  - date2_days
    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#Si el primer dia es MENOR que el segundo
def CalculateDaysDaysSmaller(date1, date2):
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days =  date2_days  - date1_days

    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#Si el primer dia es MAYOR que el segundo
def CalculateDaysDaysGreater(date1, date2):
    print(f"fecha 1: {date1} --- fecha 2: {date2}")

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))

    total_days =  date1_days - date2_days 

    print(f"Fecha 1 dias transcurridos: {date1_days}\nfecha 2 dias transcurridos: {date2_days} \n DIAS TOTAL: {total_days}")

#CONDICIONAL
if year1 == year2:
    if mounth1 == mounth2:
        if day1 < day2:
           CalculateDaysDaysSmaller(date1, date2)
        else:
            CalculateDaysDaysGreater(date1, date2)
    elif mounth1 < mounth2:
        CalculateMounthSmaller(date1, date2)
    else:
        CalculateMounthGreater(date1, date2)
elif year1 < year2:
    CalculateDaysSmaller(year1, year2)
else:
    CalculateDaysGreater(year1, year2)