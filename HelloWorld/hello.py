# Se crea un Diccionario con Iniciales de Días de la Semana
my_schedule = {'L': {}, 'M': {}, 'W': {}, 'J': {}, 'V': {}}

# Se crea un Sistema de Menú sencillo
repeat_menu = True
while repeat_menu:
    print('0 - Agregar Clase')
    print('1 - Modificar Clase')
    print('2 - Eliminar Clase')
    print('3 - Ver Horario')
    menu_selection = int(input('Ingrese su Opción: '))
    if menu_selection == 0:
        print(' ========== AGREGAR CLASE ========== ')
        day_selection = ''
        while day_selection not in my_schedule:
            day_selection = input('Ingrese el día para la Nueva Clase: ')

            # Se evalúa la existencia de un Día en el Diccionario
            if day_selection not in my_schedule: print('No se encuentra el día ingresado.')

        hour_selection = ''
        while hour_selection not in my_schedule[day_selection]:
            hour_selection = int(input('Ingrese la hora para la Nueva Clase: '))

            # Se evalúa la existencia de una Hora en el Diccionario del Día
            if hour_selection in my_schedule[day_selection]:
                print('Esta hora ya es usada por', my_schedule[day_selection][hour_selection])
            else:
                new_class = input('Ingrese el nombre de la Clase: ')
                my_schedule[day_selection][hour_selection] = new_class
                print('Se agregó la Clase', new_class, 'el día', day_selection, 'a la hora', hour_selection)

    elif menu_selection == 1:
        print(' ========== MODIFICAR CLASE ========== ')
        day_selection = ''
        while day_selection not in my_schedule:
            day_selection = input('Ingrese el día de la Clase a Modificar: ')

            # Se evalúa la existencia de un Día en el Diccionario
            if day_selection not in my_schedule:
                print('No se encuentra el día ingresado.')

        hour_selection = ''
        while hour_selection not in my_schedule[day_selection]:
            hour_selection = int(input('Ingrese la hora de la Clase a Modificar: '))

            # Se evalúa la existencia de una Hora en el Diccionario del Día
            if hour_selection not in my_schedule:
                print('No existe Clase a esta Hora')
            else:
                new_class = input('Ingrese el nombre de la Clase: ')
                my_schedule[day_selection][hour_selection] = new_class
                print('Se cambió la clase del día', day_selection, 'a la hora', hour_selection, 'por la Clase',
                      new_class)

    elif menu_selection == 2:
        print(' ========== ELIMINAR CLASE ========== ')
        day_selection = ''
        while day_selection not in my_schedule:
            day_selection = input('Ingrese el día de la Clase a Eliminar: ')

            # Se evalúa la existencia de un Día en el Diccionario
            if day_selection not in my_schedule:
                print('No se encuentra el día ingresado.')

        hour_selection = ''
        while hour_selection not in my_schedule[day_selection]:
            hour_selection = int(input('Ingrese la hora de la Clase a Eliminar: '))

            # Se evalúa la existencia de un Día en el Diccionario
            if hour_selection not in my_schedule:
                print('No existe Clase a esta Hora.')
            else:
                current_class = my_schedule[day_selection][hour_selection]
                del_confirm = bool(int(input('¿Seguro que desea Eliminar la Clase', current_class, '? (S/N): ')))
                if del_confirm == 'S':
                    del my_schedule[day_selection][hour_selection]
                else:
                    print('Se ha cancelado la acción de Eliminar.')

    elif menu_selection == 3:
        day_selection = ''
        while day_selection not in my_schedule:
            day_selection = input('Ingrese el día para ver el Horario: ')

            # Se evalúa la existencia de un Día en el Diccionario
            if day_selection not in my_schedule:
                print('No se encuentra el día ingresado.')
            else:
                for i in my_schedule[day_selection].keys():
                    print('Hora:', i, '- Clase:', my_schedule[day_selection][i])
    else:
        print('Opción Invalida')

    repeat_menu = bool(int(input('\n¿Desea continuar? (S/N): ')))
    if repeat_menu == 'S':
        repeat_menu = True
    else:
        repeat_menu = False
    print()