# Autor: Andres Mauricio Ortiz
# Fecha: 10/09/2020
# Sistema de facturación
import os
from datetime import datetime

TIPO_DE_EMPRESA = "Asadero y Restaurante"
NOMBRE_DE_EMPRESA = "POLLOS PICOCHIN"
NIT_EMPRESA = "92456951-8"
VALOR_IVA = 0.19
VALOR_PROPINA = 0.20

print(" **************** SISTEMA DE FACTURACIÓN "+NOMBRE_DE_EMPRESA + " ****************")
plato_producto_uno = str(input("Por favor ingrese el nombre del plato 1: "))
cantidad_uno = int(input("Por favor ingrese la cantidad: "))
valor_unidad_uno = float(input("Por favor ingrese el valor unitario: "))
valor_total_uno = float(input("Por favor ingrese el valor total: "))
print()
plato_producto_dos = str(input("Por favor ingrese el nombre del plato 2: "))
cantidad_dos = int(input("Por favor ingrese la cantidad: "))
valor_unidad_dos = float(input("Por favor ingrese el valor unitario: "))
valor_total_dos = float(input("Por favor ingrese el valor total: "))
print()
plato_producto_tres = str(input("Por favor ingrese el nombre del plato 3: "))
cantidad_tres = int(input("Por favor ingrese la cantidad: "))
valor_unidad_tres = float(input("Por favor ingrese el valor unitario: "))
valor_total_tres = float(input("Por favor ingrese el valor total: "))
print()
plato_producto_cuatro = str(input("Por favor ingrese el nombre del plato 4: "))
cantidad_cuatro = int(input("Por favor ingrese la cantidad: "))
valor_unidad_cuatro = float(input("Por favor ingrese el valor unitario: "))
valor_total_cuatro = float(input("Por favor ingrese el valor total: "))

total_bruto =+valor_total_uno+valor_total_dos+valor_total_tres+valor_total_cuatro
iva = total_bruto * VALOR_IVA
subtotal = total_bruto - iva
total_con_propina = total_bruto + (total_bruto * float(VALOR_PROPINA))
print()
print(" **************** FACTURA DE VENTA ****************")
print()
print("                                "+TIPO_DE_EMPRESA+"                                ")
print("                                "+NOMBRE_DE_EMPRESA+"                              ")
print("                               Nit. "+NIT_EMPRESA+"                              ")
print("                               "+str(datetime.now())+"                           ")
print(" CANTIDAD ----- PLATO (PRODUCTO) ---------------- VALOR UNITARIO ----- VALOR TOTAL")
print(str(cantidad_uno)+" ----------- "+ plato_producto_uno+ " ------------------- $"+ str(valor_unidad_uno) + " ------------------- $"+ str(valor_total_uno))
print(str(cantidad_dos)+" ----------- "+ plato_producto_dos+ " -------------- $"+ str(valor_unidad_dos) + " --------------- $"+ str(valor_total_dos))
print(str(cantidad_tres)+" ----------- "+ plato_producto_tres+ " ----------------------- $"+ str(valor_unidad_tres) + " ---------------------- $"+ str(valor_total_tres))
print(str(cantidad_cuatro)+" ----------- "+ plato_producto_cuatro+ " ----------------------- $"+ str(valor_unidad_cuatro) + " ---------------------- $"+ str(valor_total_cuatro))
print("-------------------------------------------------------------------------------------------------------")
print("              Subtotal                                                                         $ "+ str(subtotal))
print("              IVA                                                                              $ "+ str(iva))
print("              Total                                                                            $ "+ str(total_bruto))
print("              Total con propina del 20%                                                        $ "+ str(total_con_propina))
print()
print(" **************** FIN FACTURA DE VENTA ****************")
file = open("/home/programador/Documents/Desarrollo de Software/CursoPython/factura.txt", "w")
file.write("                                "+TIPO_DE_EMPRESA+"                                " + os.linesep)
file.write("                                "+NOMBRE_DE_EMPRESA+"                                " + os.linesep)
file.write("                               Nit. "+NIT_EMPRESA+"                              " + os.linesep)
file.write("                               "+str(datetime.now())+"                           " + os.linesep)
file.write(" CANTIDAD ----- PLATO (PRODUCTO) ---------------- VALOR UNITARIO ----- VALOR TOTAL" + os.linesep)
file.write(str(cantidad_uno)+" ----------- "+ plato_producto_uno+ " ------------------- $"+ str(valor_unidad_uno) + " ------------------- $"+ str(valor_total_uno)+ os.linesep)
file.write(str(cantidad_dos)+" ----------- "+ plato_producto_dos+ " -------------- $"+ str(valor_unidad_dos) + " --------------- $"+ str(valor_total_dos)+ os.linesep)
file.write(str(cantidad_tres)+" ----------- "+ plato_producto_tres+ " ----------------------- $"+ str(valor_unidad_tres) + " ---------------------- $"+ str(valor_total_tres)+ os.linesep)
file.write(str(cantidad_cuatro)+" ----------- "+ plato_producto_cuatro+ " ----------------------- $"+ str(valor_unidad_cuatro) + " ---------------------- $"+ str(valor_total_cuatro)+ os.linesep)
file.write("-------------------------------------------------------------------------------------------------------"+os.linesep)
file.write("              Subtotal                                                                         $ "+ str(subtotal)+os.linesep)
file.write("              IVA                                                                              $ "+ str(iva)+os.linesep)
file.write("              Total                                                                            $ "+ str(total_bruto)+os.linesep)
file.write("              Total con propina del 20%                                                        $ "+ str(total_con_propina)+os.linesep)
file.close()