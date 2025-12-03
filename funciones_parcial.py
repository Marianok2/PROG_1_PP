
from Funciones import *
def dato_harco(l_nombre,l_genero,l_lega,l_esta,matriz):
    nom = ["mariano","mateo","paloma","antonio"]
    l_nombre += nom
    gen = ["m","m","f","x"]
    l_genero += gen
    leg = [102030,203010,103020,403020]
    l_lega += leg
    mat =[
        [3,7,8],
        [6,9,4],
        [8,8,5],
        [5,7,7]
    ]
    matriz += mat
    est = [1,1,1,1]
    l_esta += est

def cargar_datos_por_uno(cant_est: int, cant_mat: int, l_nombres: list, l_generos: list, l_legajos: list,matriz: list, l_estados: list) -> None:
    
    for i in range(cant_est):
        print(f"\n--- Carga datos Estudiante N° {i+1} ---")

        # 1. Nombre
        nom = input("Ingrese Nombre y Apellido: ")
        nom = nombre_apellido(nom)
        l_nombres += [nom] 

        # 2. Género
        gen = input(f"Ingrese Genero de {nom} ('F', 'M', 'X'): ")
        gen = validacion_genero(gen)
        l_generos += [gen]

        # 3. Legajo
        leg = input(f"Ingrese Legajo: ")
        leg = validacion_legajo(leg)
        l_legajos += [leg]

        # 4. Notas (Armamos la fila y la metemos a la matriz)
        fila_notas = []
        for j in range(cant_mat):
            nota = input(f"  - Nota materia {j+1}: ")
            nota = calificaciones(nota)
            fila_notas += [nota]
        
        matriz += [fila_notas] 

        # 5. Estado
        l_estados += [1]

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

    txt = "Nombre y Apellido"
    espacios = 25 - len(txt) 
    m = int (espacios/2 )
    celda_nom = (""*m) + txt + (" " * espacios)

    txt2 = "Gen"
    espacios_totales = 5 - len(txt2)
    mitad1 = int(espacios_totales / 2)
    resto1 = espacios_totales - mitad1
   
    celda_gen = (" " * mitad1) + txt2 + (" " * resto1)

    txt3 = "Legajo"
    espacios_totales = 10 - len(txt3)
    mitad2 = int(espacios_totales / 2)
    resto2 = espacios_totales - mitad2
    celda_leg = (" " * mitad2) + txt3 + (" " * resto2)

    linea_entera = "| " + celda_nom + " | " + celda_gen + " | " + celda_leg + " |"

    cant_materias = len(lista_estudiantes[0]) - 3
    
    for k in range(cant_materias):
        txt4 = "Mat. " + str(k+1)

        espacios_totales = 7 - len(txt4)
        mitad3 = int(espacios_totales / 2)
        resto3 = espacios_totales - mitad3
        
        celda_mat = (" " * mitad3) + txt4 + (" " * resto3)
        linea_entera += " " + celda_mat + " |"

    largo_total = len(linea_entera)
    print("-" * largo_total)
    print(linea_entera)
    print("-" * largo_total)

    for est in lista_estudiantes:

        nombre = str(est[0])
        genero = str(est[1])
        legajo = str(est[2])

        espacios = 25 - len(nombre)
        celda_nom = nombre + (" " * espacios)

        espacios_totales = 5 - len(genero)
        mitad1 = int(espacios_totales / 2)
        resto1 = espacios_totales - mitad1
        celda_gen = (" " * mitad1) + genero + (" " * resto1)

        espacios_totales = 10 - len(legajo)
        mitad2 = int(espacios_totales / 2)
        resto2 = espacios_totales - mitad2
        celda_leg = (" " * mitad2) + legajo + (" " * resto2)

        fila = "| " + celda_nom + " | " + celda_gen + " | " + celda_leg + " |"

        for j in range(3, len(est)):
            nota = str(est[j])
            
            espacios_totales = 7 - len(nota)
            mitad3 = int(espacios_totales / 2)
            resto3 = espacios_totales - mitad3
            
            celda_nota = (" " * mitad3) + nota + (" " * resto3)
            fila += " " + celda_nota + " |"

        print(fila)

    print("-" * largo_total)

def dibujo_prome():
    txt = "¡ Promedios cargados exitosamente !"
    espacios_totales = 50 - len(txt) 
    
    m_izquierda = int(espacios_totales / 2)
    m_derecha = espacios_totales - m_izquierda
    celda_nom = ("|"+" " * m_izquierda) + txt + (" " * m_derecha+"|")
    
    largo_total = len(celda_nom) 
    
    print("-" * largo_total)
    print(celda_nom)
    print("-" * largo_total)

def promedio(matriz: list) -> list:
    """Calcula el promedio de notas por cada fila (estudiante).
    Args:
        matriz: Matriz de notas de los estudiantes.
    Returns:
        Lista de flotantes con los promedios calculados.
    """
    lista_promedios = []
    for fila in matriz:
        suma = 0
        cantidad = len(fila)
        for nota in fila:
            suma += nota
            
        if cantidad > 0:
            promedio = suma / cantidad
            promedio = (promedio * 100 // 1) / 100
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
    if orden:
        texto_orden = "Menor a Mayor"
    else:
        texto_orden = "Mayor a Menor"


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
                
            else: # Descendente (Mayor a Menor - Default)
                if p_actual < p_siguiente:
                    intercambiar = True
                
            
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
        buscar = buscar_indice_por_legajo(lista_estudiantes,buscar)

        if buscar != -1:
            datos = lista_estudiantes[buscar]
            prome = lista_promedio[buscar]

            dibuja_legajo(datos,prome)

            break
        else:
            print(" Estudiante no encontrado. Intente nuevamente.\n")


def repeticiones_por_materia(matriz: list, materia: int) -> list:
    """Cuenta cuántas veces aparece cada nota (1-10) en una materia específica.
    Args:
        matriz: Matriz de notas.
        materia: El número de la materia a analizar (int).
    Returns:
        Lista de conteo de 10 elementos, donde el índice+1 es la nota.
    """
    materia = materia_validacion(materia)
    columna = materia - 1
    
    # Inicializamos lista fija de 10 ceros
    contadores = [0] * 10 
    
    for i in range(len(matriz)):
        # Tomamos la nota de la fila i, columna seleccionada
        nota = matriz[i][columna]
        
        # Validamos que sea nota valida (por si hay 0s de inicializacion)
        idx = nota - 1
        contadores[idx] = contadores[idx] + 1
            
    for k in range(10):
        print("Nota", k+1, ":", " se repite " ,contadores[k], "veces")
