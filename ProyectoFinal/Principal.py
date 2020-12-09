from tkinter import *
from tkinter import ttk
import csv
import Utilidades
import Modal

main_window = Tk()

main_window.title("Mis Finanzas")
main_window.geometry("1750x860")
fila = 4
fila_para_carga = 4
identificador = 0
presupuesto = {'Enero': {}, 'Febrero': {}, 'Marzo': {}, 'Abril': {}, 'Mayo': {},'Junio': {}, 'Julio': {}, 'Agosto': {},
              'Septiembre': {}, 'Octubre': {}, 'Noviembre': {}, 'Diciembre': {}}

gasto_enero = {}
gasto_febrero = {}
gasto_marzo = {}
gasto_abril = {}
gasto_mayo = {}
gasto_junio = {}
gasto_julio = {}
gasto_agosto = {}
gasto_septiembre = {}
gasto_octubre = {}
gasto_noviembre = {}
gasto_diciembre = {}

def crear_headers():
    Label(main_window, text="ID", font=('Arial', 11)).grid(row = 4,column=1,pady=10)
    Label(main_window, text="FECHA", font=('Arial', 11)).grid(row=4, column=2,columnspan=2,pady=10)
    Label(main_window, text="CONCEPTO", font=('Arial', 11)).grid(row=4, column=4,columnspan=2, pady=10)
    Label(main_window, text="DETALLE", font=('Arial', 11)).grid(row=4, column=6, columnspan=2, pady=10)
    Label(main_window, text="TIPO", font=('Arial', 11)).grid(row=4, column=8,columnspan=2, pady=10)
    Label(main_window, text="VALOR", font=('Arial', 11)).grid(row=4, column=10, columnspan=2, pady=10)

