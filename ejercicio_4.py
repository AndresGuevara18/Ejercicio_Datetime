from datetime import datetime

print("4) EDAD EN DIAS: Escribe un programa que calcule la edad de una persona en dias, dado la fecha de nacimiento y ",
      "la fecha actual") 

#date1 = input("Ingresa tu fecha de cumpleaños (YYYY-MM-DD): ") 
"""date1 = "1991-10-18"

# Convertir las cadenas de entrada en objetos datetime
date1 = datetime.strptime(date1, "%Y-%m-%d")
ahora = datetime.now()

#covertir en int el año de la fecha ingresada
year1 = int(date1.strftime("%Y"))
year2 = int(ahora.strftime("%Y"))

days = 365

def CalculateDaysBirth(year1, year2):
    dif_years = year2 - year1
    days_years = dif_years * days

    print(f"Año 1 : {year1} --- Año 2: {year2}\nAños cumplidos: {dif_years} --- Dias de años: {days_years}\nFecha nacimiento: {date1}  ---  fecha actual: {ahora}")

    #dias trasncurridos en los dos años
    days_date1 = int(date1.strftime("%j"))
    days_now = int(ahora.strftime("%j"))

    print(f"\nDias nacimiento: {days_date1} ---- Dias ahora: {days_now}")

    date1_birt = (days_years - days_date1) + days_now

    print(f"Dias en años cumplidos: {date1_birt}")


CalculateDaysBirth(year1, year2)"""



#date1 = input("Ingresa tu fecha de cumpleaños (YYYY-MM-DD): ") 
date1 = "1991-10-18"

# Convertir la cadena de entrada en un objeto datetime
date_birth = datetime.strptime(date1, "%Y-%m-%d")
date_act = datetime.now()

# Calcular la diferencia en días
diferen = date_act - date_birth
days_birth = diferen.days

print(f"Feha nacimiento: {date_birth.strftime('%Y-%m-%d')}\nFecha actual: {date_act.strftime('%Y-%m-%d')}\nEdad en dias: {days_birth}")