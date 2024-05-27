from datetime import datetime, timedelta

print("2) SUMA DE DÍAS: Crea un programa que tome una fecha y un número de días como entrada, luego imprime la fecha ",
      "resultante después de agregar ese número de días\n")

# Leer la fecha de inicio y el número de días (puedes descomentar las líneas siguientes si deseas ingresar los valores manualmente)
# fecha1 = input("Ingrese la fecha (YYYY-MM-DD):")
# num_days = int(input("Ingrese los días: "))

# Usar valores predefinidos para propósitos de demostración
fecha1 = "2024-05-02"
num_days = -30

# Convertir la cadena de fecha en un objeto datetime
fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
year1 = fecha1.year

print(f"Fecha: {fecha1.strftime('%Y-%m-%d')} --- Año: {year1}")

# Función para sumar días a una fecha e imprimir la nueva fecha
def add_days(fecha, dias):
    nueva_fecha = fecha + timedelta(days=dias)
    
    print(f"Dias: {dias}\nFecha resultante: {datetime.strftime(nueva_fecha, '%Y-%m-%d')}")
    return nueva_fecha

# Calcular e imprimir la nueva fecha
add_days(fecha1, num_days)
