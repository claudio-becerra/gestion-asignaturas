import os  #PARA INTERACTUAR CON EL SISTEMA OPERATIVO


def mostrar_menu_principal(): #MOSTRAR MENU
    #INGRESAR ALUMNO / INSCRIBIR ASIGNATURAS / SALIR
    print("""
Bienvenido al sistema de inscrición de asignaturas.
----------------------------------------------------
Opciones:

1 - Ingresar alumno.
2 - Inscribir asignaturas.
3 - Eliminar alumno
4 - Salir
        """)

def pausar():
    input("Presione enter para continuar")

def limpiar_pantalla():
    #PARA WINDOWS
    if os.name == "nt":  #NT ES EL NOMBRE QUE RECIBE WINDOWS (NEW TECHNOLOGY)
        os.system('cls')  #ESCRIBE CLS EN CONSOLA BORRANDO EL CONTENIDO DE ESTA.
    #PARA MAC Y LINUX
    else:  #EN CASO DE NO SER WINDOWS
        os.system('clear')  #ESCRIBE CLEAR EN CONSOLA BORRANDO EL CONTENIDO

def es_rut_valido(rut): #RECIBE UNA CADENA (RUT) Y RETORNA TRUE OR FALSE
    #DAMOS EL FORMATO AL RUT - 12345678K
    rut = formato_rut(rut)

    #SI TIENE UN LARGO MINIMO DE 7 CARACTERES (LO MÁS PEQUEÑO QUE SE PUEDE CONSEGUIR DE UNA PERSONA VIVA EN LA ACTUALIDAD)
    if len(rut) > 7:
        #SEPARAMOS EL CUERPO DEL DÍGITO VERIFICADOR
        cuerpo = rut[0:-1] #SELECCIONAMOS DESDE EL INICIO DE LA CADENA HASTA EL PENÚLTIMO CARACTER
        dv = rut[-1].upper() #SELECCIONAMOS EL ÚLTIMO CARACTER Y EN CASO DE SER K, LO DEJAMOS EN MAYUSCULAS

        #SI EL CUERPO SON SOLO NÚMEROS
        if cuerpo.isdigit():
            #REALIZAMOS LA SUMA DE COMPROBACIÓN
            suma = 0 #ACUMULADOR
            multiplo = 2 #NÚMERO POR EL QUE HAY QUE MULTIPLICAR CADA DÍGITO

            #RECORREMOS EL CUERPO A LA INVERSA
            #PARA CADA CARACTER EN RUT
            for c in reversed(cuerpo):
                #AL CARACTER SE TRABAJA COMO INT Y SE MULTIPLICA POR EL MULTIPLO
                valor = int(c) * multiplo
                #EL RESULTADO SE AGREGA AL ACUMULADOR SUMA
                suma += valor
                multiplo += 1
                #AL LLEGAR A 7 EL MULTIPLO VUELVE A 2
                if multiplo == 8:
                    multiplo = 2
                
            
            #CALCULAMOS EL DV QUE DEBERÍA CORRESPONDER
            resto = suma % 11
            resultado = 11 - resto
            #TRANSFORMAMOS A FORMATO DV
            #SI EL RESULTADO == 11
            if resultado == 11:
                #DV = 0
                dv_esperado = "0"
            #SI EL RESULTADO == 10
            elif resultado == 10:
                #DV = K
                dv_esperado = "K"
            #SI ES CUALQUIER OTRO NUMERO
            else:
                #DV = RESULTADO
                dv_esperado = str(resultado)

            #COMPARAMOS EL DV GENERADO Y EL DV INGRESADO
            #SI COINCIDEN
            if dv_esperado == dv:
                return True
            #SI NO COINCIDEN
            else:
                return False

        #SI EL CUERPO NO SON SOLO NUMEROS
        else:
            return False

    #SI NO TIENE EL MÍNIMO NECESARIO
    else:
        return False

def formato_rut(rut):
    rut = rut.replace('.', "").replace('-', "") #PRIMERO QUITAMOS LOS '.' Y LUEGO EL '-'
    return rut

