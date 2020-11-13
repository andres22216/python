# Aplicación para controlar el horario semanal
# Fecha: Octubre 24 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

# variable para iniciar el ciclo while de la operación
operacion = 6
# diccionario para almacenar el calendario
calendario = {'L': {}, 'M': {}, 'W': {}, 'J': {}, 'V': {}}
# diccionarios para almacenar los horarios de cada dia de la semana
horario_lunes = {}
horario_martes = {}
horario_miercoles = {}
horario_jueves = {}
horario_viernes = {}

print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
print("| - - - - - - - - - - - PROGRAMA PARA REGISTRAR EL HORARIO SEMANAL - - - - - - - - - - |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
# ciclo para controlar el menu principal de la aplicación
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
    # Operación de agregar clases
    if (operacion == 1):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - AGREGANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("Por favor ingrese el día para el cual desea agregar la clase")
        # Definimos el menú para seleccionar los días
        dia = input("""Nota: para mayor facilidad los días se identifican asi:
        
        L: Lunes
        M: Martes
        W: Miércoles
        J: Jueves
        V: Viernes
        """)

        if (dia == 'L'):
            ingreso_nueva_clase = 'S'
            # ciclo para controlar si se desea seguir ingresando clases
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                # validamos si la hora ya esta seleccionada
                if hora in horario_lunes:
                    print("La hora ya esta ocupada. Por favor seleccione una diferente")
                else:
                    clase = input("Por favor ingrese el nombre de la clase: ")
                    horario_lunes[hora] = clase

                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Lunes? (S/N): ")
            calendario['L'] = horario_lunes

        elif (dia == 'M'):
            ingreso_nueva_clase = 'S'
            # ciclo para controlar si se desea seguir ingresando clases
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                # validamos si la hora ya esta seleccionada
                if hora in horario_martes:
                    print("La hora ya esta ocupada. Por favor seleccione una diferente")
                else:
                    clase = input("Por favor ingrese el nombre de la clase: ")
                    horario_martes[hora] = clase

                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Martes? (S/N): ")
            calendario['M'] = horario_martes

        elif (dia == 'W'):
            ingreso_nueva_clase = 'S'
            # ciclo para controlar si se desea seguir ingresando clases
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                # validamos si la hora ya esta seleccionada
                if hora in horario_miercoles:
                    print("La hora ya esta ocupada. Por favor seleccione una diferente")
                else:
                    clase = input("Por favor ingrese el nombre de la clase: ")
                    horario_miercoles[hora] = clase

                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Miércoles? (S/N): ")
            calendario['W'] = horario_miercoles

        elif (dia == 'J'):
            ingreso_nueva_clase = 'S'
            # ciclo para controlar si se desea seguir ingresando clases
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                # validamos si la hora ya esta seleccionada
                if hora in horario_jueves:
                    print("La hora ya esta ocupada. Por favor seleccione una diferente")
                else:
                    clase = input("Por favor ingrese el nombre de la clase: ")
                    horario_jueves[hora] = clase

                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Jueves? (S/N): ")
            calendario['J'] = horario_jueves

        elif (dia == 'V'):
            ingreso_nueva_clase = 'S'
            # ciclo para controlar si se desea seguir ingresando clases
            while (ingreso_nueva_clase == 'S'):
                hora = input("Por favor ingrese la hora: ")
                # validamos si la hora ya esta seleccionada
                if hora in horario_viernes:
                    print("La hora ya esta ocupada. Por favor seleccione una diferente")
                else:
                    clase = input("Por favor ingrese el nombre de la clase: ")
                    horario_viernes[hora] = clase

                ingreso_nueva_clase = input("\n¿Desea continuar ingresando clases para el día Viernes? (S/N): ")
            calendario['V'] = horario_viernes
        else:
            print("El día seleccionado no existe")

    # Operación para modificar las clases
    elif (operacion == 2):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  +")
        print("| - - - - - - - - - - - MODIFICANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  +")
        print("Por favor ingrese el día para el cual desea modificar la clase")
        # Definimos el menú para seleccionar los días
        dia = input("""Nota: para mayor facilidad los días se identifican asi:

                L: Lunes
                M: Martes
                W: Miércoles
                J: Jueves
                V: Viernes
                """)

        if (dia == 'L'):
            modificando_clase = 'S'
            # ciclo para controlar si se desea seguir modificando clases
            while (modificando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a modificar: ")
                # validamos si la hora a modificar si existe en el calendario del dia
                if hora in horario_lunes:
                    clase_modificada = input("Por favor ingrese el nuevo nombre de la clase: ")
                    horario_lunes[hora] = clase_modificada
                else:
                    print("No existe la hora seleccionada")

                modificando_clase = input("\n¿Desea continuar modificando clases para el día Lunes? (S/N): ")

        elif (dia == 'M'):
            modificando_clase = 'S'
            # ciclo para controlar si se desea seguir modificando clases
            while (modificando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a modificar: ")
                # validamos si la hora a modificar si existe en el calendario del dia
                if hora in horario_martes:
                    clase_modificada = input("Por favor ingrese el nuevo nombre de la clase: ")
                    horario_martes[hora] = clase_modificada
                else:
                    print("No existe la hora seleccionada")

                modificando_clase = input("\n¿Desea continuar modificando clases para el día Lunes? (S/N): ")

        elif (dia == 'W'):
            modificando_clase = 'S'
            # ciclo para controlar si se desea seguir modificando clases
            while (modificando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a modificar: ")
                # validamos si la hora a modificar si existe en el calendario del dia
                if hora in horario_miercoles:
                    clase_modificada = input("Por favor ingrese el nuevo nombre de la clase: ")
                    horario_miercoles[hora] = clase_modificada
                else:
                    print("No existe la hora seleccionada")

                modificando_clase = input("\n¿Desea continuar modificando clases para el día Lunes? (S/N): ")

        elif (dia == 'J'):
            modificando_clase = 'S'
            # ciclo para controlar si se desea seguir modificando clases
            while (modificando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a modificar: ")
                # validamos si la hora a modificar si existe en el calendario del dia
                if hora in horario_jueves:
                    clase_modificada = input("Por favor ingrese el nuevo nombre de la clase: ")
                    horario_jueves[hora] = clase_modificada
                else:
                    print("No existe la hora seleccionada")

                modificando_clase = input("\n¿Desea continuar modificando clases para el día Lunes? (S/N): ")

        elif (dia == 'V'):
            modificando_clase = 'S'
            # ciclo para controlar si se desea seguir modificando clases
            while (modificando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a modificar: ")
                # validamos si la hora a modificar si existe en el calendario del dia
                if hora in horario_viernes:
                    clase_modificada = input("Por favor ingrese el nuevo nombre de la clase: ")
                    horario_viernes[hora] = clase_modificada
                else:
                    print("No existe la hora seleccionada")

                modificando_clase = input("\n¿Desea continuar modificando clases para el día Lunes? (S/N): ")
        else:
            print("El día para cual desea modificar el horario no existe")

    # Operación para eliminar clases
    elif (operacion == 3):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
        print("| - - - - - - - - - - - ELIMINANDO CLASES - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
        print("Por favor ingrese el día para el cual desea eliminar la clase")
        # Definimos el menú para seleccionar los días
        dia = input("""Nota: para mayor facilidad los días se identifican asi:

                        L: Lunes
                        M: Martes
                        W: Miércoles
                        J: Jueves
                        V: Viernes
                        """)

        if (dia == 'L'):
            eliminando_clase = 'S'
            # ciclo para controlar si se desea seguir eliminando clases
            while (eliminando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a eliminar: ")
                # validamos si la hora existe y pedimos confirmación para eliminar
                if hora in horario_lunes:
                    confirma_eliminacion = input("¿Seguro que desea eliminar la clase de las "+hora+" ? (Si/No): ")
                    if (confirma_eliminacion == 'Si'):
                        del horario_lunes[hora]
                        print("Eliminación exitosa")
                    else:
                        print("El usuario ha cancelado la eliminación")
                else:
                    print("No existe la hora seleccionada")

                eliminando_clase = input("\n¿Desea continuar eliminando clases para el día Lunes? (S/N): ")

        elif (dia == 'M'):
            eliminando_clase = 'S'
            # ciclo para controlar si se desea seguir eliminando clases
            while (eliminando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a eliminar: ")
                # validamos si la hora existe y pedimos confirmación para eliminar
                if hora in horario_martes:
                    confirma_eliminacion = input("¿Seguro que desea eliminar la clase de las " + hora + " ? (Si/No): ")
                    if (confirma_eliminacion == 'Si'):
                        del horario_martes[hora]
                        print("Eliminación exitosa")
                    else:
                        print("El usuario ha cancelado la eliminación")
                else:
                    print("No existe la hora seleccionada")

                eliminando_clase = input("\n¿Desea continuar eliminando clases para el día Martes? (S/N): ")

        elif (dia == 'W'):
            eliminando_clase = 'S'
            # ciclo para controlar si se desea seguir eliminando clases
            while (eliminando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a eliminar: ")
                # validamos si la hora existe y pedimos confirmación para eliminar
                if hora in horario_miercoles:
                    confirma_eliminacion = input("¿Seguro que desea eliminar la clase de las " + hora + " ? (Si/No): ")
                    if (confirma_eliminacion == 'Si'):
                        del horario_miercoles[hora]
                        print("Eliminación exitosa")
                    else:
                        print("El usuario ha cancelado la eliminación")
                else:
                    print("No existe la hora seleccionada")

                eliminando_clase = input("\n¿Desea continuar eliminando clases para el día Miércoles? (S/N): ")

        elif (dia == 'J'):
            eliminando_clase = 'S'
            # ciclo para controlar si se desea seguir eliminando clases
            while (eliminando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a eliminar: ")
                # validamos si la hora existe y pedimos confirmación para eliminar
                if hora in horario_jueves:
                    confirma_eliminacion = input("¿Seguro que desea eliminar la clase de las " + hora + " ? (Si/No): ")
                    if (confirma_eliminacion == 'Si'):
                        del horario_jueves[hora]
                        print("Eliminación exitosa")
                    else:
                        print("El usuario ha cancelado la eliminación")
                else:
                    print("No existe la hora seleccionada")

                eliminando_clase = input("\n¿Desea continuar eliminando clases para el día Jueves? (S/N): ")

        elif (dia == 'V'):
            eliminando_clase = 'S'
            # ciclo para controlar si se desea seguir eliminando clases
            while (eliminando_clase == 'S'):
                hora = input("Por favor ingrese la hora de la clase a eliminar: ")
                # validamos si la hora existe y pedimos confirmación para eliminar
                if hora in horario_viernes:
                    confirma_eliminacion = input("¿Seguro que desea eliminar la clase de las " + hora + " ? (Si/No): ")
                    if (confirma_eliminacion == 'Si'):
                        del horario_viernes[hora]
                        print("Eliminación exitosa")
                    else:
                        print("El usuario ha cancelado la eliminación")
                else:
                    print("No existe la hora seleccionada")

                eliminando_clase = input("\n¿Desea continuar eliminando clases para el día Viernes? (S/N): ")
        else:
            print("El día para cual desea eliminar el horario no existe")

    # Operación
    elif (operacion == 4):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - - VIENDO HORARIO - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print()
        for i in calendario:
            print("Horario del día: "+i)
            print()
            print("Hora           Clase")
            print()
            horario = calendario[i]
            for k in horario:
                print(k +"              "+horario[k])
            print()

    # Operación para terminar la ejecución del programa
    elif (operacion == 5):
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
        print("| - - - - - - - - - - - - - - SALIENDO - - - - - - - - - - - |")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")

    else:
        print("Opcion inválida")
