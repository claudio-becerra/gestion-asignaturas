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

def es_rut_valido(rut):
    pass

def se_repite(rut, lista):
    pass

def confirmar():
    pass
