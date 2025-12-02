
from Funciones import *

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any = 0) -> list:
    """Crea una matriz con las dimensiones especificadas e inicializada con un valor.
    Args:
        cantidad_filas: Cantidad de filas de la matriz.
        cantidad_columnas: Cantidad de columnas de la matriz.
        valor_inicial: Valor con el que se rellena la matriz (default 0).
    Returns:
        Matriz (lista de listas) inicializada.
    """
    matriz = []
    for i in range (cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz

def paralela_estado(mi_matriz: list) -> list:
    """Crea una lista paralela de estados inicializada en 0.
    Args:
        mi_matriz: La matriz principal de referencia para el tamaño.
    Returns:
        Lista de enteros (ceros) con el mismo largo que la matriz.
    """
    lista_paralela = []

    for i in range(len(mi_matriz)):
        lista_paralela += [0]

    return lista_paralela



def cargar_matriz_secuencial(mi_matriz: list, estados: list) -> list:
    """Carga notas en la matriz de forma secuencial, saltando estudiantes ocupados.
    Args:
        mi_matriz: Matriz de notas a rellenar.
        estados: Lista de estados (1 = ocupado, 0 = libre).
    Returns:
        La matriz de notas actualizada.
    """
    
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


# 2) Una lista de apellido y nombre de los estudiantes
def paralela_nombre_apellido(mi_matriz: list) -> list:
    """Solicita y valida el nombre y apellido para cada fila de la matriz.
    Args:
        mi_matriz: Matriz de referencia para la cantidad de estudiantes.
    Returns:
        Lista con los nombres validados.
    """
    lista_paralela = []

    for i in range(len(mi_matriz)):
        validacion = input(f"Ingrese Nombre y Apellido del estudiante n°{i+1}: ")
        validacion = nombre_apellido(validacion)
        lista_paralela += [validacion]

    return lista_paralela


# 3)Una lista de genero entre F,M,X

def paralela_genero(nombres: list) -> list:
    """Solicita y valida el género (F, M, X) para cada estudiante.
    Args:
        nombres: Lista de nombres de los estudiantes.
    Returns:
        Lista de caracteres representando los géneros.
    """
    lista_paralela = []
    
    for i in range(len(nombres)):
        validacion = input(f"Ingrese Genero de {nombres[i]} 'F', 'M', 'X':  ")
        validacion = validacion_genero(validacion)
        lista_paralela += [validacion]

    return lista_paralela


# 4)Una lista de legajos de los estudiantes de 6 cifras

def paralela_legajo(nombres: list) -> list:
    """Solicita y valida un número de legajo de 6 cifras para cada estudiante.
    Args:
        nombres: Lista de nombres de los estudiantes.
    Returns:
        Lista de enteros con los legajos.
    """
    lista_paralela = []
    
    for i in range(len(nombres)):
        validacion = input(f"Ingrese numero de lejado de {nombres[i]} de 6 cifras:  ")
        validacion = validacion_legajo(validacion)
        lista_paralela += [validacion]

    return lista_paralela



def recorrido(matriz: list, nombre: list, genero: list, legajo: list, estados: list) -> list:
    """Combina las listas paralelas y la matriz en una única estructura de datos.
    Args:
        matriz: Matriz de notas.
        nombre: Lista de nombres.
        genero: Lista de géneros.
        legajo: Lista de legajos.
        estados: Lista de estados (solo procesa si estado es 1).
    Returns:
        Lista de listas donde cada sublista es [Nombre, Genero, Legajo, Nota1, Nota2...].
    """
    lista_estudiante = []
    
    for i in range(len (matriz)):
        if estados[i] == 1:
            fila = [nombre[i], genero[i],legajo[i]]
            for j in range (len(matriz[i])):
                fila += [matriz[i][j]]

            lista_estudiante += [fila]
        
    return lista_estudiante    

def ver_todos_estudiantes(lista_estudiantes: list) -> None:
    """Muestra los datos de todos los estudiantes.
    Args:
        lista_estudiantes: Lista combinada generada por la función 'recorrido'.
    Returns:
        None
    """

    for i in lista_estudiantes:
            print(f"Datos del estudiante {i[0]}, Genero {i[1]}, numero de legajo {i[2]}, Sus Notas son: ")
            for j in range(3, len(i)):
                print(f" {i[j]}")


def ver_estudiante(lista_estudiantes: list) -> None:
    """Busca un estudiante por nombre e imprime sus datos y notas.
    Args:
        lista_estudiantes: Lista combinada generada por la función 'recorrido'.
    Returns:
        None
    """
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



def promedio(matriz: list) -> list:
    """Calcula el promedio de notas por cada fila (estudiante).
    Args:
        matriz: Matriz de notas de los estudiantes.
    Returns:
        Lista de flotantes con los promedios calculados.
    """
    for fila in matriz:
        suma = 0
        cantidad = len(fila)
        for nota in fila:
            suma += nota
            
        if cantidad > 0:
            promedio = suma / cantidad
        else:
            promedio = 0.0
            
        lista_promedios += [promedio]
        
    return lista_promedios

def ordenar_por_promedio(lista_estudiantes: list, lista_promedios: list, orden: bool = True) -> None:
    """Ordena AMBAS listas basándose en los valores de la lista de promedios.
    Args:
        lista_estudiantes: La lista con los datos (Nombres, Legajos, etc).
        lista_promedios: La lista con los números decimales de los promedios.
        orden: True para ASC (Menor a Mayor), False para DESC (Mayor a Menor).
    Returns:
        None (Modifica las listas originales directamente).
    """
    prom_temp = []

    for x in lista_promedios:
        prom_temp = prom_temp + [x]
    
    est_temp = []

    for fila in lista_estudiantes:
        nueva_fila = []
        for x in fila:
            nueva_fila = nueva_fila + [x]   # agrego elemento
        est_temp = est_temp + [nueva_fila]
    

    n = len(prom_temp)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            p_actual = prom_temp[j]
            p_siguiente = prom_temp[j+1]
            
            intercambiar = False
            
            if orden == True: # Ascendente
                if p_actual > p_siguiente:
                    intercambiar = True
                texto_orden = "Menor a Mayor"
            else: # Descendente (Mayor a Menor - Default)
                if p_actual < p_siguiente:
                    intercambiar = True
                texto_orden = "Mayor a Menor"
            
            if intercambiar:
                # Intercambiamos en las listas 
                aux_p = prom_temp[j]
                prom_temp[j] = prom_temp[j+1]
                prom_temp[j+1] = aux_p
                
                aux_e = est_temp[j]
                est_temp[j] = est_temp[j+1]
                est_temp[j+1] = aux_e

    print(f"\n--- Ranking de Estudiantes ({texto_orden}) ---")
    for k in range(len(est_temp)):
        nombre = est_temp[k][0] 
        prom = prom_temp[k]
        print(f"{k+1}°: {nombre} - Promedio: {prom}")


def imprimir_lista(lista: list) -> None:
    """Imprime los elementos de una lista en una sola línea separados por espacios.
    Args:
        lista: Lista de elementos a imprimir.
    Returns:
        None
    """
    for i in range(len(lista)):
 	    print(lista[i] , end = " ")
         

def imprimir_matriz(matriz: list) -> None:
    """Imprime una matriz fila por fila.
    Args:
        matriz: La matriz a imprimir.
    Returns:
        None
    """
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(matriz[i][j], end = "")
        print()    

def promedio_materias(matriz: list) -> list:
    """Calcula el promedio por columnas (materias) en lugar de filas.
    Args:
        matriz: Matriz de notas.
    Returns:
        Lista de promedios por materia.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    promedios = []

    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += matriz[i][j]

        if filas > 0:
            prom = suma / filas
        else:
            prom = 0.0
        promedios += [prom]

    return promedios

def mostrar_mayor_promedio_materia(matriz: list) -> None:
    """Identifica y muestra la materia con el mayor promedio general.
    Args:
        matriz: Matriz de notas.
    Returns:
        None
    """

    promedios = promedio_materias(matriz)
    
    max_prom = promedios[0]

    for prom in promedios:
            if prom > max_prom:
                max_prom = prom
    
    for j in range(len(promedios)):
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

def buscar_indice_por_legajo(lista_estudiantes: list, legajo_buscado: int) -> int:
    """Recorre la lista de estudiantes buscando un legajo específico.
    Args:
        lista_estudiantes: La lista combinada (generada por la función recorrido).
        legajo_buscado: El número entero del legajo a buscar.
    Returns:
        El índice (int) donde se encuentra el estudiante, o -1 si no existe.
    """
    # Recorremos toda la lista de estudiantes
    for i in range(len(lista_estudiantes)):
        # la función 'recorrido', el legajo está en la posición 2
        legajo_actual = lista_estudiantes[i][2]
        
        if legajo_actual == legajo_buscado:
            return i #  Devolvemos su posición
            
    return -1 # Retornamos -1 si recorrimos todo y no estaba

def ver_estudiante_legajo(lista_estudiantes: list, lista_promedio: list) -> None:
    """Busca un estudiante por legajo y su promedio.
    Args:
        lista_estudiantes: Lista combinada de estudiantes.
        lista_promedio: Lista de promedios paralela.
    Returns:
        None
    """
    while True:
        buscar = validacion_legajo(input("Ingrese el numero de legajo del estudiante que desea ver: "))
        buscar = (buscar_indice_por_legajo(lista_estudiantes,buscar))

        if buscar != -1:
            datos = lista_estudiantes[buscar]
            prome = lista_promedio[buscar]

            print(f"Datos del estudiante: {datos[0]}")
            print(f"Genero: {datos[1]}")
            print(f"Legajo: {datos[2]}")
            print("Sus Notas son:")
            
            # Recorremos las notas (desde el índice 3)
            for j in range(3, len(datos)):
                 print(f" - {datos[j]}")
                    
            print(f"Promedio general: {prome}")

            break
        else:
            print(" Estudiante no encontrado. Intente nuevamente.\n")


def repeticiones_por_materia(matriz: list, materia: int) -> list:
    """Cuenta cuántas veces aparece cada nota (1-10) en una materia específica.
    Args:
        matriz: Matriz de notas.
        numero_materia: El número de la materia a analizar (int).
    Returns:
        Lista de conteo de 10 elementos, donde el índice+1 es la nota.
    """
    
    col = materia - 1
    
    conteo = [0] * 10

    for fila in matriz:
        nota = fila[col] 
        if 1 <= nota <= 10:
            conteo[nota - 1] += 1  

    return conteo

