from datetime import datetime
import csv
import Modal

def esNumerico(texto):
    try:
        int(texto)
        return True
    except ValueError:
        return False

def esFechaCorrecta(fecha_str):
    while True:
        try:
            datetime.strptime(fecha_str, '%d/%m/%Y')
            break
        except:
            return False
    return True

def guardar_en_archivo(mes,dic_datos):

    fieldnames = ['identificador','fecha','concepto', 'detalle', 'tipo', 'valor']
    ruta = 'presupuesto/'
    nombre_archivo = mes+'.csv'
    ruta_nombre_archivo = ruta + nombre_archivo

    with open(ruta_nombre_archivo, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerow(dic_datos)

def guardar_en_archivo(mes, identificador, fecha, concepto, detalle, tipo, valor):

    ruta = 'presupuesto/'
    nombre_archivo = mes+'.csv'
    ruta_nombre_archivo = ruta + nombre_archivo

    with open(ruta_nombre_archivo, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([identificador, fecha, concepto, detalle, tipo, valor])

    actualizar_valor_identificador(identificador)

def siguiente_valor_identificador():
    f = open("secuencia.txt", "r")
    valor_secuencia = f.read()
    return int(str(valor_secuencia))

def actualizar_valor_identificador(valor_actual):
    f = open("secuencia.txt", "w")
    f.write(str(valor_actual))
    f.close()

def llenar_diccionario_presupuesto():
    listado_meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    presupuesto_dic = {}
    for mes in listado_meses:
        movimientos = {}
        nombre_archivo_a_cargar = "presupuesto/"+mes+".csv"
        with open(nombre_archivo_a_cargar, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                movimientos[row[0]] = [row[1],row[2],row[3],row[4],row[5]]
                presupuesto_dic[mes]=movimientos
    return presupuesto_dic

def liquidar_mes (ventana_padre, movimientos_mes):
    total_ingresos = 0
    total_gastos = 0
    for dato in movimientos_mes:
        fila = movimientos_mes[dato]
        if (fila[3] == "Gasto"):
            total_gastos = total_gastos + int(fila[4])
        else:
            total_ingresos = total_ingresos + int(fila[4])

    if (total_ingresos > total_gastos):
        mensaje = "Total Ingresos: "+str(total_ingresos) +" "+"Total Gastos:"+ str(total_gastos)+", " \
                  "los ingresos son superiores, por lo tanto quedaron "+str(total_ingresos-total_gastos)
    elif (total_gastos > total_ingresos):
        mensaje = "Total Ingresos: " + str(total_ingresos) + " " + "Total Gastos:" + str(total_gastos) + ", " \
                  "los gastos son superiores, por lo tanto faltaron " + str(total_gastos - total_ingresos)
    else:
        mensaje = "Total Ingresos: " + str(total_ingresos) + " " + "Total Gastos:" + str(total_gastos) + ", " \
                  "los gastos y los ingresos fueron los mismos"

    Modal.ventana_mensaje(mensaje, ventana_padre, 2)