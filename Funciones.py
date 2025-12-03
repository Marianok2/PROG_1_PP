#1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def calificaciones(num: str) -> int:
    """Valida que la calificación sea un número entero entre 1 y 10.
    Args:
        num: El valor a validar (puede venir como string o int).
    Returns:
        El número entero validado entre 1 y 10.
    """
    
    while True:
        num = str(num)
        entero = True

        if num == "":
            num = input("Ingrese una calificacion valida:  ")
        for caracter in num:
            
            if caracter == "-":
                print("Datos incorrecto.")
                num = input("Ingrese una calificacion valida:  ")
                break
            
            if ord(caracter) < 48 or ord(caracter) > 57:
                print("Datos incorrecto.")
                num = input("Ingrese una calificacion valida:  ")
                entero = False
                break
            else:
                entero = True
        if entero == True:
            num = int(num)
            if num < 1 or num > 10:
                print("Datos incorrecto.")
                num = input("Ingrese una calificacion valida:  ")
            else:   
                return num

def nombre_apellido(cadena: str) -> str:
    """Valida que una cadena no contenga números.
    Args:
        cadena: El texto a validar.
    Returns:
        La cadena validada sin números.
    """
    texto = True
    
    while True:
        cadena = min_a_mayus(cadena)
        cadena = str(cadena)
        indice = 0
        if cadena == "":
            cadena = input("Ingrese nombre y apellido validos: ")
            continue
        
        
        for i in cadena:
            caracter = ord(i)
            if 48 <= caracter <= 57 and caracter != 32 :
                cadena = input("Ingrese nombre y apellido validos: ")
                texto = False
                break
            if caracter == 32 and indice == 0:
                cadena = input("Ingrese nombre y apellido validos: ")
                texto = False
                break
            else:
                indice += 1
                texto = True
        if texto == True:
            return cadena

def num_entero_pos(num: int) -> int:
    """Valida y retorna un número entero positivo.
    Args:
        num: El valor a validar.
    Returns:
        El número entero positivo.
    """
    while True:
        num = str(num)
        if num == "":
            num = input("Ingrese un numero valido: ")
            continue

        entero = True
        for caracter in num:
            
            if caracter == "-":
                    print("Datos incorrecto.")
                    num = input("Ingrese un numero valido:  ")
                    entero = False
                    break
            if ord(caracter) < 48 or ord(caracter) > 57:
                print("Datos incorrecto.")
                num = input("Ingrese un numero valido:  ")
                entero = False
                break

        if entero :            
            return int(num)        


def num_entero(num: int) -> int:
    """Valida y retorna un número entero (permite negativos).
    Args:
        num: El valor a validar.
    Returns:
        El número entero validado.
    """
    while True:
        num = str(num)
        indice = 0
        if num == "":
            num = input("Ingrese un numero valido: ")
            continue

        entero = True
        for caracter in num:
            
            if caracter == "-" or caracter == "+" and indice == 0:
                    indice += 1 # si tiene valor 2 o mas significa q es --2 o -2-3
                    continue  # permitir el signo negativo solo al inicio
            indice += 1
            if ord(caracter) < 48 or ord(caracter) > 57:
                print("Datos incorrecto.")
                num = input("Ingrese un numero valido:  ")
                entero = False
                break

        if entero :            
            return int(num)        

#2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def num_flot(num: int) -> float:
    """Valida y retorna un número flotante (decimal).
    Args:
        num: El valor a validar.
    Returns:
        El número flotante validado.
    """
    
    while True:

        num = str(num)

        if num == "":
            num = input("Ingrese un dato valido: ")
            continue

        indice = 0
        contador_punto = 0
        es_valido = True

        for caracter in num:
            
            if (caracter == "-" or caracter == "+" ) and indice == 0:
                indice += 1 # si tiene valor 2 o mas significa q es --2 o -2-3
                continue # permitir el signo negativo solo al inicio
            if indice > 0 and (caracter == "-" or caracter == "+"):
                print("Datos incorrecto.")
                num = input("Ingrese un dato valido: ")
                es_valido = False
                break
            indice += 1
            caracter = ord(caracter)

            if caracter == 46: 
                contador_punto += 1
                if contador_punto > 1:
                    print("Datos incorrecto (demasiados puntos).")
                    num = input("Ingrese un dato valido: ")
                    es_valido = False
                    break

            elif  caracter < 48 or caracter > 57 :
                print("Datos incorrecto.")
                es_valido = False
                num = input("Ingrese un dato valido: ")
                break
        if es_valido:
            return float(num)

#3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def cadena(cadena: str) -> str:
    """Valida una cadena genérica asegurando que no tenga números.
    Args:
        cadena: La cadena a validar.
    Returns:
        La cadena validada.
    """
    texto = False

    while texto == False:
        cadena = str(cadena)
        if cadena == "":
            cadena = input("Ingrese un dato valido: ")
            continue
            
        for i in cadena:
            caracter = ord(i)
            if 48 <= caracter <= 57 :
                cadena = input("Ingrese un dato valido: ")
                texto = False
                break
            else:
                texto = True
        if texto == True:
            return cadena

def min_a_mayus(cadena: str) -> str:
    """Convierte una cadena de minúsculas a mayúsculas manualmente.
    Args:
        cadena: El texto en minúsculas.
    Returns:
        El texto convertido a mayúsculas.
    """
    vacio = ""
    for letra in cadena:
        caracter = ord(letra)
        if 97 <= caracter <= 122:
            vacio += chr(caracter - 32)  
        else:
            vacio += letra  
    return vacio

