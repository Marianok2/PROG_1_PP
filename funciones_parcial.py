import sys
sys.path.append(r"C:\Users\yasuo\OneDrive\Escritorio\Python\PYTHON")

from PROG_1_PP.Funciones import *


# 1) Una matriz de numeros enteros de 30 filas(los alumnos) x 5 columnas (materias) y la interseccion es una calificacion entera entre 1 y 10.
num_estudiante = 2
num_materia = 3

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any = 0)->list:
    matriz = []
    for i in range (cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz

def paralela_estado(mi_matriz: list)->list:
    lista_paralela = []

    for i in range(len(mi_matriz)):
        lista_paralela += [0]

    return lista_paralela

# 5)Una lista de estados 0(libre) y 1 (cupado)

matriz = inicializar_matriz(num_estudiante,num_materia)
estados = paralela_estado(matriz)

def cargar_matriz_secuencial(mi_matriz: list,estados)->list:
    
    for i in range(len (mi_matriz)):
        if estados[i] == 1:
            print(f"El estudiante N°{i+1} esta ocupado, Saltado al proximo")
            continue
        for j in range (len(mi_matriz[i])):
            validacion = input(f"Ingrese nota para el estudiante N°{i+1} de la materia °{j+1}: ")
            validacion = calificaciones(validacion)
            mi_matriz[i][j] = validacion
        estados[i] = 1   
    
    return mi_matriz

carga_matriz = cargar_matriz_secuencial(matriz, estados)

# for i in range(len(estados)):
#     print(estados[i])


# print(carga_matriz)

# 2) Una lista de apellido y nombre de los estudiantes
def paralela_nombre_apellido(mi_matriz: list)->list:
    lista_paralela = []

    for i in range(len(mi_matriz)):
        validacion = input(f"Ingrese Nombre y Apellido del estudiante n°{i+1}: ")
        validacion = nombre_apellido(validacion)
        lista_paralela += [validacion]

    return lista_paralela


lista_nom = paralela_nombre_apellido(carga_matriz)
# for l in range (len(lista_nom)):
#     print(lista_nom[l])


# for i in range (len(carga_matriz)):
#     for j in range (len(carga_matriz[i])):
#         print(carga_matriz[i][j], end = "") 
#     print()

# 3)Una lista de genero entre F,M,X

def paralela_genero(nombres: list)->list:
    lista_paralela = []
    
    for i in range(len(nombres)):
        validacion = input(f"Ingrese Genero de {nombres[i]} 'F', 'M', 'X':  ")
        validacion = validacion_genero(validacion)
        lista_paralela += [validacion]

    return lista_paralela

genero = paralela_genero(lista_nom)
#for l in range (len(genero)):
    # print(genero[l])

# 4)Una lista de legajos de los estudiantes de 6 cifras

def paralela_legajo(nombres: list)->list:
    lista_paralela = []
    
    for i in range(len(nombres)):
        validacion = input(f"Ingrese numero de lejado de {nombres[i]} de 6 cifras:  ")
        validacion = validacion_legajo(validacion)
        lista_paralela += [validacion]

    return lista_paralela

legajo = paralela_legajo(lista_nom)

def recorrido(matriz: list, nombre: list, genero: list, legajo: list, estados : list):
    lista_estudiante = []
    
    for i in range(len (matriz)):
        if estados[i] == 1:
            fila = [nombre[i], genero[i],legajo[i]]
            for j in range (len(matriz[i])):
                fila += [matriz[i][j]]

            lista_estudiante += [fila]
        else:
            estados
    return lista_estudiante    

estudiantes = recorrido(carga_matriz, lista_nom, genero, legajo, estados)

def ver_estudiante(lista_estudiantes: list):
    while True:
        buscar = input("Ingrese el nombre del estudiante que desea ver: ")
        buscar = nombre_apellido(buscar)

        encontrado = False
        
        for i in lista_estudiantes:
            if buscar == i[0]:
                print(f"Datos del estudiante {i[0]}, Genero {i[1]}, numero de legajo {i[2]}, Sus Notas son: ")
                
                for j in range(3, len(i)):
                    print(f" {i[j]}")
                encontrado = True
                break

        if encontrado == True:
            break
        else:
            print(" Estudiante no encontrado. Intente nuevamente.\n")

ver = ver_estudiante(estudiantes)

def promedio(matriz: list):
    promedios = []  

    for i in matriz:
        suma = 0
        for nota in i:
            suma += nota
        prom = suma / len(i)
        promedios += [prom]   

    return promedios

def ordenar_burbuja_list(lista: list, orden: bool = True) -> list:
    """
    La función ordena una lista.
    Args: Variable lista.
    Return: lista. ordenada.
    """
    n = len(lista) 
    for i in range(n):
        for j in range(0,n - i -1):
            if orden == True:
                if lista[j] > lista[j + 1]: 
                    aux = lista[j] 
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
            else:
                 if lista[j] < lista[j + 1]: 
                    aux = lista[j] 
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
    return lista
    

def ordenar_burbuja(matriz: list,orden: bool = True) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
         matriz[i] = ordenar_burbuja_list(matriz[i], orden)
    

    return matriz
    
    
def imprimir_lista(lista):
     for i in range(len(lista)):
 	    print(lista[i] , end = " ")
         

def imprimir_matriz(matriz:list)->list:
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(matriz[i][j], end = "")
        print()    

def promedio_materias(matriz: list) -> list:
    filas = len(matriz)
    columnas = len(matriz[0])
    promedios = []

    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += matriz[i][j]
        prom = suma / filas
        promedios += [prom]

    return promedios

def mostrar_mayor_promedio_materia(matriz: list):

    promedios = promedio_materias(matriz)
    columnas = len(matriz[0])
    
    max_prom = promedios[0]
    for prom in promedios:
            if prom > max_prom:
                max_prom = prom

    for j in range(columnas):
        if promedios[j] == max_prom:
            print("La MATERIA_" + str(j + 1)," Promedio:",promedios[j])

def promedio(matriz: list):
    promedios = []  

    for i in matriz:
        suma = 0
        for nota in i:
            suma += nota
        prom = suma / len(i)
        promedios += [prom]   

    return promedios

def ver_estudiante_legajo(lista_estudiantes: list):
    while True:
        buscar = input("Ingrese el numero de legajo del estudiante que desea ver: ")
        buscar = validacion_legajo(buscar)

        encontrado = False
        
        for i in lista_estudiantes:
            if buscar == i[2]:
                print(f"Datos del estudiante {i[0]}, Genero {i[1]}, numero de legajo {i[2]}, Sus Notas promedia:")
                
                notas = []
                for j in range(3, len(i)):
                    notas += [i[j]]

                prom = promedio([notas])
                print("Promedio:", prom[0])

                for j in range(3, len(i)):
                    print(f" {i[j]}")
                encontrado = True
                break

        if encontrado == True:
            break
        else:
            print(" Estudiante no encontrado. Intente nuevamente.\n")

def repeticiones_por_materia(matriz: list):
    materia = input("Ingrese numero de materia (1-5): ")
    materia = materia_validacion(materia)
    
    col = materia - 1
    
    conteo = [0] * 10

    for fila in matriz:
        nota = fila[col] 
        if 1 <= nota <= 10:
            conteo[nota - 1] += 1  

    return conteo

