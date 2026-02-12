
def main():
    #MIENTRAS TRUE
        #MOSTRAR MENU
            #INGRESAR ALUMNO / INSCRIBIR ASIGNATURAS / SALIR
        
        #RECIBIR OPCIÓN DEL USUARIO
        #MATCH CON LAS OPCIONES

        #OPCION 1 - 
            #INGRESAR ALUMNOS

            #INGRESAR DATOS DEL ALUMNO
            #NOMBRE - APELLIDO
            #RUT
                #VALIDAR QUE EL RUT EXISTA
                #VALIDAR QUE EL RUT NO SE REPITA EN LA LISTA DE ALUMNOS
            #AL SER NUEVO ALUMNO, ENTRA EN NIVEL 1 SIN ASIGNATURAS COMPLETADAS NI ASIGNATURAS INSCRITAS
            
            #GUARDAR ALUMNO EN LA LISTA
            #MOSTRAR MENSAJE DE EXITO
            #LIMPIAR PANTALLA
            #VOLVER AL MENU


        #OPCION 2 -
            #INSCRIBIR ASIGNATURAS

            #RECIBE EL RUT DEL ALUMNO INGRESADO POR EL USUARIO
                #VALIDA QUE EL RUT EXISTA
                #VERIFICA QUE EL RUT SE ENCUENTRE EN LA LISTA DE ALUMNOS
                    #SI EXISTE
                        #OBTENEMOS EL USUARIO
                        #MOSTRAR MENU INSCRIPCION
                            #INSCRIBIR ASIGNATURA- ELIMINAR ASIGNATURA - VOLVER A MENU PRINCIPAL

                            #MATCH CON LAS OPCIONES

                            #OPCION 1 -
                                #INSCRIBIR ASIGNATURAS
                                
                                #MIENTRAS TRUE 
                                    #MOSTRAR LISTA ASIGNATURAS DEL NIVEL DEL ALUMNO
                                    #MOSTRAR ASIGNATURAS DE UN NIVEL ANTERIOR QUE NO APAREZCA EN LISTA ASIGNATURAS COMPLETADAS
                                        #CODIGO - NOMBRE - NIVEL
                                    #MENSAJE DEL USUARIO PARA QUE INGRESE EL CODIGO DE LA ASIGNATURA
                                    #RECIBIR NUMERO DE LA ASIGNATURA A INSCRIBIR
                                        #VALIDAR QUE SEA UNA DE LAS ASIGNATURAS MOSTRADAS
                                        #VALIDAR QUE NO TENGA MÁS DE 6 ASIGNATURAS INSCRITAS

                                        #PEDIR CONFIRMACIÓN AL USUARIO S/N
                                            #SI CONFIRMA S-
                                                #AGREGAR ASIGNATURA A ASIGNATURAS INSCRITAS
                                                #MENSAJE DE ASIGNATURA INSCRITA
                                                #PAUSAR
                                                #LIMPIAR PANTALLA
                                                #VOLVER A LA SELECCION DE ASIGNATURAS


                                            #SI NO CONFIRMA N-
                                                #MENSAJE AL USUARIO NO SE HA INSCRITO LA ASIGNATURA
                                                #PAUSAR
                                                #VOLVER A LA SELECCION DE ASIGNATURAS


                            #OPCION 2 -
                                #ELIMINAR ASIGNATURA

                                #SI HAY ASIGNATURAS INSCRITAS
                                    #MIENTRAS TRUE
                                        #MOSTRAS LISTA DE ASIGNATURAS INSCRITAS
                                            #CODIGO - NOMBRE - NIVEL
                                        #MENSAJE AL USUARIO PARA QUE INGRESE EL CODIGO DE LA ASIGNATURA A ELIMINAR
                                        #RECIBIR NUMERO DE LA ASIGNATURA A ELIMINAR
                                            #VALIDAR QUE SEA UNA DE LAS ASIGNATURAS MOSTRADAS (INSCRITAS)
                                            #ELIMINAR ASIGNATURA DE ASIGNATURAS INSCRITAS
                                            #MENSAJE AL USUARIO ASIGNATURA ELIMINADA
                                            #PAUSAR
                                            #LIMPIAR PANTALLA
                                            #VOLVER A ELIMINAR ASIGNATURAS (BREAK)
                                

                                #SI NO HAY ASIGNATURAS INSCRITAS
                                    #MENSAJE AL USUARIO NO HAY ASIGNATURAS INSCRITAS
                                    #PAUSAR
                                    #LIMPIAR PANTALLA
                                    #VOLVER A MENU DE INSCRIPCION


                            #OPCION 3 -
                                #VOLVER AL MENU PRINCIPAL

                            #OPCION _ -
                                #MENSAJE DE ERROR
                                #PAUSAR
                                #LIMPIAR PANTALLA

                    #SI NO EXISTE
                        #MENSAJE DE ERROR AL USUARIO
                        #PAUSAR - PRESIONE TECLA ENTER PARA CONTINUAR
                        #LIMPIAMOS PANTALLA
                        #VOLVEMOS A INGRESAR ALUMNO

        #OPCION _ -
            #MENSAJE DE ERROR
            #PAUSAR
            #LIMPIAR PANTALLA
            #VOLVER AL MENU


    pass