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
    rut = rut.replace('.', "").replace('-', "") #PRIMERO QUITAMOS LOS '.' Y LUEGO EL '-'

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


def se_repite(rut, lista):
    pass

def confirmar():
    pass
