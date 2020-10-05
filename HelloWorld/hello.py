print("Hello world!!!!!!")
a = int("18")
print("Tengo "+ str(a) + " años")

nombre: str = input("ingrese su nombre: ")

prueba_flotante = 5.80

print(nombre)
print(prueba_flotante)

nombre = input("Ingrese su nombre nuevamente: ")
edad = int(input("Ingrese su eded: "))
print("Hola a todos soy "+nombre+" y tengo "+str(edad)+" años")


# Este código es solo un ejemplo que está construído únicamente con fines educativos
# Aplique y adapte sus propios conocimientos para la solución de la Práctica

# Ingreso del producto o cultivo a gestionar

while (True):
    productoValido = False
    accionValida = False

    while (accionValida == False):

        # Muestra menú de las acciones
        accion = input("""
            MENÚ -------
            Elija una acción:
            1. GESTIÓN DEL CULTIVO
            2. VER ETAPAS DEL CULTIVO
            3. Salir
            """)

        if (accion == "1"):
            # GESTIÓN DEL CULTIVO
            productoValido = False

            # Se pide el producto que desea gestionar
            while (productoValido == False):
                # Mientras no se ingrese un producto válido, seguirá pidiendolo
                cultivo = input("Nombre del cultivo (maiz ó arroz) : ")
                if (cultivo == "maiz"):
                    productoValido = True
                elif (cultivo == "arroz"):
                    productoValido = True
                else:
                    productoValido = False

            print("GESTIÓN DE CULTIVO DE --> " + cultivo)

            if (cultivo == "maiz"):
                # Días y horarios para actividades sobre el cultivo
                print("""
            DIAS Y HORARIOS RECOMENDADOS 

            Mantenimiento: 
                Lunes, 4:00 pm
                Viernes, 6:00 pm

            Regado:
                Martes, Jueves y Sábado, 8:00 am
                Domingo Y Lunes 10:00 am

            Abono:
                Martes, 5:00 pm
                Sábado, 7:00 am

                """)

            elif (cultivo == "arroz"):
                print("""
          DIAS Y HORARIOS RECOMENDADOS 

          Mantenimiento: 
              Miercoles y Jueves, 7:00 am
              Sábado y Domingo, 8:00 am

          Regado:
              Martes y Sábado, 10:00 am

          Abono:
              Lunes, 8:00 pm

              """)

        elif (accion == "2"):
            # ETAPAS DE UN CULTIVO
            productoValido = False

            # Se pide el producto que se desea
            while (productoValido == False):
                # Mientras no se ingrese un producto válido, seguira pidiendolo
                cultivo = input("Nombre del cultivo:  ")
                if (cultivo == "maiz"):
                    productoValido = True
                elif (cultivo == "arroz"):
                    productoValido = True
                else:
                    print("Producto no encontrado...")
                    productoValido = False

            print("ETAPAS DE CULTIVO DE --> " + cultivo)

            if (cultivo == "maiz"):
                # Días y horarios para actividades sobre el cultivo
                print("""
            ETAPA 1 - Fase Vegetativa
              De 5 a 30 días luego de la siembra
              - Crecimiento de las plántulas
              - Crecimiento vegetativo

            ETAPA 2 - Fase reproductiva
              De 55 a 112 días después de la siembra
              - Floración y la fecundación 
              - Llenado de grano y la madurez 

                """)

            elif (cultivo == "arroz"):
                print("""

            ETAPA 1 - Fase Vegetativa
              - Se da desde los 4 a los 65 días.
              - La planta se desarrolla desde la semilla
                hasta obtener un cuerpo vegetal.

            ETAPA 2 - Fase reproductiva
              - Se da de los 60 a los 76 días 
              - La planta se encuentra en su estado de floración

            ETAPA 3 - Fase maduración 
              - Se da de 110 a 12 días
              - La planta adquiere madurez en su floración
                completando el crecicimiento 
                del producto que ahora está listo para cosechar.

              """)
        elif (accion == "3"):
            break

        else:
            print("       Opción inválida")