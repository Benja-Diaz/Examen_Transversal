import csv 
import random

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”MiguelSánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_trabajadores = []

def asignar_sueldos(trabajadores):
    sueldo_random = round(random.uniform(300000, 2500000)
    print(f"el empleado {trabajadores} tiene un sueldo de {sueldo}")


def clasificar_sueldos(trabajadores):
    if sueldo < 800000:
        print(f"sueldos menores a $800.000 TOTAL: {len()}")
    elif sueldo > 800000 and sueldo < 2000000:
        print(f"sueldos entre $800.000 y $2.000.000 TOTAL{len()}")
    elif sueldo > 2000000:
        print(f"sueldos superiores a $2.000.000 TOTAL {len()}")


def estadisticas(trabajadores):
    menor = min(sueldos_trabajadores)
    mayor = max(sueldos_trabajadores)
    promedio = sum(sueldos_trabajadores['sueldo'] for sueldo in sueldos_trabajadores) / len(trabajadores)

    print("el sueldo mas bajo es de: {menor}")
    print("el sueldo mas alto es de: {mayor}")
    print("el promedio de los sueldos es de: {promedio}")

def reporte_de_sueldo(trabajadores):
    descuento_salud = sueldo-sueldo*(7/100)
    descuento_afp = sueldo-sueldo*(12/100)
    sueldo_liquido = sueldo - descuento_afp - descuento_salud

    

def guardar_csv(sueldos_trabajadores, filename='sueldos.csv'):
    if sueldos_trabajadores:
        keys = sueldos_trabajadores[0].keys()
        with open(filename, 'w', newline='')as output_file:
            dict_writer=csv.DictWriter(output_file, filename=keys)
            dict_writer.writeheader()
            dict_writer.writerows(sueldos_trabajadores)
        print("finalizando programa...")
        print("Desarrollado por Benjamin Diaz")
        print("RUT 21.672.417-8")
    