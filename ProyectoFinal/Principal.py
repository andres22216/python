from tkinter import *
from tkinter import ttk
import Utilidades
import cvs

main_window = Tk()

main_window.title("Mis Finanzas")
main_window.geometry("1750x860")
fila = 4
identificador = 0
#presupuesto = {'Enero': {}, 'Febrero': {}, 'Marzo': {}, 'Abril': {}, 'Mayo': {},'Junio': {}, 'Julio': {}, 'Agosto': {},
 #             'Septiembre': {}, 'Octubre': {}, 'Noviembre': {}, 'Diciembre': {}}

def ventana_modal(mensaje):
    ## Crea la ventana hija.
    t1 = Toplevel(main_window)

    ## Establece el tamaño para la ventana.
    t1.geometry('800x200')

    ## Provoca que la ventana tome el focus
    t1.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t1.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t1.transient(master=main_window)

    ## Crea un widget Label en la ventana
    Label(t1, text=mensaje, fg="red").pack(padx=10, pady=10)

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.
    Button(t1, text="Cerrar", command=t1.destroy).pack()

    ## Pausa el mainloop de la ventana de donde se hizo la invocación.
    t1.wait_window(t1)

def crear_headers():
    Label(main_window, text="ID", font=('Arial', 11)).grid(row = 4,column=1,pady=10)
    Label(main_window, text="FECHA", font=('Arial', 11)).grid(row=4, column=2,columnspan=2,pady=10)
    Label(main_window, text="CONCEPTO", font=('Arial', 11)).grid(row=4, column=4,columnspan=2, pady=10)
    Label(main_window, text="DETALLE", font=('Arial', 11)).grid(row=4, column=6, columnspan=2, pady=10)
    Label(main_window, text="TIPO", font=('Arial', 11)).grid(row=4, column=8,columnspan=2, pady=10)
    Label(main_window, text="VALOR", font=('Arial', 11)).grid(row=4, column=10, columnspan=2, pady=10)

def agregar_gasto_ingreso_tabla(fecha,concepto,detalle,tipo,valor):
    global fila, identificador
    fila = fila + 1
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

def agregar_al_diccionario():
    mes = combo_mes.get()
    if mes == "":
        print("Debe seleccionar un mes......")
    else:
        print("Agregar gasto......")


def agregar_gasto():
    if textbox_fecha.get() == "" or textbox_concepto.get()== "" or textbox_detalle.get()== "" or combo_tipo.get() == "" \
            or textbox_valor.get() == "" or combo_mes.get() == "":
        ventana_modal("Por favor ingrese valores en los campos de mes, fecha, concepto, detalle, tipo y valor")
    else:
        #validar si el valor es numérico
        if (Utilidades.esNumerico(textbox_valor.get())):
            agregar_gasto_ingreso_tabla(textbox_fecha.get(), textbox_concepto.get(),
                                    textbox_detalle.get(),combo_tipo.get(),textbox_valor.get())
            limpiar_campos_al_agregar()
            agregar_al_diccionario()
        else:
            ventana_modal("Debe ingresar un valor numerico en el campo valor")

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
                                    "Abril","Mayo","Junio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])

combo_mes.grid(row=1, column = 1,pady=10)

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

text_resumen = "Resumen"
lbl_resumen = Label(main_window, text=text_resumen, font=('Arial',11))
lbl_resumen.grid(row = 3, column = 1)

crear_headers()

main_window.mainloop()
