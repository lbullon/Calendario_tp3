from sys import argv
import calendar
from utils import consigue_primer_dia_year, crea_calendario, crea_calendario_festivos


fichero_meses = open(argv[1], "r")
fichero_meses_b = open(argv[1], "r")
fichero_meses_festivos = open(argv[1], "r")


fichero_dias = open(argv[2], "r")
fichero_dias_b = open(argv[3], "r")
fichero_dias_festivos = open (argv[4], "r")




year = int(input("Mete el year"))

def bisiesto (year):
    if calendar.isleap(year) == False:
        primer_dia_year = consigue_primer_dia_year(year)
        calendar1 = crea_calendario(fichero_meses, fichero_dias, primer_dia_year)



    else:
        primer_dia_year = consigue_primer_dia_year(year)
        calendar1 = crea_calendario(fichero_meses, fichero_dias_b, primer_dia_year)

    return calendar1

calendario_pedido = bisiesto(year)
calendario_festivos= crea_calendario_festivos(fichero_meses_festivos, fichero_dias_festivos)

def crea_calendario_festivos_pedido(calendario_festivos):
    n = 0
    while n < len(calendario_festivos.keys()):

        meses = list(calendario_festivos)
        x = meses[n]

        t = 0
        while len(calendario_festivos[x]) > t:
            if calendario_pedido[x][calendario_festivos[x][t]] == 6:
                calendario_festivos[x][t] = int(calendario_festivos[x][t]) + 1

            else:
                calendario_festivos[x][t] = calendario_festivos[x][t]
            t += 1
        n += 1

    return calendario_festivos


respuesta = crea_calendario_festivos_pedido(calendario_festivos)


print(respuesta)