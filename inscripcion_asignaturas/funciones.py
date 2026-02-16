from inscripcion_asignaturas import utils as ut

alumno_actual = {}

def ingresar_alumno(alumnos_inscritos): #RECIBE LA LISTA DE ALUMNOS, RETORNE UN DICCIONARIO DEL ALUMNO NUEVO
    print("Ingrese los datos del alumno a ingresar")
    nuevo_alumno ={} #INICIALIZAMOS EL OBJETO QUE UTILIZAREMOS
    while True: #MIENTRAS NO ESTÉ UN NOMBRE VÁLIDO
        nuevo_alumno["nombre"] = input("Ingrese nombre completo del alumno: ").upper() #GUARDAMOS EL NOMBRE EN MAYUSCULAS PARA FORMATO
        if nuevo_alumno["nombre"] == "": #SI EL NOMBRE ESTÁ VACIÓ
            #MENSAJE PARA EL USUARIO - DEBE INGRESAR UN NOMBRE
            print("Debe ingresar el nombre del alumno")
            #PAUSAR
            ut.pausar()
        else: #SI EL NOMBRE NO ESTÁ VACÍO, CONTINUAR CON LOS DEMÁS DATOS
            break
    #INGRESAR RUT
    while True: #QUE INGRESE RUT HASTA QUE SALGAMOS DEL CICLO
        print("Ingrese el rut del alumno: ")
        print("En caso de querer cancelar la operación, presionar enter sin ingresar datos")
        rut =input("Ingrese el rut del alumno: ")
        #SI DEJÓ EL INPUT VACIO
        if ut.es_vacio(rut): #SI DEJA EL CAMPO VACIO, CANCELAR OPERACION
            #MOSTRAR MENSAJE A USUARIO DE CANCELACIÓN
            print("El proceso ha sido cancelado\n Volviendo al menu")
            ut.pausar()
            return
        #validamos rut
        if ut.es_rut_valido(rut): #SI SE INGRESA UN RUT VALIDO
            if not ut.se_encuentra_en_lista(ut.formato_rut(rut), alumnos_inscritos): #SI NO SE REPITE EN LA LISTA

                nuevo_alumno["rut"] = ut.formato_rut(rut)
                break

            else: #SI SE REPITE
                #MENSAJE AL USUARIO - EL RUT INGRESADO YA SE ENCUENTRA INSCRITO
                print("El rut que ha ingresado ya se encuentra inscrito")
                ut.pausar()
                continue

        else: #SI EL RUT NO ES VALIDO
            #MENSAJE AL USUARIO - EL RUT ES INVALIDO
            print("El rut ingresado no es válido")
            print("Volviendo a ingresar el rut...")
            #PAUSAR
            ut.pausar()
            #LIMPIAR PANTALLA
            ut.limpiar_pantalla()
            #VOLVEMOS A INGRESAR RUT
            continue
    
    nuevo_alumno["nivel"] = 1 #AL SER NUEVO ALUMNO, EL NIVEL BASE ES 1
    nuevo_alumno["asignaturas_inscritas"] =[]

    #GUARDAR ALUMNO EN LA LISTA
    alumnos_inscritos.append(nuevo_alumno)
    #MENSAJE AL USUARIO - ALUMNO INSCRITO
    print("El alumno fue inscrito de forma exitosa")
    print(f"Nombre: {nuevo_alumno['nombre']} - rut: {nuevo_alumno['rut']}")
    ut.pausar()

