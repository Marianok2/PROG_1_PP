from PROG_1_PP.Funciones import *
from PROG_1_PP.funciones_parcial import *


datos_cargados = False

while True:
    print("      Inicio de Menú de opciones       \n")
    print("1. Cargar datos")
    print("2. Mostrar datos")
    print("3. Promediar notas")
    print("4. Ordenar promedio DESC o ASC")
    print("5. Mostrar materia de mayor promedio")
    print("6. Buscar estudiante con su legajo")
    print("7. Repeticion de nota de una materia")
    print("8. Salir")

    opcion = input("Elija una opción (1-8): ")

    match opcion:
        case "1":
            num_estudiante = input("Ingrese cantidad de estudiante: ")
            num_estudiante = num_entero_pos(num_estudiante)

            num_materia = input("ingrese cantidad de materias")
            num_materia = num_entero_pos(num_materia)

            matriz = inicializar_matriz(num_estudiante,num_materia)

            estados = paralela_estado(matriz)

            carga_matriz = cargar_matriz_secuencial(matriz, estados)

            lista_nom = paralela_nombre_apellido(carga_matriz)

            genero = paralela_genero(lista_nom)

            legajos = paralela_legajo(lista_nom)

            datos_cargados = True
        case "2":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                estudiantes = recorrido(carga_matriz, lista_nom, genero, legajos, estados)
                ver = ver_estudiante(estudiantes)
        case "3":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                promedios = promedio(carga_matriz)
        case "4":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                datos_asc_des = ordenar_burbuja(promedio,True)
                datos_asc_des = imprimir_matriz(datos_asc_des)
        case "5":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                promedio_materia = promedio_materias(carga_matriz)
                promedio_materia = mostrar_mayor_promedio_materia(carga_matriz)

        case "6":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                legajo = ver_estudiante_legajo(estudiantes)
        case "7":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.")
            else:
                repeticiones = repeticiones_por_materia(carga_matriz)
        case "8":
            print(" ---Saliendo del programa---")
            break

        case _:
            print(" Opción inválida, intente nuevamente.")