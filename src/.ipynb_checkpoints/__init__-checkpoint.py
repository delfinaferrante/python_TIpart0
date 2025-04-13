from datetime import datetime

def calcular_edad(fecha_nac_str):
    """Funcion que calcula la edad usando datetime, basandose solo en el año de nacimiento"""

    # Convierto el string 'xx/xx/xxxx' en un objeto datetime
    fecha_nac = datetime.strptime(fecha_nac_str, '%d/%m/%Y')

    # Defino la fecha de referencia (fin del 3er trimestre 2024)
    fecha_ref = datetime(2024, 9, 30) 

    # Resto los años para calcular la edad
    edad = fecha_ref.year - fecha_nac.year

    return edad
