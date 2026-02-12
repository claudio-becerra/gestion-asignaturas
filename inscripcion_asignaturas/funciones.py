from inscripcion_asignaturas import utils as ut

def ingresar_alumno(alumnos_inscritos): #RECIBE LA LISTA DE ALUMNOS, RETORNE UN DICCIONARIO DEL ALUMNO NUEVO
    print("Ingrese los datos del alumno a ingresar")
    nuevo_alumno ={} #INICIALIZAMOS EL OBJETO QUE UTILIZAREMOS
    nuevo_alumno["nombre"] = input("Ingrese nombre del alumno: ").upper() #GUARDAMOS EL NOMBRE EN MAYUSCULAS PARA FORMATO
    #INGRESAR RUT
    while True: #QUE INGRESE RUT HASTA QUE SALGAMOS DEL CICLO
        print("En caso de querer cancelar la operación, presionar enter sin ingresar datos")
        rut =input("Ingrese el rut del alumno: ")
        #SI DEJÓ EL INPUT VACIO
        if rut == "": #SI DEJA EL CAMPO VACIO, CANCELAR OPERACION
            #MOSTRAR MENSAJE A USUARIO DE CANCELACIÓN
            print("El proceso ha sido cancelado\n Volviendo al menu")
            return
        #validamos rut
        if ut.es_rut_valido(rut): #SI SE INGRESA UN RUT VALIDO
            if not ut.se_repite(rut, alumnos_inscritos): #SI NO SE REPITE EN LA LISTA
                nuevo_alumno["rut"] = rut
                break

            else: #SI SE REPITE
                #MENSAJE AL USUARIO - EL RUT INGRESADO YA SE ENCUENTRA INSCRITO
                print("El rut que ha ingresado ya se encuentra inscrito")
                break
        else: #SI EL RUT NO ES VALIDO
            #MENSAJE AL USUARIO - EL RUT ES INVALIDO
            print("El rut ingresado no es válido")
            #VOLVEMOS A INGRESAR RUT
            continue

    nuevo_alumno["nivel"] = 1 #AL SER NUEVO ALUMNO, EL NIVEL BASE ES 1
    nuevo_alumno["asignaturas-inscritas"] =[]

    #GUARDAR ALUMNO EN LA LISTA
    alumnos_inscritos.append()
    #MENSAJE AL USUARIO - ALUMNO INSCRITO
    print("El alumno fue inscrito de forma exitosa")
    print(f"Nombre: {nuevo_alumno["nombre"]} - rut: {nuevo_alumno["rut"]}")


