from datetime import datetime

print("1) DIFERENCIA DE DIAS: escriba un programa que tome dos fechas como entrada y calcule la diferencia en dias entre ellas")

"""date1 = input("Ingrese la primera fecha (YYYY-MM-DD): ")
date2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")"""

#yearSmaller
#date1 = "1991-10-18"
#date2 = "2024-05-17"

#YearGreater
#date1 = "2024-05-17"
#date2 = "1991-10-18"

#MounthSmaller
#date1 = "2022-05-17"
#date2 = "2022-06-30"

#MounthGreater
#date1 = "2022-06-30"
#date2 = "2022-05-17"

#DaySmaller
#date1 = "2022-05-17"
#date2 = "2022-05-30"

#DayGreater
#date1 = "2022-06-30"
#date2 = "2022-06-17"

date1 = "2016-06-30"
date2 = "2016-06-30"

date1 = datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

print(f"Fecha 1: {date1.strftime('%Y-%m-%d')} --- Fecha 2: {date2.strftime('%Y-%m-%d')}")

year1 = int(date1.strftime("%Y"))
mounth1 = int(date1.strftime("%m"))
day1 = int(date1.strftime("%d"))

year2 = int(date2.strftime("%Y"))
mounth2 = int(date2.strftime("%m"))
day2 = int(date2.strftime("%d"))

days = 365
contador_days_more = 0

year_one = year1
year_two = year2

while year_one <= year2:  
    if year_one % 4 == 0 and year_one % 100 !=0: #divisible entre 4 y no entre 100 o 400      
        contador_days_more += 1
    else:
        contador_days_more += 0       
    year_one += 1

while year_two <= year1:
    if year_two % 4 == 0 and year_two % 100 !=0: #divisible entre 4 y no entre 100 o 400       
        contador_days_more += 1
    else:
        contador_days_more += 0       
    year_two += 1

#Si la primer fecha es MENOR que la segunda
def CalculateYearSmaller(year1, year2):
    dif_year = (year2 - year1) 
    days_years_tot = dif_year * days 

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days = (days_years_tot - date1_days  ) + date2_days + (contador_days_more * 2)
    print(f"La diferencia en días entre {date1.strftime('%Y-%m-%d')} y {date2.strftime('%Y-%m-%d')} es de => {total_days} días.")

#si la primer fecha MAYOR que la segunda
def CalculateYearGreater(year1, year2):
    dif_year = (year1 - year2)
    days_years_tot = dif_year * days 

    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days = (days_years_tot - date2_days  ) + date1_days + (contador_days_more * 2)
    print(f"La diferencia en días entre {date2.strftime('%Y-%m-%d')} y {date1.strftime('%Y-%m-%d')} es de => {total_days} días.")

#si el primer mes es MENOR que el segundo // o dia
def CalculateMounthSmaller():
    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days =  date2_days  - date1_days
    print(f"La diferencia en días entre {date1.strftime('%Y-%m-%d')} y {date2.strftime('%Y-%m-%d')} es de => {total_days} días.")

#Si el primer mes es MAYOR que el segundo // o dia
def CalculateMounthGreater():
    date1_days = int(date1.strftime("%j"))
    date2_days = int(date2.strftime("%j"))
    total_days =  date1_days  - date2_days
    print(f"La diferencia en días entre {date2.strftime('%Y-%m-%d')} y {date1.strftime('%Y-%m-%d')} es de => {total_days} días.")


#CONDICIONAL
if year1 == year2:
    if mounth1 == mounth2:
        if day1 < day2:
           CalculateMounthSmaller()
        else:
            CalculateMounthGreater()
    elif mounth1 < mounth2:
        CalculateMounthSmaller()
    else:
        CalculateMounthGreater()
elif year1 < year2:
    CalculateYearSmaller(year1, year2)
else:
    CalculateYearGreater(year1, year2)