def se_encuentra_en_lista(rut, lista): #RECIBE EL RUT Y LA LISTA DE ALUMNOS 
    #RECORREMOS LA LISTA
    #PARA CADA ALUMNO EN LA LISTA
    for alumno in lista:
        #SI RUT == ALUMNO["RUT"] - SI ALGUN ALUMNO TIENE EL MISMO RUT QUE SE INGRESÓ
        if rut == alumno["rut"]:
            return True
    #SI TERMINA LA LISTA SIN ENCONTRAR UNA COINCIDENCIA
    return False

def buscar_index(codigo, lista):
    i = 0
    for asignatura in lista:
        if codigo == asignatura["codigo"]:
            return i
        else:
            i += 1

def buscar_index_alumno(alumnos, rut):
    i = 0
    for alumno in alumnos:
        if rut == alumno["rut"]:
            return i
        else:
            i += 1

def confirmar():
    while True: 
        respuesta = input("¿Confirma su selección? S/N: ").upper()
        if respuesta == "S": #SI CONFIRMA
            return True #RETORNA TRUE
        elif respuesta == "N": #SI NO CONFIRMA
            return False #RETORNA FALSE
        else: #EN CASO DE OBTENER OTRA RESPUESTA
            #MENSAJE DE ERROR AL USUARIO
            print("Escriba S para confirmar, N para cancelar")  
            #VOLVEMOS AL CICLO DE LA OPCIÓN
        
def es_vacio(entrada): #RECIBE UN RUT Y RETORNA TRUE OR FALSE
        if entrada == "": #SI DEJA EL CAMPO VACIO, CANCELAR OPERACION
            return True 
        else: #SI NO ESTÁ VACÍO
            return False 


def mostrar_menu_inscripcion(): 
    print("""
Bienvenido al menú de inscrición de asignaturas.
----------------------------------------------------
Opciones:

1 - Inscribir asignatura.
2 - Eliminar asignatura.
3 - Volver al menú principal
        """)

def mostrar_asignaturas(nivel_alumno, asignaturas): #RECIBE EL NIVEL Y LA LISTA DE ASIGNATURAS
    #MOSTRAR ASIGNATURAS DE UN NIVEL ANTERIOR QUE NO APAREZCA EN LISTA ASIGNATURAS COMPLETADAS
    #CODIGO - NOMBRE - NIVEL
    print("Asignaturas a inscribir")
    for codigo, asignatura in asignaturas.items():
        if int(nivel_alumno) >= int(asignatura["nivel"]):
            print(f"{codigo} : {asignatura["nombre"]}")

def se_encuentra_asignatura(codigo_ingresado, asignaturas, nivel_alumno): #RECIBE EL CODIGO DE ASIGNATURA. LISTA ASIGNATURAS Y RETORNA TRUE O FALSE
    for codigo, asignatura in asignaturas.items():
        if int(nivel_alumno) >= int(asignatura["nivel"]): 
            #SI SE ENCUENTRA LA ASIGNATURA
            if codigo_ingresado.upper() == codigo:
                return True
        #SI NO SE ENCUENTRA
        else:
            return False

def buscar_alumno(rut_alumno, lista_alumnos): #RECIBE EL RUT DEL ALUMNO, LA LISTA DE ALUMNOS Y DICCIONARIO ALUMNO
    for alumno in lista_alumnos:
        if alumno["rut"] == rut_alumno:
            return alumno

def se_encuentra_inscrita(codigo, asignaturas_inscritas): #RECIBE EL CODIGO, LA LISTA DE ASIGNATURAS Y RETORNA TRUE OR FALSE
    for asignatura in asignaturas_inscritas:
        if codigo == asignatura["codigo"]:
            return True
    return False


def mostrar_asignaturas_inscritas(alumno): #RECIBE AL ALUMNO E IMPRIME LA LISTA DE SUS ASIGNATURAS
    #MENSAJE INDICANDO QUE SE MOSTRARÁN SUS ASIGNATURAS INSCRITAS
    print("Estas son las asignaturas inscritas del alumno")
    #alumno["asignaturas_inscritas"] - LISTA DE ASIGNATURAS INSCRITAS
    for asignatura in alumno["asignaturas_inscritas"]:
        #MOSTRAR ASIGNATURA
        print(f"{asignatura["codigo"]} : {asignatura["nombre"]}")