def inscribir_asignatura(lista_asignaturas, alumno_actual):
    while True:
        #MOSTRAR LISTA ASIGNATURAS DEL NIVEL DEL ALUMNO
        ut.mostrar_asignaturas(alumno_actual["nivel"], lista_asignaturas) #MUESTRA LA LISTA DE ASIGNATURAS DEPENDIENDO DEL NIVEL
        #MENSAJE DEL USUARIO PARA QUE INGRESE EL CODIGO DE LA ASIGNATURA
        codigo_inscripcion = input("Ingrese el código de la asignatura a inscribir: ").upper()
        #SI NO SE INGRESA NADA, SE SALE DEL LA OPCIÓN
        if ut.es_vacio(codigo_inscripcion):
            print("Se ha cancelado la opción")
            ut.pausar()
            break
        

        #VALIDAR QUE SEA UNA DE LAS ASIGNATURAS MOSTRADAS
        #SI SE ENCUENTRA EN LAS ASIGNATURAS MOSTRADAS EN EL MENU
        if ut.se_encuentra_asignatura(codigo_inscripcion, lista_asignaturas, alumno_actual["nivel"] ):

            #SI LA ASIGNATURA NO SE ENCUENTRA EN SUS ASIGNATURAS INSCRITAS
            if not ut.se_encuentra_inscrita(codigo_inscripcion, alumno_actual["asignaturas_inscritas"]):

                #SI TIENE MENOS DE 6 ASIGNATURAS INSCRITAS
                if len(alumno_actual["asignaturas_inscritas"]) < 6:
                    #PEDIR CONFIRMACIÓN AL USUARIO S/N
                    #SI CONFIRMA SU SELECCIÓN
                    if ut.confirmar():
                        #DATOS DE LA ASIGNATURA
                        asignatura = lista_asignaturas[codigo_inscripcion]
                        #AGREGAMOS LA ASIGNATURA A LAS ASIGNATURAS INSCRITAS
                        nueva_inscripcion ={"codigo" : codigo_inscripcion,
                                            "nombre" : asignatura["nombre"],
                                            "nivel" : asignatura["nivel"]}
                        alumno_actual["asignaturas_inscritas"].append(nueva_inscripcion)
                        #MENSAJE DE EXITO - ASIGNATURA INSCRITA
                        print(f"Se ha inscrito la asignatura {nueva_inscripcion["codigo"]} : {nueva_inscripcion["nombre"]} ")
                        #PAUSAR
                        ut.pausar()
                        #LIMPIAR PANTALLA
                        ut.limpiar_pantalla()
                        continue #VOLVEMOS A INSCRIBIR OTRA ASIGNATURA

                    #SI NO LA CONFIRMA
                    else:
                        #MENSAJE DE ERROR - NO SE HA INCRITO LA ASIGNATURA
                        print("La asignatura no se ha inscrito")
                        #PAUSAR
                        ut.pausar()
                        continue #VOLVEMOS A INSCRIBIR ASIGNATURA




                #SI NO TIENE MENOS DE 6 ASIGNATURAS INSCRITAS
                else:
                    #MENSAJE ERROR - TOPE DE ASIGNATURAS ALCANZADO
                    print("Has superado el límite de asignaturas por inscribir")
                    ut.pausar()
                    ut.limpiar_pantalla()

            #SI SE ENCUENTRA EN LA LISTA DE ASIGNATURAS INSCRITAS
            else:
                #MENSAJE ERROR - ASIGNATURA YA SE ENCUENTRA INSCRITA
                print("La asignatura seleccionada ya se encuentra inscrita")
                ut.pausar()
                ut.limpiar_pantalla()
        
        #SI NO SE ENCUENTRA ENTRE LAS ASIGNATURAS
        else:
            #MENSAJE ERROR - NO SE ENCUENTRAN LA ASIGNATURA
            print("La asignatura ingresada no existe, intente de nuevo")
            ut.pausar()
            ut.limpiar_pantalla()

