#MODULOS
from inscripcion_asignaturas import funciones as fn
from inscripcion_asignaturas import data as d
from inscripcion_asignaturas import utils as ut

def main():
    #MIENTRAS TRUE
    while True:
        #MOSTRAR MENU
        ut.mostrar_menu_principal() #INGRESAR ALUMNO / MENU ASIGNATURAS / ELIMINAR ALUMNO / SALIR
        #RECIBIR OPCIÓN DEL USUARIO
        opcion_principal = input("Ingrese su opción: ")
        #MATCH CON LAS OPCIONES
        match opcion_principal:
        #OPCION 1 - INGRESAR ALUMNO
            case "1":
                #INGRESAR ALUMNOS
                fn.ingresar_alumno(d.lista_alumnos)
                #LIMPIAR PANTALLA
                ut.limpiar_pantalla()
                #VOLVER AL MENU


        #OPCION 2 - MENU ASIGNATURAS
            case "2":
                print("Bienvenido al menú de asignaturas")
                fn.menu_asignaturas(d.lista_alumnos, d.lista_asignaturas)

        #OPCION 3 - ELIMINAR ALUMNO
            case "3":
                fn.eliminar_alumno(d.lista_alumnos)

        #OPCION 4 - SALIR
            case "4":
                #MOSTRAR MENSAJE DE CIERRE
                print("El programa está finalizando...")
                #PAUSAR
                ut.pausar()
                #FINALIZAR PROGRAMA
                break


        #OPCION _ - OPCIÓN ERRONEA
            case _:
                pass
                #MENSAJE DE ERROR
                print("Ingrese una opción válida")
                #PAUSAR
                ut.pausar()
                #LIMPIAR PANTALLA
                ut.limpiar_pantalla()


if __name__ == "__main__":
    main()