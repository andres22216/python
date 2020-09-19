# Aplicación para registros de cultivos estudiantiles
# Fecha: Septiembre 2 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

#definición de variables para los cultivos

#cultivo 1
nombre_cultivo_uno=""
cantidad_de_cultivo_uno=0
tiempo_del_cultivo_uno=0.0
tiene_problemas_uno=""
observaciones_sobre_el_cultivo_uno=""

#cultivo 2
nombre_cultivo_dos=""
cantidad_de_cultivo_dos=0
tiempo_del_cultivo_dos=0.0
tiene_problemas_dos=""
observaciones_sobre_el_cultivo_dos=""

#cultivo 3
nombre_cultivo_tres=""
cantidad_de_cultivo_tres=0
tiempo_del_cultivo_tres=0.0
tiene_problemas_tres=""
observaciones_sobre_el_cultivo_tres=""

#cultivo 4
nombre_cultivo_cuatro=""
cantidad_de_cultivo_cuatro=0
tiempo_del_cultivo_cuatro=0.0
tiene_problemas_cuatro=""
observaciones_sobre_el_cultivo_cuatro=""

print("**************** PROGRAMA PARA REGISTRAR INFORMACIÓN DE LOS CULTIVOS DE LA HUERTA ESTUDIANTIL **************** ")
#capturamos los datos por consola para el cultivo 1 usando la función input y los asignamos a las variables
print("")
print("**************** Por favor ingrese los datos del cultivo 1 ****************")
print("")
nombre_cultivo_uno = str(input("Por favor ingrese el nombre del cultivo: "))
cantidad_de_cultivo_uno = int(input("Por favor ingrese la cantidad del cultivo: "))
tiempo_del_cultivo_uno = float(input("Por favor ingrese el tiempo que tiene el cultivo (puede ingresar valores como 1.5 meses): "))
tiene_problemas_uno = bool(str(input("Por favor ingrese si el cultivo tiene problemas (SI-NO): ")))
observaciones_sobre_el_cultivo_uno = str(input("Por favor ingrese observaciones sobre el cultivo: "))
#capturamos los datos por consola para el cultivo 2 usando la función input y los asignamos a las variables
print("")
print("**************** Por favor ingrese los datos del cultivo 2 ****************")
print("")
nombre_cultivo_dos = str(input("Por favor ingrese el nombre del cultivo: "))
cantidad_de_cultivo_dos = int(input("Por favor ingrese la cantidad del cultivo: "))
tiempo_del_cultivo_dos = float(input("Por favor ingrese el tiempo que tiene el cultivo (puede ingresar valores como 1.5 meses): "))
tiene_problemas_dos = bool(str(input("Por favor ingrese si el cultivo tiene problemas (SI-NO): ")))
observaciones_sobre_el_cultivo_dos = str(input("Por favor ingrese observaciones sobre el cultivo: "))
#capturamos los datos por consola para el cultivo 3 usando la función input y los asignamos a las variables
print("")
print("**************** Por favor ingrese los datos del cultivo 3 ****************")
print("")
nombre_cultivo_tres = str(input("Por favor ingrese el nombre del cultivo: "))
cantidad_de_cultivo_tres = int(input("Por favor ingrese la cantidad del cultivo: "))
tiempo_del_cultivo_tres = float(input("Por favor ingrese el tiempo que tiene el cultivo (puede ingresar valores como 1.5 meses): "))
tiene_problemas_tres = bool(str(input("Por favor ingrese si el cultivo tiene problemas (SI-NO): ")))
observaciones_sobre_el_cultivo_tres = str(input("Por favor ingrese observaciones sobre el cultivo: "))
#capturamos los datos por consola para el cultivo 4 usando la función input y los asignamos a las variables
print("")
print("**************** Por favor ingrese los datos del cultivo 4 ****************")
print("")
nombre_cultivo_cuatro = str(input("Por favor ingrese el nombre del cultivo: "))
cantidad_de_cultivo_cuatro = int(input("Por favor ingrese la cantidad del cultivo: "))
tiempo_del_cultivo_cuatro = float(input("Por favor ingrese el tiempo que tiene el cultivo (puede ingresar valores como 1.5 meses): "))
tiene_problemas_cuatro = bool(str(input("Por favor ingrese si el cultivo tiene problemas (SI-NO): ")))
observaciones_sobre_el_cultivo_cuatro = str(input("Por favor ingrese observaciones sobre el cultivo: "))
print("")
#mostramos por pantalla los datos de los cultivos
print("**************** DATOS REGISTRADOS PARA LOS CULTIVOS **************** ")
print("")
print("**************** DATOS REGISTRADOS PARA EL CULTIVO 1 ****************")
print("Nombre del cultivo: " + nombre_cultivo_uno)
print("Cantidad del cultivo: " + str(cantidad_de_cultivo_uno))
print("Edad del cultivo: " + str(tiempo_del_cultivo_uno))
print("Problemas del cultivo (True=SI y False=NO): " + str(tiene_problemas_uno))
print("Observaciones del cultivo: " + observaciones_sobre_el_cultivo_uno)
print("-----------------------------------------------------------------------------------")
print("**************** DATOS REGISTRADOS PARA EL CULTIVO 2 ****************")
print("Nombre del cultivo: " + nombre_cultivo_dos)
print("Cantidad del cultivo: " + str(cantidad_de_cultivo_dos))
print("Edad del cultivo: " + str(tiempo_del_cultivo_dos))
print("Problemas del cultivo (True=SI y False=NO): " + str(tiene_problemas_dos))
print("Observaciones del cultivo: " + observaciones_sobre_el_cultivo_dos)
print("-----------------------------------------------------------------------------------")
print("**************** DATOS REGISTRADOS PARA EL CULTIVO 3 ****************")
print("Nombre del cultivo: " + nombre_cultivo_tres)
print("Cantidad del cultivo: " + str(cantidad_de_cultivo_tres))
print("Edad del cultivo: " + str(tiempo_del_cultivo_tres))
print("Problemas del cultivo (True=SI y False=NO): " + str(tiene_problemas_tres))
print("Observaciones del cultivo: " + observaciones_sobre_el_cultivo_tres)
print("-----------------------------------------------------------------------------------")
print("**************** DATOS REGISTRADOS PARA EL CULTIVO 4 ****************")
print("Nombre del cultivo: " + nombre_cultivo_cuatro)
print("Cantidad del cultivo: " + str(cantidad_de_cultivo_cuatro))
print("Edad del cultivo: " + str(tiempo_del_cultivo_cuatro))
print("Problemas del cultivo (True=SI y False=NO): " + str(tiene_problemas_cuatro))
print("Observaciones del cultivo: " + observaciones_sobre_el_cultivo_cuatro)
