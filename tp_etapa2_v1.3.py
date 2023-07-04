import random

""" ACA EMPIEZA LA ETAPA 8"""

def nueva_creacion_diccionario():
    
    with open("palabras.txt", "r") as palabras, open("definiciones.txt", "r") as definiciones:
        
        diccionario = {}
        palabra = palabras.readline().strip()
        definicion = definiciones.readline().strip()
        
        while palabra != "" and definicion != "":
            if palabra.isalpha():
                diccionario[palabra] = definicion

            palabra = palabras.readline().strip()
            definicion = definiciones.readline().strip()

    palabras.close()
    definiciones.close()

    palabras_ordenadas = sorted(diccionario.keys())
    
    """ en esta primera parte de la atapa 8:
    se abren los dos archivos que fueron otorgados, el de palabras y el definiciones.
    luego se crea un diccionario vacio, y se leen simultaneamente las lineas de ambos archivos con .readline()
    se crea un bucle while que tiene como condicion mientras haya palabra y definicion
    con el metodo .isalpha() se verifica que la palabra contenga solamente caracteres alfabeticos
    luego se cierran los archivos
    y se ordena la lista de palabras con un sorted y .keys() del diccionario    
    """
    
    with open("diccionario.csv", "w") as diccionario_exportar:
        for palabra in palabras_ordenadas:
            definicion = diccionario[palabra]
            diccionario_exportar.write(f"{palabra}, '{definicion}'\n")

    return diccionario

# guido tiscornia

    """ en esta segunda parte de la atapa 8:
    se abren los dos archivos que fueron otorgados, el de palabras y el definiciones.
    luego se crea un diccionario vacio, y se leen simultaneamente las lineas de ambos archivos con .readline()
    se crea un bucle while que tiene como condicion mientras haya palabra y definicion
    con el metodo .isalpha() se verifica que la palabra contenga solamente caracteres alfabeticos
    luego se cierran los archivos
    y se ordena la lista de palabras con un sorted y .keys() del diccionario    
    """
    
""" ACA TERMINA LA ETAPA 8"""


def obtener_lista_10_letras(lista_letras):
    """crea una lista vacia, un contador
    con un bucle while mientras el contador sea menor a 10 se selecciona una letra al alzar de la lista de letras
    si la letra ya está incluida no la agrega y si falta la agrega y suma uno al contador
    ordena la lista y la retorna
    """
    lista_letras_participantes = []
    contador_letras = 0
    while contador_letras < 10:
        letra_al_azar_actual = random.choice(lista_letras)
        if letra_al_azar_actual not in lista_letras_participantes:
            lista_letras_participantes.append(random.choice(lista_letras))
            contador_letras += 1
    lista_letras_participantes.sort()
    return lista_letras_participantes
#guido tiscornia


def obtener_lista_10_palabras(diccionario_de_pd, lista_letras_elegidas):
    """con el diccionario creado y la lista de letras elegidas crea una lista vacia de palabras
    para cada letra con un bucle for recorre todas las palabras del diccionario y las agrega a una lista si empiezan con esa letra
    luego selecciona una palabra al azar de la lista de palabras de cada letra
    agrega las palabras elegidas de cada letra y retorna esa lista de palabras
    """
    lista_palabras_definitiva = []
    for letra in lista_letras_elegidas:
        palabras_con_esa_letra = []
        for palabra in diccionario_de_pd:
            if palabra[0] == letra:
                palabras_con_esa_letra.append(palabra)
        palabra_seleccionada_al_azar = random.choice(palabras_con_esa_letra)
        lista_palabras_definitiva.append(palabra_seleccionada_al_azar)
    return lista_palabras_definitiva
#guido tiscornia


def obtener_lista_10_definiciones(diccionario_de_pd, lista_palabras_elegidas):
    """
    a partir de la lista de palabras elegidas, itera en el diccionario generado para seleccionar las definiciones
    segun la palabra encontrada
    """
    lista_definiciones_definitivas = []
    for palabra in lista_palabras_elegidas:
        if palabra in diccionario_de_pd:
            lista_definiciones_definitivas.append(diccionario_de_pd[palabra])
    return lista_definiciones_definitivas
#joaquin maguina


def contar_palabras_empiezan_con_letra(dicc, letra):
    """
    itera dentro del diccionario generado y cuenta cuantas palabras empiezan con la letra en el parametro
    """
    contador = 0
    for palabra in dicc:
        if palabra[0] == letra:
            contador += 1
    return contador
#joaquin maguina y santiago bassedas


def imprimir_cantidad_palabras_para_letra(letra, cantidad):
    print(f"Cantidad de palabras en el diccionario para la letra {letra}: {cantidad}.")
#santiago bassedas


# muestra las letras a utilizar
def mostrar_letras(lista_letras):
    for letra in lista_letras:
        print(f"[{letra}]\t", end="")
    print()
#joaquin maguina

# muestra 'a' o 'e' segun acierto o error
def mostrar_resultados(lista_resultados):
    for resultado in lista_resultados:
        if resultado == "":
            print("[ ]\t", end="")
        else:
            print(f"[{resultado}]\t", end="")
    print()
#pablo martinez

# muestra turnos
def mostrar_turno(letra, palabra, definicion):
    largo_palabra = len(palabra)
    print(f"Turno letra {letra} - Palabra de {largo_palabra} letras")
    print(f"Definición: {definicion}")
