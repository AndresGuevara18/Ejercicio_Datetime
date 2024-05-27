from datetime import datetime

print("4) EDAD EN DIAS: Escribe un programa que calcule la edad de una persona en dias, dado la fecha de nacimiento y ",
      "la fecha actual") 

#date1 = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ") 
date1 = "1991-10-18"

# Convertir las cadenas de entrada en objetos datetime
date1 = datetime.strptime(date1, "%Y-%m-%d")
ahora = datetime.now()

#covertir en int el año de la fecha ingresada
year1 = int(date1.strftime("%Y"))
year2 = int(ahora.strftime("%Y"))

days = 365
cont_day_more = 0

year_one = year1
year_two = year2

while year_one <= year_two:
    if year_one % 4 == 0 and year_one % 100 !=0: #divisible entre 4 y no entre 100 o 400      
        cont_day_more += 1
    else:
        cont_day_more += 0       
    year_one += 1

def CalculateDaysBirth(year1, year2):
    dif_years = year2 - year1
    days_years = dif_years * days

    print(f"\nFecha nacimiento: {date1.strftime('%Y-%m-%d')}  ---  fecha actual: {ahora.strftime('%Y-%m-%d')}")

    #dias trasncurridos en los dos años
    days_date1 = int(date1.strftime("%j"))
    days_now = int(ahora.strftime("%j"))
    date1_birt = (days_years - days_date1) + days_now + cont_day_more
    print(f"La diferencia en días entre {date1.strftime('%Y-%m-%d')} y {ahora.strftime('%Y-%m-%d')} es de => {date1_birt} días.")

CalculateDaysBirth(year1, year2)


"""
#date1 = input("Ingresa tu fecha de cumpleaños (YYYY-MM-DD): ") 
date1 = "1991-10-18"

# Convertir la cadena de entrada en un objeto datetime
date_birth = datetime.strptime(date1, "%Y-%m-%d")
date_act = datetime.now()

# Calcular la diferencia en días
diferen = date_act - date_birth
days_birth = diferen.days

print(f"Feha nacimiento: {date_birth.strftime('%Y-%m-%d')}\nFecha actual: {date_act.strftime('%Y-%m-%d')}\nEdad en dias: {days_birth}")
"""