# Aplicación para registro de productos de la tienda escolar
# Fecha: Septiembre 29 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

# variable para iniciar el ciclo while
operacion = 5

print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
print("| - - - PROGRAMA DE REGISTRO PARA LA DE GESTIÓN DE CULTIVOS DE LA GRANJA ESCOLAR - - - |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+")
print("***************** Registro de información para cada uno de los cultivos ***************")
# Capturamos los datos para el cultivo uno
print()
nombre_cultivo_uno = input("Ingrese el nombre del cultivo 1: ")
dias_horario_mantenimiento_cultivo_uno = input("Ingrese los días y horarios de mantenimiento: ")
dias_horario_regado_cultivo_uno = input("Ingrese los días y horarios de regado: ")
dias_abono_cultivo_uno = input("Ingrese los días y horarios de abono: ")
print()
print("Ahora ingrese las ETAPAS para el cultivo 1 ")
print()
dias_fase_vegetativa_cultivo_uno = input("Ingrese los días para la fase vegetativa: ")
detalle_fase_vegetativa_cultivo_uno = input("Ingrese algún comentario o detalle para la fase: ")
dias_fase_reproductiva_cultivo_uno = input("Ingrese los dias para la fase reproductiva: ")
detalle_fase_reproductiva_cultivo_uno = input("Ingrese algún comentario o detalle para la fase reproductiva: ")
print()
# Capturamos los datos para el cultivo dos
print()
nombre_cultivo_dos = input("Ingrese el nombre del cultivo 2: ")
dias_horario_mantenimiento_cultivo_dos = input("Ingrese los días y horarios de mantenimiento: ")
dias_horario_regado_cultivo_dos = input("Ingrese los días y horarios de regado: ")
dias_abono_cultivo_dos = input("Ingrese los días y horarios de abono: ")
print()
print("Ahora ingrese las ETAPAS para el cultivo 2 ")
print()
dias_fase_vegetativa_cultivo_dos = input("Ingrese los días para la fase vegetativa: ")
detalle_fase_vegetativa_cultivo_dos = input("Ingrese algún comentario o detalle para la fase: ")
dias_fase_reproductiva_cultivo_dos = input("Ingrese los días para la fase reproductiva: ")
detalle_fase_reproductiva_cultivo_dos = input("Ingrese algún comentario o detalle para la fase reproductiva: ")
print()
# Capturamos los datos para el cultivo tres
print()
nombre_cultivo_tres = input("Ingrese el nombre del cultivo 3: ")
dias_horario_mantenimiento_cultivo_tres = input("Ingrese los días y horarios de mantenimiento: ")
dias_horario_regado_cultivo_tres = input("Ingrese los días y horarios de regado: ")
dias_abono_cultivo_tres = input("Ingrese los días y horarios de abono: ")
print()
print("Ahora ingrese las ETAPAS para el cultivo 3 ")
print()
dias_fase_vegetativa_cultivo_tres = input("Ingrese los días para la fase vegetativa: ")
detalle_fase_vegetativa_cultivo_tres = input("Ingrese algún comentario o detalle para la fase: ")
dias_fase_reproductiva_cultivo_tres = input("Ingrese los días para la fase reproductiva: ")
detalle_fase_reproductiva_cultivo_tres = input("Ingrese algún comentario o detalle para la fase reproductiva: ")
print()
print("Seleccione una opción del menú ")
print()
# Inicializamos el ciclo que mostrará el menú principal
while (operacion > 0 and operacion != 3):
    operacion = int(input("""
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   1   + - - - - GESTIÓN DEL CULTIVO - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   2   + - - - VER ETAPAS DEL CULTIVO - - -  +
                + - - - + - - - - - - - - - - - - - - - - - - +
                |   3   + - - - - - - - SALIR - - - - - - - - +
                + - - - + - - - - - - - - - - - - - - - - - - +
                """))