def eliminar_asignatura(alumno_actual):
    #SI HAY ASIGNATURAS INSCRITAS - NO ESTÁ VACIO
    if alumno_actual["asignaturas_inscritas"] != []:
        #MIENTRAS TRUE
        while True:
            #MOSTRAS LISTA DE ASIGNATURAS INSCRITAS
            ut.mostrar_asignaturas_inscritas(alumno_actual)
            #MENSAJE AL USUARIO PARA QUE INGRESE EL CODIGO DE LA ASIGNATURA A ELIMINAR
            print("Si desea salir del menu, solo presione enter")
            asignatura = input("\nIngrese el código de la asignatura a eliminar: ").upper()

            #SI EL CAMPO ESTA VACIO, SALIR DEL MENU
            if ut.es_vacio(asignatura):
                print("Volviendo al menu")
                ut.pausar()
                ut.limpiar_pantalla()
                break
            #SI LA ASIGNATURA SE ENCUENTRA INSCRITA
            if ut.se_encuentra_inscrita(asignatura, alumno_actual["asignaturas_inscritas"]):
                #Buscar index de la asignatura en la lista
                index_eliminar = ut.buscar_index(asignatura, alumno_actual["asignaturas_inscritas"])

                #ELIMINAR ASIGNATURA DE ASIGNATURAS INSCRITAS
                alumno_actual["asignaturas_inscritas"].pop(index_eliminar)
                #MENSAJE AL USUARIO ASIGNATURA ELIMINADA
                print("La asignatura ha sido eliminada")
                #PAUSAR
                ut.pausar()
                #LIMPIAR PANTALLA
                ut.limpiar_pantalla()
                #VOLVER A ELIMINAR ASIGNATURAS
                break
            #SI NO SE ENCUENTRA INSCRITA
            else:
                print("La asignatura no se encuentra inscrita, favor intentarlo de nuevo")

    #SI NO HAY ASIGNATURAS INSCRITAS
    else:
        #MENSAJE AL USUARIO NO HAY ASIGNATURAS INSCRITAS
        print("El alumno no posee asignaturas inscritas")
        #PAUSAR
        ut.pausar()
        #LIMPIAR PANTALLA
        ut.limpiar_pantalla()
        #VOLVER A MENU DE INSCRIPCION

def eliminar_alumno(alumnos):
    #SI HAY ALUMNOS INSCRITOS
    if alumnos != []:
        #PEDIR RUT DEL ALUMNO
        while True: #QUE INGRESE RUT HASTA QUE SALGAMOS DEL CICLO
            print("En caso de querer cancelar la operación, presionar enter sin ingresar datos")
            rut =input("Ingrese el rut del alumno: ")
            #SI DEJÓ EL INPUT VACIO
            if ut.es_vacio(rut): #SI DEJA EL CAMPO VACIO, CANCELAR OPERACION
                #MOSTRAR MENSAJE A USUARIO DE CANCELACIÓN
                print("El proceso ha sido cancelado\n Volviendo al menu")
                ut.pausar()
                return
            #validamos rut
            if ut.es_rut_valido(rut): #SI SE INGRESA UN RUT VALIDO
                rut = ut.formato_rut(rut)
                #VER SI SE ENCUENTRA EN LA LISTA DE ALUMNOS
                if ut.se_encuentra_en_lista(rut, alumnos):
                    rut_alumno_actual = ut.formato_rut(rut)
                    alumno_actual = ut.buscar_alumno(rut_alumno_actual, alumnos)

                    #CONFIRMAR SI SE QUIERE ELIMINAR
                    print(f"Se va a eliminar el alumno {alumno_actual["nombre"]}")
                    #SI SE QUIERE ELIMINAR
                    if ut.confirmar():
                        index_eliminar = ut.buscar_index_alumno(alumnos, rut)
                        #SE ELIMINA EL ALUMNO DE LA LISTA
                        alumnos.pop(index_eliminar)
                        #MENSAJE AL USUARIO - ALUMNO ELIMINADO
                        print("El alumno ha sido eliminado")
                        ut.pausar()
                        break
                    #SI NO SE QUIERE ELIMINAR
                    else:
                        #MENSAJE AL USUARIO - EL ALUMNO NO SE ELIMINÓ
                        print("El alumno NO fue eliminado")
                        #PAUSAR
                        ut.pausar()
                        break


                else: #SI NO SE ENCUENTRA EN LA LISTA DE ALUMNOS INSCRITOS
                    #MENSAJE ERROR AL USUARIO - ALUMNO NO INSCRITO
                    print("El rut ingresado no está inscrito")
                    print("Volviendo a ingresar el rut...")
                    #PAUSAR
                    ut.pausar()
                    
            else: #SI EL RUT NO ES VALIDO
                #MENSAJE AL USUARIO - EL RUT ES INVALIDO
                print("El rut ingresado no es válido")
                print("Volviendo a ingresar el rut...")
                #PAUSAR
                ut.pausar()
                #LIMPIAR PANTALLA
                ut.limpiar_pantalla()

    #SI NO HAY ALUMNOS INSCRITOS
    else:
        #MENSAJE AL USUARIO - NO HAY ALUMNOS INSCRITOS
        print("No hay alumnos inscritos")
        #PAUSAR
        ut.pausar()

