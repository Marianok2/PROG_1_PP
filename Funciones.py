#1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def calificaciones(num: int) -> int :
    
    while True:
        num = str(num)
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

def nombre_apellido(cadena: str)->str:
    texto = False
    while texto != True:
        cadena = str(cadena)
        if cadena == "":
            cadena = input("Ingrese nombre y apellido validos: ")
            break
        for i in cadena:
            caracter = ord(i)
            if 48 <= caracter <= 57 :
                cadena = input("Ingrese nombre y apellido validos: ")
                texto = False
                break
            else:
                texto = True
        if texto == True:
            return cadena

def num_entero_pos(num: int) -> int :
    while True:
        num = str(num)
        if num == "":
            num = input("Ingrese un numero valido: ")
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
            else:
                entero = True

        if entero == True:            
            return int(num)        


def num_entero(num: int) -> int :
    while True:
        num = str(num)
        indice = 0
        if num == "":
            num = input("Ingrese un numero valido: ")
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
            else:
                entero = True

        if entero == True:            
            return int(num)        

# num = input("Ingrese un numero entero: ")
# validacion = print(num_entero(num))


#2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def num_flot(num: float)->float:
    flotante = False
    numero = False
    
    while flotante != True or numero != True:
        num = str(num)
        indice = 0
        contador_punto = 0
        if num == "":
            num = input("Ingrese un dato valido: ")
        if numero == True and flotante == False:
                num = input("Ingrese un dato valido: ")
        for caracter in num:
            
            if caracter == "-" or caracter == "+"  and indice == 0:
                indice += 1 # si tiene valor 2 o mas significa q es --2 o -2-3
                continue # permitir el signo negativo solo al inicio
            if indice > 0 and caracter == "-":
                num = input("Ingrese un dato valido: ")
                break
            indice += 1
            caracter = ord(caracter)
            if  caracter > 48 and caracter < 57:
                numero = True
                
            if caracter == 46: 
                
                contador_punto += 1
                if contador_punto > 1:
                    flotante = False
                    
                    break
                else:    
                    flotante = True
                    continue
            elif  caracter < 48 or caracter > 57 :
                numero = False
                num = input("Ingrese un dato valido: ")
                break
        if numero == True and flotante == True:
            return float(num)

# num = input("Ingrese un numero flotante: ")
# ejer_1 = num_flot(num)
# print(ejer_1)

#3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def cadena(cadena: str)->str:
    texto = False
    while texto != True:
        cadena = str(cadena)
        if cadena == "":
            cadena = input("Ingrese un dato valido: ")
            break
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

# texto = input("Ingrese cadena de caracteres: ")
# dato = ingreso_cadena(texto)
# print (dato)

def min_a_mayus(cadena):
    vacio = ""
    for letra in cadena:
        caracter = ord(letra)
        if 97 <= caracter <= 122:
            vacio += chr(caracter - 32)  
        else:
            vacio += letra  
    return vacio


def validacion_genero(respuesta:str)-> str:
    dato = min_a_mayus(respuesta)
    while dato != 'F' and dato != 'M' and dato != 'X':
        dato = input ("Ingrese un Genero valido ('F', 'M', 'X'): ")
        dato = dato(min_a_mayus)

    return dato

def validacion_legajo(respuesta: int)->int:
    dato = num_entero_pos(respuesta)
    while dato < 100000 or dato > 999999:
        print("Datos incorrecto.")
        dato = (input("Ingrese un numero legajo valido:  "))
        dato =  num_entero_pos(dato)
    else:   
        return dato

def materia_validacion(num: int) -> int :
    
    while True:
        num = str(num)
        if num == "":
            num = input("Ingrese una materia valida:  ")
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
            else:
                entero = True
        if entero == True:
            num = int(num)
            if num < 1 or num > 5:
                print("Datos incorrecto.")
                num = input("Ingrese una materia valida:  ")
            else:   
                return num


