# Aplicación para registro de producots de la tienda escolar
# Fecha: Septiembre 13 de 2020
# Autor: Andrés Mauricio Ortiz Gallego

#Declaración de variables
capital_total = 0.0
capital_total_actual = 0.0
valor_total_compra_productos = 0.0
valor_total_de_ventas = 0.0
ganancia_total = 0.0

# variables producto 1
nombre_producto_uno = ""
cantidad_producto_uno = 0
valor_producto_uno = 0.0
valor_para_venta_prod_uno = 0.0
total_unidades_vendidas_prod_uno = 0
total_vendido_producto_uno = 0.0

#variables producto 2
nombre_producto_dos = ""
cantidad_producto_dos = 0
valor_producto_dos = 0.0
valor_para_venta_prod_dos = 0.0
total_unidades_vendidas_prod_dos = 0
total_vendido_producto_dos = 0.0

#variables producto 3
nombre_producto_tres = ""
cantidad_producto_tres = 0
valor_producto_tres = 0.0
valor_para_venta_prod_tres = 0.0
total_unidades_vendidas_prod_tres = 0
total_vendido_producto_tres = 0.0

#variables producto 4
nombre_producto_cuatro = ""
cantidad_producto_cuatro = 0
valor_producto_cuatro = 0.0
valor_para_venta_prod_cuatro = 0.0
total_unidades_vendidas_prod_cuatro = 0
total_vendido_producto_cuatro = 0.0
#Sección para el Ingreso de productos
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
print("|     PROGRAMA DE REGISTRO DE PRODUCTOS PARA LA TIENDA ESCOLAR    |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
print("")
capital_total = float(input("Por favor ingrese el capital total: "))
print("")
print("INGRESO DE PRODUCTOS")
print("")
print("Producto 1")
nombre_producto_uno = input("Por favor ingrese el nombre: ")
cantidad_producto_uno = int(input("Por favor ingrese la cantidad comprada: "))
valor_producto_uno = float(input("Por favor ingrese el valor de compra: "))
print("")
#Calculamos el valor unitario del producto 1
print("El valor unitario del producto 1 es: "+str(valor_producto_uno/cantidad_producto_uno))
print("")
valor_para_venta_prod_uno = float(input("Por favor ingrese el valor de venta: "))
print("")
print("Producto 2")
nombre_producto_dos = input("Por favor ingrese el nombre: ")
cantidad_producto_dos = int(input("Por favor ingrese la cantidad comprada: "))
valor_producto_dos = float(input("Por favor ingrese el valor de compra: "))
print("")
#Calculamos el valor unitario del producto 2
print("El valor unitario del producto 2 es: "+str(valor_producto_dos/cantidad_producto_dos))
print("")
valor_para_venta_prod_dos = float(input("Por favor ingrese el valor de venta: "))
print("")
print("Producto 3")
nombre_producto_tres = input("Por favor ingrese el nombre: ")
cantidad_producto_tres = int(input("Por favor ingrese la cantidad comprada: "))
valor_producto_tres = float(input("Por favor ingrese el valor de compra: "))
print("")
#Calculamos el valor unitario del producto 3
print("El valor unitario del producto 3 es: "+str(valor_producto_tres/cantidad_producto_tres))
print("")
valor_para_venta_prod_tres = float(input("Por favor ingrese el valor de venta: "))
print("")
print("Producto 4")
nombre_producto_cuatro = input("Por favor ingrese el nombre: ")
cantidad_producto_cuatro = int(input("Por favor ingrese la cantidad comprada: "))
valor_producto_cuatro = float(input("Por favor ingrese el valor de compra: "))
print("")
#Calculamos el valor unitario del producto 4
print("El valor unitario del producto 4 es: "+str(valor_producto_cuatro/cantidad_producto_cuatro))
print("")
valor_para_venta_prod_cuatro = float(input("Por favor ingrese el valor de venta: "))
print("")
#Calculos y estadisticas iniciales
#Calculamos el valor total de la compra de productos
valor_total_compra_productos = valor_producto_uno + valor_producto_dos + valor_producto_tres + valor_producto_cuatro
#Calculamos el capital actual luego de la compra
capital_total_actual = capital_total - valor_total_compra_productos
print("Valor total invertido en la compra de productos: "+str(valor_total_compra_productos))
print("")
print("El capital actual es: "+str(capital_total_actual))
print("")
#Sección para la Venta de productos
print("VENTA DE PRODUCTOS")
print("")
total_unidades_vendidas_prod_uno = int(input("Por favor ingrese la cantidad de unidades vendidas del producto 1: "))
total_unidades_vendidas_prod_dos = int(input("Por favor ingrese la cantidad de unidades vendidas del producto 2: "))
total_unidades_vendidas_prod_tres = int(input("Por favor ingrese la cantidad de unidades vendidas del producto 3: "))
total_unidades_vendidas_prod_cuatro = int(input("Por favor ingrese la cantidad de unidades vendidas del producto 4: "))
print("")
#Calculamos el valor vendido de cada producto
total_vendido_producto_uno = valor_para_venta_prod_uno * total_unidades_vendidas_prod_uno
total_vendido_producto_dos = valor_para_venta_prod_dos * total_unidades_vendidas_prod_dos
total_vendido_producto_tres = valor_para_venta_prod_tres * total_unidades_vendidas_prod_tres
total_vendido_producto_cuatro = valor_para_venta_prod_cuatro * total_unidades_vendidas_prod_cuatro
print("Valor total de las ventas del producto 1: "+str(total_vendido_producto_uno))
print("Valor total de las ventas del producto 2: "+str(total_vendido_producto_dos))
print("Valor total de las ventas del producto 3: "+str(total_vendido_producto_tres))
print("Valor total de las ventas del producto 4: "+str(total_vendido_producto_cuatro))
print("")
#Calculamos las unidades sobrantes de cada producto
print("Unidades sobrantes del producto 1: "+str((cantidad_producto_uno-total_unidades_vendidas_prod_uno)))
print("Unidades sobrantes del producto 2: "+str((cantidad_producto_dos-total_unidades_vendidas_prod_dos)))
print("Unidades sobrantes del producto 3: "+str((cantidad_producto_tres-total_unidades_vendidas_prod_tres)))
print("Unidades sobrantes del producto 4: "+str((cantidad_producto_cuatro-total_unidades_vendidas_prod_cuatro)))
print("")
#Calculos y estadisticas luego de ventas
print("ESTADISTICAS DE LAS VENTAS")
print("")
#Validamos si las ventas superaron la inversión inicial del producto 1
print("Superaron las ventas la inversión inicial en el producto uno? (True = SI, False = NO)")
print(bool(total_vendido_producto_uno>valor_producto_uno))
print("")
#Validamos si las ventas superaron la inversión inicial del producto 2
print("Superaron las ventas la inversión inicial en el producto dos? (True = SI, False = NO)")
print(bool(total_vendido_producto_dos>valor_producto_dos))
print("")
#Validamos si las ventas superaron la inversión inicial del producto 3
print("Superaron las ventas la inversión inicial en el producto tres? (True = SI, False = NO)")
print(bool(total_vendido_producto_tres>valor_producto_tres))
print("")
#Validamos si las ventas superaron la inversión inicial del producto 4
print("Superaron las ventas la inversión inicial en el producto cuatro? (True = SI, False = NO)")
print(bool(total_vendido_producto_cuatro>valor_producto_cuatro))
print("")
#Calculamos el valor total de las ventas sumando las ventas de cada producto
print("El valor total de las ventas fue:")
valor_total_de_ventas = total_vendido_producto_uno + total_vendido_producto_dos + total_vendido_producto_tres + total_vendido_producto_cuatro
print(str(valor_total_de_ventas))
print("")
#Validamos si el total de las ventas superó la inversión inicial
print("El valor total de ventas superó la inversión total? (True = SI, False = NO)")
print(bool(valor_total_de_ventas>valor_total_compra_productos))
print("")
#Calculamos la ganancia total
print("La ganacia total es: ")
ganancia_total = valor_total_de_ventas-valor_total_compra_productos
print(str(ganancia_total))
print("")
#Calculamos el capital total después de las ventas incluyendo las ganancias
print("El capital actual después de ventas es:")
print(str((capital_total + ganancia_total)))
print("")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
print("|  FIN PROGRAMA DE REGISTRO DE PRODUCTOS PARA LA TIENDA ESCOLAR   |")
print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")




