from utilidades import *

sueldos_trabajadores = []

while True:
    print("\nMenu:")
    print("1) asignar sueldos aleatorios")
    print("2) clasificar sueldos")
    print("3) ver estadisticas")
    print("4) reporte de sueldos")
    print("5) salir del programa")

    opcion = input("ingrese la opcion: ")

    if opcion == '1':
        asignar_sueldos(sueldos_trabajadores)
    elif opcion == '2':
        clasificar_sueldos(sueldos_trabajadores)
    elif opcion == '3':
        estadisticas(sueldos_trabajadores)
    elif opcion == '4':
        reporte_de_sueldo(sueldos_trabajadores)
    elif opcion == '5':
        guardar_csv(sueldos_trabajadores)
        break 
    else:
        print("la opcion es invalida, ingrese nuevamente")   