
**Proyecto realizado como evaluación del módulo Fundamentos de la programación en Python del bootcamp Desarrollo de aplicaciones FullStack Python**

#  Sistema de Gestión de Asignaturas

Sistema de consola escrito en Python para administrar la inscripción de alumnos y la gestión de cargas académicas. 
Este proyecto permite registrar alumnos, validar sus datos (RUT) y gestionar la inscripción o eliminación de asignaturas.

##  Características

- **Gestión de Alumnos:**
  - Registro de nuevos alumnos con validación de RUT chileno.
  - Validación de duplicados.
  
- **Gestión Académica:**
  - Inscripción de asignaturas validando el nivel del alumno.
  - Eliminación de asignaturas inscritas.
  - Validación de tope máximo de asignaturas (Máximo 6 ramos).
  - Prevención de inscripción de asignaturas duplicadas.

- **Arquitectura Modular:** Código organizado en paquetes para facilitar la escalabilidad.

##  Requisitos Previos

Este proyecto utiliza la estructura `match-case`, por lo que **necesitas Python 3.10 o superior**.


##  Estructura del Proyecto


├── main.py                     # Archivo principal (Menú General)
├── README.md                   
│
└── inscripcion_asignaturas/    # Paquete principal
    ├── data.py                 # "Base de datos" simulada (Listas y Diccionarios)
    ├── funciones.py            # Lógica de ins (Inscribir, Eliminar, Menús)
    └── utils.py                # Herramientas reutilizables (Validar RUT, limpiar pantalla)