def mayus_a_min(cadena: str) -> str:
    """Convierte una cadena de mayúsculas a minúsculas  manualmente.
    Args:
        cadena: El texto en minúsculas.
    Returns:
        El texto convertido a mayúsculas.
    """
    vacio = ""
    for letra in cadena:
        caracter = ord(letra)
        if 65 <= caracter <= 90:
            vacio += chr(caracter + 32)  
        else:
            vacio += letra  
    return vacio
def validacion_genero(respuesta: str) -> str:
    """Valida el género ingresado permitiendo solo F, M o X.
    Args:
        respuesta: El carácter ingresado inicialmente.
    Returns:
        El género validado en mayúscula ('F', 'M', 'X').
    """
    dato = min_a_mayus(respuesta)
    while dato != 'F' and dato != 'M' and dato != 'X':
        dato = input ("Ingrese un Genero valido ('F', 'M', 'X'): ")
        dato = min_a_mayus(dato)

    return dato

def validacion_legajo(respuesta: str) -> int:
    """Valida que el legajo sea un número entero de 6 cifras.
    Args:
        respuesta: El valor a validar.
    Returns:
        El número de legajo validado (entre 100000 y 999999).
    """
    
    dato = num_entero_pos(respuesta)
    while dato < 100000 or dato > 999999:
        print("Datos incorrecto.")
        dato = (input("Ingrese un numero legajo valido:  "))
        dato =  num_entero_pos(dato)
      
    return dato

def materia_validacion(nume: int) -> int:
    """Valida que el número de materia esté entre 1 y numero de columnas.
    Args:
        nume: el numero de materias.
    Returns:
        El número de materia entero validado.
    """

    num = input(f"Ingrese numero de materia (1-{nume}): ")

    while True:
        num = str(num)
        if num == "":
            num = input("Ingrese una materia valida:  ")
            continue
        entero = True
        for caracter in num:
            
            if caracter == "-":
                print("Datos incorrecto.")
                num = input("Ingrese una materia valida:  ")
                break
            
            if ord(caracter) < 48 or ord(caracter) > 57:
                print("Datos incorrecto.")
                num = input("Ingrese una materia valida:  ")
                entero = False
                break

        if entero:
            num = int(num)
            if num < 1 or num > nume:
                print("Datos incorrecto.")
                num = input("Ingrese una materia valida:  ")
            else:   
                return num



def dibuja_legajo(dato,prome):
    #  CONFIGURACIÓN DE ANCHOS
            ancho_nom = 25
            ancho_gen = 5
            ancho_leg = 10
            ancho_mat = 7
            ancho_prom = 10

            #  CONSTRUIR ENCABEZADO 
            
            # Nombre (Alineado Izquierda)
            txt = "Nombre y Apellido"
            espacios = ancho_nom - len(txt)
            celda_nom = txt + (" " * espacios)

            # Genero (Centrado)
            txt = "Gen"
            esp = ancho_gen - len(txt)
            mitad = int(esp / 2)
            celda_gen = (" " * mitad) + txt + (" " * (esp - mitad))

            # Legajo (Centrado)
            txt = "Legajo"
            esp = ancho_leg - len(txt)
            mitad = int(esp / 2)
            celda_leg = (" " * mitad) + txt + (" " * (esp - mitad))

            # Base del encabezado
            linea_header = "| " + celda_nom + " | " + celda_gen + " | " + celda_leg + " |"

            # Materias (Dinámico)
            cant_materias = len(dato) - 3 # Restamos nombre, genero, legajo
            
            for k in range(cant_materias):
                txt = "Mat " + str(k+1)
                esp = ancho_mat - len(txt)
                mitad = int(esp / 2)
                celda_mat = (" " * mitad) + txt + (" " * (esp - mitad))
                linea_header += " " + celda_mat + " |"

            # Promedio (Centrado)
            txt = "Promedio"
            esp = ancho_prom - len(txt)
            mitad = int(esp / 2)
            celda_prom = (" " * mitad) + txt + (" " * (esp - mitad))
            linea_header += " " + celda_prom + " |"

            # IMPRIMIR ENCABEZADO
            largo_total = len(linea_header)
            print("-" * largo_total)
            print(linea_header)
            print("-" * largo_total)

            # CONSTRUIR LA FILA DE DATOS ---

            nombre = str(dato[0])
            genero = str(dato[1])
            legajo = str(dato[2])

            # Nombre (Izq)
            esp = ancho_nom - len(nombre)
            if esp < 0: esp = 0
            celda_nom = nombre + (" " * esp)

            # Genero (Centro)
            esp = ancho_gen - len(genero)
            mitad = int(esp / 2)
            celda_gen = (" " * mitad) + genero + (" " * (esp - mitad))

            # Legajo (Centro)
            esp = ancho_leg - len(legajo)
            mitad = int(esp / 2)
            celda_leg = (" " * mitad) + legajo + (" " * (esp - mitad))

            fila = "| " + celda_nom + " | " + celda_gen + " | " + celda_leg + " |"

            # Notas (Centro)
            for j in range(3, len(dato)):
                nota = str(dato[j])
                esp = ancho_mat - len(nota)
                mitad = int(esp / 2)
                celda_nota = (" " * mitad) + nota + (" " * (esp - mitad))
                fila += " " + celda_nota + " |"

            # Promedio (Centro)

            prom_str = str(round(prome, 2)) 
            esp = ancho_prom - len(prom_str)
            mitad = int(esp / 2)
            celda_prom = (" " * mitad) + prom_str + (" " * (esp - mitad))
            fila += " " + celda_prom + " |"

            # IMPRIMIR FILA
            print(fila)
            print("-" * largo_total)
            print("")