#pablo martinez


# si el usuario no ingresa caracteres validos
def solicitar_respuesta():
    palabra = input("Ingrese palabra: ")
    while not palabra.isalpha():
        palabra = input("Su ingreso no es valido, intente de nuevo: ")
    return palabra
#guido tiscornia


# verifica la palabra ingresada con la mostrada
def verificar_palabra(palabra_ingresada, palabra_mostrada):
    return palabra_ingresada == palabra_mostrada
#joaquin maguina

# muestra el puntaje actual después de cada turno / palabra mostrada
def mostrar_puntaje_actual(aciertos, errores):
    print(f"Aciertos: {aciertos}")
    print(f"Errores : {errores}")
#santiago bassedas


# sumo o resto puntos
def puntaje_final(aciertos, errores):
    return (aciertos * 10) + (errores * (-3))
#santiago bassedas

# pregunta si desea jugar otra vez, basado en SI o NO como respuesta
def jugar_otra():
    """
    pregunta al jugador si quiere o no seguir continuando con la partida
    en caso de que acepte, se reinicia el juego
    si no acepta se terminara la partida, si ingresa cualquier otra cosa, vuelve a preguntar
    """
    valor = True
    bandera = None
    while valor:
        otra_vez = input(
            "¿Desea jugar otra partida? Responda SI o NO. El puntaje final se mantendrá desde la jugada anterior: ")
        otra_vez = otra_vez.upper()
        if otra_vez == "SI":
            bandera = True
            valor = False
        elif otra_vez == "NO":
            bandera = False
            valor = False
    return bandera
#guido tiscornia

# funcion principal
def main():

    # se definen las variables a utilizar luego
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
    aciertos = 0
    errores = 0
    dicc_generado = nueva_creacion_diccionario()

    # se calcula e imprime la cantidad de palabras en el diccionario generado
    cant_de_palabras = len(dicc_generado)
    print(f"Cantidad de palabras en el diccionario: {cant_de_palabras}.")

    # se inicia el puntaje para la primera corrida y se habilita el juego
    puntaje_total = 0
    jugar = True

    while jugar:
        # se itera en las letras del abecedario y se imprime la cantidad de palabras que que tiene cada una en el
        # diccionario
        for letra in lista_letras:
            cantidad_letra_actual = contar_palabras_empiezan_con_letra(dicc_generado, letra)
            imprimir_cantidad_palabras_para_letra(letra, cantidad_letra_actual)

        # se eligen las 10 letras, palabras y definiciones para el juego
        lista_letras_elegidas = obtener_lista_10_letras(lista_letras)
        lista_palabras_elegidas = obtener_lista_10_palabras(dicc_generado, lista_letras_elegidas)
        lista_definiciones_elegidas = obtener_lista_10_definiciones(dicc_generado, lista_palabras_elegidas)

        # se generan e imprime el tablero con letras elegidas y puntaje
        lista_resultados = [""] * len(lista_letras_elegidas)
        mostrar_letras(lista_letras_elegidas)
        mostrar_resultados(lista_resultados)

        # se inician los turnos (de 0 a 9)
        turno_actual = 0

        # se itera en cada letra de las 10 letras
        for letra_generada in lista_letras_elegidas:
            # se define la palabra del turno actual y muestra en pantalla
            palabra_turno_actual = lista_palabras_elegidas[turno_actual]
            definicion_turno_actual = lista_definiciones_elegidas[turno_actual]
            mostrar_turno(letra_generada, palabra_turno_actual, definicion_turno_actual)
            #        SOLO COMO PRUEBA >>> print(palabra_turno_actual)
            # solicita respuesta al usuario para comparar a la palabra del turno actual
            palabra_ingresada_actual = solicitar_respuesta()

            # verifica la palabra ingresada con la palabra del turno actual y calcula acierto o error
            if verificar_palabra(palabra_ingresada_actual, palabra_turno_actual):
                print("Respuesta correcta.")
                aciertos += 1
                # compara la letra elegida con la ingresada y la asigna a una lista para luego imprimir el tablero
                for i in range(len(lista_letras_elegidas)):
                    if lista_letras_elegidas[i] == letra_generada:
                        lista_resultados[i] = 'a'
            else:
                print("Respuesta incorrecta.")
                errores += 1
                # compara la letra elegida con la ingresada y la asigna a una lista para luego imprimir el tablero
                for i in range(len(lista_letras_elegidas)):
                    if lista_letras_elegidas[i] == letra_generada:
                        lista_resultados[i] = 'e'

            # imprime el tablero con letras, resultados y puntaje hasta el turno actual
            mostrar_letras(lista_letras_elegidas)
            mostrar_resultados(lista_resultados)
            mostrar_puntaje_actual(aciertos, errores)
            print()
            turno_actual += 1

        # calcula puntaje al finalizar la ronda, imprime resultado
        puntaje_final_al_turno = puntaje_final(aciertos, errores)
        print(f"Puntaje final: {puntaje_final_al_turno}")

        # agrega el puntaje de esta ronda al "puntaje final", si el usuario quiere jugar de nuevo
        puntaje_total += puntaje_final_al_turno
        # pregunta si quiere jugar otra ronda
        jugar = jugar_otra()


main()
#autor: guido tiscornia, joaquin maguina, santiago bassedas, pablo martinez