# Realizamos la comparación de la opción seleccionada
    if (operacion == 1):
        print()
        print("**************************** Gestión del cultivo *************************")
        print()
        print("Por favor seleccione el cultivo")
        # Submenú para la selección de cultivo
        operacion_cultivo = int(input("""
                        + - - - + - - - - - - - - - - - - - - +
                        |   1   + - - - - CULTIVO UNO - - - - +
                        + - - - + - - - - - - - - - - - - - - +
                        |   2   + - - - - CULTIVO DOS - - - - +
                        + - - - + - - - - - - - - - - - - - - +
                        |   3   + - - - - CULTIVO TRES - - - -+
                        + - - - + - - - - - - - - - - - - - - +
                        """))
        if(operacion_cultivo == 1):
            print("Para el cultivo: "+nombre_cultivo_uno)
            print("Los horarios de mantenimiento son: "+dias_horario_mantenimiento_cultivo_uno)
            print("Los horarios de regado son: " + dias_horario_regado_cultivo_uno)
            print("Los horarios de abono son: " + dias_abono_cultivo_uno)
        elif(operacion_cultivo == 2):
            print("Para el cultivo: " + nombre_cultivo_dos)
            print("Los horarios de mantenimiento son: " + dias_horario_mantenimiento_cultivo_dos)
            print("Los horarios de regado son: " + dias_horario_regado_cultivo_dos)
            print("Los horarios de abono son: " + dias_abono_cultivo_dos)
        elif (operacion_cultivo == 3):
            print("Para el cultivo: " + nombre_cultivo_tres)
            print("Los horarios de mantenimiento son: " + dias_horario_mantenimiento_cultivo_tres)
            print("Los horarios de regado son: " + dias_horario_regado_cultivo_tres)
            print("Los horarios de abono son: " + dias_abono_cultivo_tres)
        else :
            print("El cultivo con identificación "+str(operacion_cultivo)+ " no existe")
    elif (operacion == 2):
        print()
        print("**************************** Etapas de los cultivos *************************")
        print()
        print("Por favor seleccione el cultivo")
        # Submenú para la selección de cultivo
        operacion_cultivo = int(input("""
                                + - - - + - - - - - - - - - - - - - - +
                                |   1   + - - - - CULTIVO UNO - - - - +
                                + - - - + - - - - - - - - - - - - - - +
                                |   2   + - - - - CULTIVO DOS - - - - +
                                + - - - + - - - - - - - - - - - - - - +
                                |   3   + - - - - CULTIVO TRES - - - -+
                                + - - - + - - - - - - - - - - - - - - +
                                """))
        if (operacion_cultivo == 1):
            print("Para el cultivo: " + nombre_cultivo_uno)
            print("Los horarios de la fase vegetativa son: " + dias_fase_vegetativa_cultivo_uno)
            print("El detalle de la fase vegetativa es: " + detalle_fase_vegetativa_cultivo_uno)
            print("Los horarios de la fase reproductiva son: " + dias_fase_reproductiva_cultivo_uno)
            print("El detalle de la fase reproductiva es: " + detalle_fase_reproductiva_cultivo_uno)
        elif (operacion_cultivo == 2):
            print("Para el cultivo: " + nombre_cultivo_dos)
            print("Los horarios de la fase vegetativa son: " + dias_fase_vegetativa_cultivo_dos)
            print("El detalle de la fase vegetativa es: " + detalle_fase_vegetativa_cultivo_dos)
            print("Los horarios de la fase reproductiva son: " + dias_fase_reproductiva_cultivo_dos)
            print("El detalle de la fase reproductiva es: " + detalle_fase_reproductiva_cultivo_dos)
        elif (operacion_cultivo == 3):
            print("Para el cultivo: " + nombre_cultivo_tres)
            print("Los horarios de la fase vegetativa son: " + dias_fase_vegetativa_cultivo_tres)
            print("El detalle de la fase vegetativa es: " + detalle_fase_vegetativa_cultivo_tres)
            print("Los horarios de la fase reproductiva son: " + dias_fase_reproductiva_cultivo_tres)
            print("El detalle de la fase reproductiva es: " + detalle_fase_reproductiva_cultivo_tres)
        else:
            print("El cultivo con identificación " + str(operacion_cultivo) + " no existe")
    elif (operacion == 3):
        print(" *************************** Saliendo *************************** ")
    else:
        print("Error!! Opción no válida")