def cargar_datos_desde_archivos():
    presupuesto = Utilidades.llenar_diccionario_presupuesto()
    for mes in presupuesto:
        #print(mes)#es solo la clave, es el mes
        #print(presupuesto[mes])#es el valor
        fila_mes = presupuesto[mes]
        for detalle in fila_mes:
            #print(detalle)#es solo la clave, es el identificador
            lista_detalle = fila_mes[detalle]
            #print(fila_mes[detalle]) #detalle
            #print(lista_detalle[0])
            if (mes == 'Enero'):
                gasto_enero[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_enero
            elif (mes == 'Febrero'):
                gasto_febrero[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_febrero
            elif (mes == 'Marzo'):
                gasto_marzo[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_marzo
            elif (mes == 'Abril'):
                gasto_abril[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_abril
            elif (mes == 'Mayo'):
                gasto_mayo[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_mayo
            elif (mes == 'Junio'):
                gasto_junio[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_junio
            elif (mes == 'Julio'):
                gasto_julio[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_julio
            elif (mes == 'Agosto'):
                gasto_agosto[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_agosto
            elif (mes == 'Septiembre'):
                gasto_septiembre[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_septiembre
            elif (mes == 'Octubre'):
                gasto_octubre[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_octubre
            elif (mes == 'Noviembre'):
                gasto_noviembre[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_noviembre
            elif (mes == 'Diciembre'):
                gasto_diciembre[detalle] = [lista_detalle[0], lista_detalle[1], lista_detalle[2], lista_detalle[3], lista_detalle[4]]
                #presupuesto[mes] = gasto_diciembre

def crear_label(mes,lista_detalles,valor_fila):
    Label(main_window, text=mes).grid(row=valor_fila, column=1)
    Label(main_window, text=lista_detalles[0]).grid(row=valor_fila, column=2, columnspan=2)
    Label(main_window, text=lista_detalles[1]).grid(row=valor_fila, column=4, columnspan=2)
    Label(main_window, text=lista_detalles[2]).grid(row=valor_fila, column=6, columnspan=2)
    Label(main_window, text=lista_detalles[3]).grid(row=valor_fila, column=8, columnspan=2)
    Label(main_window, text=lista_detalles[4]).grid(row=valor_fila, column=10, columnspan=2)

def cargar_datos_mes():
    #print(gasto_enero)
    global fila_para_carga, fila
    selector_mes = combo_mes.get()
    if (selector_mes == 'Enero'):
        if(gasto_enero):
            for valor_mes in gasto_enero:
                lista_detalle = gasto_enero[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes,lista_detalle,fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Enero",main_window,1)
    elif (selector_mes == 'Febrero'):
        if(gasto_febrero):
            for valor_mes in gasto_febrero:
                lista_detalle = gasto_febrero[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Febrero", main_window, 1)
    elif (selector_mes == 'Marzo'):
        if(gasto_marzo):
            for valor_mes in gasto_marzo:
                lista_detalle = gasto_marzo[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes,lista_detalle,fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Marzo",main_window,1)
    elif (selector_mes == 'Abril'):
        if(gasto_abril):
            for valor_mes in gasto_abril:
                lista_detalle = gasto_abril[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Abril", main_window, 1)
    elif (selector_mes == 'Mayo'):
        if(gasto_mayo):
            for valor_mes in gasto_mayo:
                lista_detalle = gasto_mayo[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes,lista_detalle,fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Mayo", main_window, 1)
    elif (selector_mes == 'Junio'):
        if(gasto_junio):
            for valor_mes in gasto_junio:
                lista_detalle = gasto_junio[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Junio", main_window, 1)
    elif (selector_mes == 'Julio'):
        if(gasto_julio):
            for valor_mes in gasto_julio:
                lista_detalle = gasto_julio[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Julio", main_window, 1)
    elif (selector_mes == 'Agosto'):
        if(gasto_agosto):
            for valor_mes in gasto_agosto:
                lista_detalle = gasto_agosto[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Agosto", main_window, 1)
    elif (selector_mes == 'Septiembre'):
        if(gasto_septiembre):
            for valor_mes in gasto_septiembre:
                lista_detalle = gasto_septiembre[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Septiembre", main_window, 1)
    elif (selector_mes == 'Octubre'):
        if(gasto_octubre):
            for valor_mes in gasto_octubre:
                lista_detalle = gasto_octubre[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Octubre", main_window, 1)
    elif (selector_mes == 'Noviembre'):
        if(gasto_noviembre):
            for valor_mes in gasto_noviembre:
                lista_detalle = gasto_noviembre[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Noviembre", main_window, 1)
    elif (selector_mes == 'Diciembre'):
        if(gasto_diciembre):
            for valor_mes in gasto_diciembre:
                lista_detalle = gasto_diciembre[valor_mes]
                fila_para_carga = fila_para_carga + 1
                crear_label(valor_mes, lista_detalle, fila_para_carga)
            fila = fila_para_carga
            fila_para_carga = 4
        else:
            Modal.ventana_mensaje("No hay movimientos para el mes de Diciembre", main_window, 1)

def agregar_gasto_ingreso_tabla(fecha,concepto,detalle,tipo,valor):
    global fila, identificador
    fila = fila + 1
    #consultar el valor actual de la secuencia para identificar el gasto
    identificador = Utilidades.siguiente_valor_identificador()
    identificador += 1
    Label(main_window, text=identificador).grid(row = fila,column=1)
    Label(main_window, text=fecha).grid(row=fila, column=2,columnspan=2)
    Label(main_window, text=concepto).grid(row=fila, column=4,columnspan=2)
    Label(main_window, text=detalle).grid(row=fila, column=6,columnspan=2)
    Label(main_window, text=tipo).grid(row=fila, column=8,columnspan=2)
    Label(main_window, text=valor).grid(row=fila, column=10,columnspan=2)

def limpiar_campos_al_agregar():
    textbox_fecha.delete(0,"end")
    textbox_concepto.delete(0,"end")
    textbox_detalle.delete(0,"end")
    textbox_valor.delete(0,"end")
    combo_tipo.delete(0,"end")

def guardar_informacion_presupuesto(fecha,concepto,detalle,tipo,valor):
    mes = combo_mes.get()
    if(mes == 'Enero'):
        gasto_enero[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_enero
    elif(mes == 'Febrero'):
        gasto_febrero[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_febrero
    elif (mes == 'Marzo'):
        gasto_marzo[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_marzo
    elif (mes == 'Abril'):
        gasto_abril[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_abril
    elif (mes == 'Mayo'):
        gasto_mayo[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_mayo
    elif (mes == 'Junio'):
        gasto_junio[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_junio
    elif (mes == 'Julio'):
        gasto_julio[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_julio
    elif (mes == 'Agosto'):
        gasto_agosto[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_agosto
    elif (mes == 'Septiembre'):
        gasto_septiembre[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_septiembre
    elif (mes == 'Octubre'):
        gasto_octubre[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_octubre
    elif (mes == 'Noviembre'):
        gasto_noviembre[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_noviembre
    elif (mes == 'Diciembre'):
        gasto_diciembre[identificador] = [fecha, concepto, detalle, tipo, valor]
        presupuesto[mes] = gasto_diciembre

    Utilidades.guardar_en_archivo(mes,identificador,fecha,concepto,detalle,tipo,valor)

def agregar_gasto():
    if textbox_fecha.get() == "" or textbox_concepto.get()== "" or textbox_detalle.get()== "" or combo_tipo.get() == "" \
            or textbox_valor.get() == "" or combo_mes.get() == "":
        Modal.ventana_mensaje("Por favor ingrese valores en los campos de mes, fecha, concepto, detalle, tipo y valor",main_window,1)
    else:
        #validar si el valor es numérico
        if (Utilidades.esNumerico(textbox_valor.get())):
            if(Utilidades.esFechaCorrecta(textbox_fecha.get())):
                agregar_gasto_ingreso_tabla(textbox_fecha.get(), textbox_concepto.get(),
                                            textbox_detalle.get(), combo_tipo.get(), textbox_valor.get())

                guardar_informacion_presupuesto(textbox_fecha.get(), textbox_concepto.get(),
                                            textbox_detalle.get(), combo_tipo.get(), textbox_valor.get())

                limpiar_campos_al_agregar()
            else:
                Modal.ventana_mensaje("Formato de fecha incorrecta", main_window,1)
        else:
            Modal.ventana_mensaje("Debe ingresar un valor numérico en el campo valor",main_window,1)

def liquidar_mes():
    mes = combo_mes.get()
    if(mes == ""):
        Modal.ventana_mensaje("Para liquidar debe seleccionar un mes",main_window,1)
    elif (mes == 'Enero'):
        Utilidades.liquidar_mes(main_window,gasto_enero)
    elif (mes == 'Febrero'):
        Utilidades.liquidar_mes(main_window,gasto_febrero)
    elif (mes == 'Marzo'):
        Utilidades.liquidar_mes(main_window,gasto_marzo)
    elif (mes == 'Abril'):
        Utilidades.liquidar_mes(main_window,gasto_abril)
    elif (mes == 'Mayo'):
        Utilidades.liquidar_mes(main_window,gasto_mayo)
    elif (mes == 'Junio'):
        Utilidades.liquidar_mes(main_window,gasto_junio)
    elif (mes == 'Julio'):
        Utilidades.liquidar_mes(main_window,gasto_julio)
    elif (mes == 'Agosto'):
        Utilidades.liquidar_mes(main_window,gasto_agosto)
    elif (mes == 'Septiembre'):
        Utilidades.liquidar_mes(main_window,gasto_septiembre)
    elif (mes == 'Octubre'):
        Utilidades.liquidar_mes(main_window,gasto_octubre)
    elif (mes == 'Noviembre'):
        Utilidades.liquidar_mes(main_window,gasto_noviembre)
    elif (mes == 'Diciembre'):
        Utilidades.liquidar_mes(main_window,gasto_diciembre)

text_titulo = "MIS FINANZAS"
lbl_titulo = Label(main_window, text=text_titulo,font=('Arial',15))
lbl_titulo.grid(row = 0, column = 0, columnspan=16,pady=10)

text_seleccion_mes = "* Seleccione el mes"
lbl_seleccion_mes = Label(main_window, text=text_seleccion_mes,font=('Arial',11))
lbl_seleccion_mes.grid(row = 1, column = 0, pady=10)

combo_mes = ttk.Combobox(main_window,
                            values=[
                                    "Enero",
                                    "Febrero",
                                    "Marzo",
                                    "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])

combo_mes.grid(row=1, column = 1,pady=10)

text_cargar_datos = "Cargar datos mes"
btn_cargar_datos = Button(main_window, text=text_cargar_datos, command=cargar_datos_mes)
btn_cargar_datos.grid(row = 1, column = 2, padx = 10, pady = 40)

text_liquidar = "Liquidar mes"
btn_liquidar = Button(main_window, text=text_liquidar, command=liquidar_mes)
btn_liquidar.grid(row = 3, column = 0, padx = 10, pady = 40)

img_agregar = PhotoImage(file='img/agregar.png') #Asignamos una variable al archivo dela imagen
text_agregar = "Agregar"
btn_agregar = Button(main_window, text=text_agregar, image=img_agregar, command=agregar_gasto) #Asignamos la imagen como una propiedad del label
btn_agregar.grid(row = 2, column = 12,padx=10,pady=40)

img_modificar = PhotoImage(file='img/modificar.png') #Asignamos una variable al archivo dela imagen
text_modificar = "Modificar"
btn_modificar = Button(main_window, text=text_modificar, image=img_modificar) #Asignamos la imagen como una propiedad del label
btn_modificar.grid(row = 2, column = 13,padx=10,pady=40)

img_eliminar = PhotoImage(file='img/eliminar.png') #Asignamos una variable al archivo dela imagen
text_eliminar = "Eliminar"
btn_eliminar = Button(main_window, text=text_eliminar, image=img_eliminar) #Asignamos la imagen como una propiedad del label
btn_eliminar.grid(row = 2, column = 14,padx=10,pady=40)

img_buscar = PhotoImage(file='img/buscar.png') #Asignamos una variable al archivo dela imagen
text_buscar = "Buscar"
btn_buscar = Button(main_window, text=text_buscar, image=img_buscar) #Asignamos la imagen como una propiedad del label
btn_buscar.grid(row = 2, column = 15, padx=10, pady=40)

text_id = "Identificador"
lbl_identificador = Label(main_window, text=text_id,font=('Arial',11))
lbl_identificador.grid(row = 2, column = 0)

textbox_identificador = Entry(main_window)
textbox_identificador.grid(row = 2,column = 1)

text_fecha = "* Fecha (dd/mm/aaaa)"
lbl_fecha = Label(main_window, text=text_fecha,font=('Arial',11))
lbl_fecha.grid(row = 2, column = 2)

textbox_fecha = Entry(main_window)
textbox_fecha.grid(row = 2, column = 3)

text_concepto = "* Concepto"
lbl_concepto = Label(main_window, text=text_concepto,font=('Arial',11))
lbl_concepto.grid(row = 2, column = 4)

textbox_concepto = Entry(main_window)
textbox_concepto.grid(row = 2, column = 5)

text_detalle = "* Detalle"
lbl_detalle = Label(main_window, text=text_detalle,font=('Arial',11))
lbl_detalle.grid(row = 2, column = 6)

textbox_detalle = Entry(main_window)
textbox_detalle.grid(row = 2 ,column = 7)

text_tipo = "* Tipo"
lbl_tipo = Label(main_window, text=text_tipo,font=('Arial',11))
lbl_tipo.grid(row = 2, column = 8)

combo_tipo = ttk.Combobox(main_window,
                            values=["Gasto","Ingreso"])

combo_tipo.grid(row=2, column = 9)

text_valor = "* Valor"
lbl_valor = Label(main_window, text=text_valor,font=('Arial',11))
lbl_valor.grid(row = 2, column = 10)

textbox_valor = Entry(main_window)
textbox_valor.grid(row = 2 ,column = 11)

text_resumen = "RESUMEN"
lbl_resumen = Label(main_window, text=text_resumen, font=('Arial',11))
lbl_resumen.grid(row = 3, column = 1)

crear_headers()
cargar_datos_desde_archivos()

main_window.mainloop()
