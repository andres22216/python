# Aplicación para registro de contactos
# Fecha: Noviembre 10 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

#Diccionario para almacenar el listado de contactos
agenda_dict = {}

print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
print("| - - - - - - - - - - - - PROGRAMA PARA EL REGISTRO DE CONTACTOS - - - - - - - - - - - |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")

#funcion para ver el menu
def verMenu():
    operacion = int(input("""
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    |   1   + - - - - - AGREGAR CONTACTO - - - - - -  +
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    |   2   + - - - - - BUSCAR CONTACTO - - - - - - - +
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    |   3   + - - - - - MODIFICAR CONTACTO - - - - -  +
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    |   4   + - - - - - ELIMINAR CONTACTO - - - - - - +
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    |   5   + - - - - - - - SALIR - - - - - - - - - - +
                    + - - - + - - - - - - - - - - - - - - - - - - - - +
                    """))

    if (operacion == 1):
        agregar()
    elif (operacion == 2):
        buscar()
    elif (operacion == 3):
        modificar()
    elif (operacion == 4):
        eliminar()
    elif (operacion == 5):
        salir()
    else:
        print("Opcion inválida")
        verMenu()

#Definimos la funcion para agregar contacto a la agenda
def agregar():
    print()
    identificacion = str(input("Por favor ingrese el número de identificación: "))
    if (identificacion in agenda_dict):
        print()
        print("La identificación: " + identificacion + " ya fue registrada en la agenda")
    else:
        nombre = str(input("Por favor ingrese el nombre: "))
        correo = str(input("Por favor ingrese el correo electrónico: "))
        telefono = str(input("Por favor ingrese el número de teléfono: "))
        edad = int(input("Por favor ingrese la edad (en años): "))
        contacto_dict = {'nombre': nombre, 'correo': correo, 'telefono': telefono, 'edad': edad}
        agenda_dict[identificacion] = contacto_dict
        print()
        print("Contacto agregado exitosamente")
    print()

    verMenu()

#Definimos la funcion para buscar contacto en la agenda
def buscar():
    print()
    identificacion = str(input("Por favor ingrese el número de identificación que desea buscar: "))
    print()
    if (identificacion in agenda_dict):
        print("Los datos del contacto son: ")
        print()
        #print(agenda_dict[identificacion])
        print("Nombre: "+str(agenda_dict[identificacion]["nombre"]))
        print("Correo: "+str(agenda_dict[identificacion]["correo"]))
        print("Teléfono: "+str(agenda_dict[identificacion]["telefono"]))
        print("Edad: "+str(agenda_dict[identificacion]["edad"]))
    else:
        print("La identificación ingresada no existe en la agenda")

    verMenu()

#Definimos la funcion para modificar los datos de un contaco
def modificar():
    print()
    identificacion = str(input("Por favor ingrese el número de identificación que desea modificar: "))
    print()
    if (identificacion in agenda_dict):
        nombre = str(input("Por favor ingrese el nuevo nombre: "))
        correo = str(input("Por favor ingrese el nuevo correo electrónico: "))
        telefono = str(input("Por favor ingrese el nuevo número de teléfono: "))
        edad = int(input("Por favor ingrese la nueva edad (en años): "))
        contacto_dict = {'nombre': nombre, 'correo': correo, 'telefono': telefono, 'edad': edad}
        agenda_dict[identificacion] = contacto_dict
        print()
        print("Contacto modificado exitosamente")
    else:
        print("La identificación ingresada no existe en la agenda")

    verMenu()

#Definimos la funcion para eliminar un contacto de la agenda
def eliminar():
    print()
    identificacion = str(input("Por favor ingrese el número de identificación que desea eliminar: "))
    print()
    if (identificacion in agenda_dict):
        eliminar_contacto = input("Esta seguro que desea eliminar el contacto (SI-NO): ")
        if (eliminar_contacto == 'SI'):
            del agenda_dict[identificacion]
            print()
            print("Contacto eliminado exitosamente")
        elif (eliminar_contacto == 'NO'):
            print()
            print("Eliminación cancelada por el usuario")
        else:
            print()
            print("Opción inválida")
    else:
        print("La identificación ingresada no existe en la agenda")

    verMenu()

#Definimos la funcion para salir del programa
def salir():
    print()
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
    print("| - - - - - - - - - - - - - - - SALIENDO - - - - - - - - - - - - - - - |")
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")

#Llamado inicial a la funcion para cargar el menu
verMenu()