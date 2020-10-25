# Aplicación para controlar el horario semanal
# Fecha: Octubre 24 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

# variable para iniciar el ciclo while
operacion = 6
calendario = {'L': {}, 'M': {}, 'W': {}, 'J': {}, 'V': {}}

print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
print("| - - - - - - - - - - - PROGRAMA PARA REGISTRAR EL HORARIO SEMANAL - - - - - - - - - - |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")

while (operacion > 0 and operacion != 5):
    operacion = int(input("""
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   1   + - - - - - AGREGAR CLASE - - - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   2   + - - - - MODIFICAR CLASE - - - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   3   + - - - - - ELIMINAR CLASE - - - - - -+
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   4   + - - - - - VER HORARIO - - - - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   5   + - - - - - - - SALIR - - - - - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                """))
    print()
    if (operacion == 1):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - AGREGANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("Por favor ingrese el día para el cual desea agregar la clase")
        dia = input("""Nota: para mayor facilidad los días se identifican asi:
        
        L: Lunes
        M: Martes
        W: Miércoles
        J: Jueves
        V: Viernes
        """)

        if (dia == 'L'):
            ingreso_nueva_clase = 'S'
            horario_lunes = {}
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                print("La hora ingresada es "+hora)
                clase = input("Por favor ingrese el nombre de la clase: ")
                print("La clase es "+clase)
                horario_lunes[hora] = clase
                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Lunes? (S/N): ")
            calendario['L'] = horario_lunes

        elif (dia == 'M'):
            ingreso_nueva_clase = 'S'
            horario_martes = {}
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                print("La hora ingresada es " + hora)
                clase = input("Por favor ingrese el nombre de la clase: ")
                print("La clase es " + clase)
                horario_martes[hora] = clase
                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Martes? (S/N): ")
            calendario['M'] = horario_martes

        elif (dia == 'W'):
            ingreso_nueva_clase = 'S'
            horario_miercoles = {}
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                print("La hora ingresada es " + hora)
                clase = input("Por favor ingrese el nombre de la clase: ")
                print("La clase es " + clase)
                horario_miercoles[hora] = clase
                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Miércoles? (S/N): ")
            calendario['W'] = horario_miercoles

        elif (dia == 'J'):
            ingreso_nueva_clase = 'S'
            horario_jueves = {}
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                print("La hora ingresada es " + hora)
                clase = input("Por favor ingrese el nombre de la clase: ")
                print("La clase es " + clase)
                horario_jueves[hora] = clase
                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Jueves? (S/N): ")
            calendario['J'] = horario_jueves

        elif (dia == 'V'):
            ingreso_nueva_clase = 'S'
            horario_viernes = {}
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                print("La hora ingresada es " + hora)
                clase = input("Por favor ingrese el nombre de la clase: ")
                print("La clase es " + clase)
                horario_viernes[hora] = clase
                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Viernes? (S/N): ")
            calendario['V'] = horario_viernes
        else:
            print("El día seleccionado no existe")

    elif (operacion == 2):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  +")
        print("| - - - - - - - - - - - MODIFICANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  +")

    elif (operacion == 3):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
        print("| - - - - - - - - - - - ELIMINANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")

    elif (operacion == 4):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - - VIENDO HORARIO - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print()
        print(calendario)

    elif (operacion == 5):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - - - - SALIENDO - - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")

    else:
        print("Opcion inválida")