def menu_asignaturas(alumnos_inscritos, lista_asignaturas):
    #INGRESAR RUT
    while True: #QUE INGRESE RUT HASTA QUE SALGAMOS DEL CICLO
        print("En caso de querer cancelar la operación, presionar enter sin ingresar datos")
        rut =input("Ingrese el rut del alumno: ")
        #SI DEJÓ EL INPUT VACIO
        if ut.es_vacio(rut): #SI DEJA EL CAMPO VACIO, CANCELAR OPERACION
            #MOSTRAR MENSAJE A USUARIO DE CANCELACIÓN
            print("El proceso ha sido cancelado\n Volviendo al menu")
            ut.pausar()
            return
        #validamos rut
        if ut.es_rut_valido(rut): #SI SE INGRESA UN RUT VALIDO
            rut = ut.formato_rut(rut)
            #VER SI SE ENCUENTRA EN LA LISTA DE ALUMNOS
            if ut.se_encuentra_en_lista(rut, alumnos_inscritos):
                rut_alumno_actual = rut
                alumno_actual = ut.buscar_alumno(rut_alumno_actual, alumnos_inscritos)

                while True: #MOSTRAMOS EL MENU DE INSCRIPCION
                    #INSCRIBIR ASIGNATURA- ELIMINAR ASIGNATURA - VOLVER A MENU PRINCIPAL
                    ut.mostrar_menu_inscripcion()

                    #MATCH CON LAS OPCIONES
                    opcion = input("Ingrese la opción que necesite: ")
                    match opcion:
                        #OPCION 1 - INSCRIBIR ASIGNATURA
                        case "1":
                            inscribir_asignatura(lista_asignaturas, alumno_actual)

                    #OPCION 2 - ELIMINAR ASIGNATURA
                        case "2":
                            eliminar_asignatura(alumno_actual)

                    #OPCION 3 - VOLVER AL MENU PRINCIPAL
                        case "3":
                        #VOLVER AL MENU PRINCIPAL
                            break

                    #OPCION _ - ERROR
                        case _:
                            #MENSAJE DE ERROR
                            print("Debe ingresar una opción válida")
                            #PAUSAR
                            ut.pausar()
                            #LIMPIAR PANTALLA
                            ut.limpiar_pantalla()
                break #VOLVEMOS AL MENU PINCIPAL
            else: #SI NO SE ENCUENTRA EN LA LISTA DE ALUMNOS INSCRITOS
                #MENSAJE ERROR AL USUARIO - ALUMNO NO INSCRITO
                print("El rut ingresado no está inscrito")
                print("Volviendo a ingresar el rut...")
                #PAUSAR
                ut.pausar()
                
        else: #SI EL RUT NO ES VALIDO
            #MENSAJE AL USUARIO - EL RUT ES INVALIDO
            print("El rut ingresado no es válido")
            print("Volviendo a ingresar el rut...")
            #PAUSAR
            ut.pausar()
            #LIMPIAR PANTALLA
            ut.limpiar_pantalla()


