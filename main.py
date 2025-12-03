from Funciones import *
from funciones_parcial import *

datos_cargados = False
dato_promedio = False
matriz = []
lista_nom = []
genero = []
legajos = []
estados = []

while True:
    print("")
    print(" - - - - - Inicio de Menú de opciones - - - - - - \n")
    print("1. Cargar datos")
    print("2. Mostrar datos")
    print("3. Promediar notas")
    print("4. Ordenar promedio DESC o ASC")
    print("5. Mostrar materia de mayor promedio")
    print("6. Buscar estudiante con su legajo")
    print("7. Repeticion de nota de una materia")
    print("8. Salir\n")
    print("-"*50)
    opcion = str(num_entero_pos(input("Elija una opción (1-8): ")))
    print("")

    match opcion:
        case "1":
            num_estudiante = num_entero_pos(input("Ingrese cantidad de estudiante: "))

            num_materia = num_entero_pos(input("ingrese cantidad de materias: "))

            cargar_datos_por_uno(num_estudiante,num_materia,lista_nom,genero,legajos,matriz,estados)
            # dato_harco(lista_nom,genero,legajos,estados,matriz)
            # num_estudiante = 4
            # num_materia = 3
            estudiantes = recorrido(matriz, lista_nom, genero, legajos, estados)

            datos_cargados = True
            print("\n¡Carga completa exitosa!\n")

        case "2":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.\n")
            else:
                
                ver = ver_todos_estudiantes(estudiantes)
        case "3":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.\n")
            else:
                dato_promedio = True
                promedios = promedio(matriz)
                dibujo_prome()
        case "4":
            if dato_promedio == False:
                print("Primero debe cargar los datos en la opción 3 para continuar.\n")
            else:
                datos_asc_des = ordenar_por_promedio(lista_nom,promedios,False)
        case "5":
            if dato_promedio == False:
                print("Primero debe cargar los datos en la opción 3 para continuar.\n")
            else:
                promedio_materia = mostrar_mayor_promedio_materia(matriz)
        case "6":
            if dato_promedio == False:
                print("Primero debe cargar los datos en la opción 1 y 3 para continuar.\n")
            else:
                legajo = ver_estudiante_legajo(estudiantes,promedios)
        case "7":
            if datos_cargados == False:
                print("Primero debe cargar los datos en la opción 1 para continuar.\n")
            else:
                repeticiones = repeticiones_por_materia(matriz,num_materia)
        case "8":
            print(" ---Saliendo del programa---\n")
            break

        case _:
            print(" Opción inválida, intente nuevamente.\n")

