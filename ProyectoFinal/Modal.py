from tkinter import *

def ventana_mensaje(mensaje, ventana_padre, opcion):
    ## Crea la ventana hija.
    t1 = Toplevel(ventana_padre)

    ## Establece el tamaño para la ventana.
    t1.geometry('800x200')

    ## Provoca que la ventana tome el focus
    t1.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t1.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t1.transient(master=ventana_padre)

    ## Crea un widget Label en la ventana
    if(opcion == 1):
        Label(t1, text=mensaje, fg="red").pack(padx=10, pady=10)
    else:
        Label(t1, text=mensaje, fg="blue").pack(padx=10, pady=10)

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.
    Button(t1, text="Cerrar", command=t1.destroy).pack()

    ## Pausa el mainloop de la ventana de donde se hizo la invocación.
    t1.wait_window(t1)