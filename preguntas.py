"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():

    """Retorne la suma de la segunda columna.
    Rta/
    214"""
    suma = 0
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            current_line = line.split(",")
            suma = suma + int(current_line[1])
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]"""
    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            current_line = line.split(",")
            current_line = current_line[0]
            if current_line in dict_letras:
                dict_letras[current_line] = dict_letras[current_line]+1
            else: dict_letras[current_line] = 1
    dict_letras = sorted(dict_letras.items())
                    
            
    return dict_letras

def pregunta_03():
    """Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]"""

    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            linea_letras = line[0]
            linea_suma = line[1]
            if linea_letras in dict_letras:
                dict_letras[linea_letras] = int(dict_letras[linea_letras])+int(linea_suma)
                
            else: 
                dict_letras[linea_letras] = linea_suma
    dict_letras = sorted(dict_letras.items())
    return dict_letras

def pregunta_04():
    """La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),]"""

    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            linea_suma = line[2]
            linea_suma = linea_suma.split("-")
            linea_suma = linea_suma[1]
            if linea_suma in dict_letras:
                dict_letras[linea_suma] = dict_letras[linea_suma] + 1
            else: 
                dict_letras[linea_suma] = 1
    dict_letras = sorted(dict_letras.items())
    return dict_letras

def pregunta_05():
    """Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),]"""

    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            linea_numeros = line[1]
            linea_letras = line[0]
            if linea_letras in dict_letras:
                dict_letras[linea_letras].append(linea_numeros)
            else: dict_letras[linea_letras] = [linea_numeros]
    lst=[]
    lst_final=[]
    for key in dict_letras:  
        dict_letras[key] = [max(dict_letras[key]), min(dict_letras[key])]
    
    lst = sorted(dict_letras.items())
    for value in lst:
        lst_final.append((value[0], int(value[1][0]), int(value[1][1])))

    return lst_final

def pregunta_06():
    """La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),]"""
    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            for caracter in line.split(','):
                if caracter.count(':') > 0:
                    if caracter[:3] in dict_letras:
                        dict_letras[caracter[:3]].append(int(caracter[4:]))
                    else: 
                        dict_letras[caracter[:3]] = [int(caracter[4:])]

    for key, value in dict_letras.items():
        dict_letras[key] = [int(min(value)),int(max(value))]
    lst = sorted(dict_letras.items())
    
    lst_final = []
    for value in lst:
        lst_final.append((value[0], int(value[1][0]), int(value[1][1])))

    return lst_final

    """La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),]"""
    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            for caracter in line.split(','):
                if caracter.count(':') > 0:
                    if caracter[:3] in dict_letras:
                        dict_letras[caracter[:3]].append(int(caracter[4:]))
                    else: 
                        dict_letras[caracter[:3]] = [int(caracter[4:])]

    for key, value in dict_letras.items():
        dict_letras[key] = [min(value), max(value)]

    return sorted(dict_letras.items())

def pregunta_07():
    """Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [(0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),]"""
    dict_num ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            linea_numeros = line[1]
            linea_letras = line[0]

            if linea_numeros in dict_num:
                dict_num[linea_numeros].append(linea_letras)
            else: dict_num[linea_numeros] = [linea_letras] 

    lst = sorted(dict_num.items())

    lst_final = []
    for value in lst:
        lst_final.append((int(value[0]),value[1]))

    return lst_final

def pregunta_08():
    """Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [(0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),]"""
    dict_num ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            linea_numeros = line[1]
            linea_letras = line[0]

            if linea_numeros in dict_num:
                if linea_letras in dict_num[linea_numeros]:
                    continue
                else: dict_num[linea_numeros].append(linea_letras)
            else: dict_num[linea_numeros] = [linea_letras] 

    for key, value in dict_num.items():
        dict_num[key] = (sorted(value))
        # dict_num[key] = sorted(dict_num.values())
    lst = sorted(dict_num.items())

    lst_final = []
    for value in lst:
        lst_final.append((int(value[0]),value[1]))

    return lst_final

def pregunta_09():
    """Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {"aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,}"""
    
    dict_letras ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            for caracter in line.split(','):
                if caracter.count(':') > 0:
                    if caracter[:3] in dict_letras:
                        dict_letras[caracter[:3]] +=1
                    else: 
                        dict_letras[caracter[:3]] = 1

    # for key, value in dict_letras.items():
    #     dict_letras[key] = [min(value), max(value)]
    registros = dict((k,v) for k,v in sorted(dict_letras.items()))

    return registros

def pregunta_10():
    """Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]"""
    
    lst =[]
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            linea_letras = line[0]
            columna4= line[3].count(',')+1
            columna5= line[4].count(',')+1
            lst.append((linea_letras, columna4, columna5))

    return lst

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {"a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,}"""
    dict_letras = {}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            columna2 = int(line[1])
            columna4 = line[3]
            for letra in columna4.split(','):
                if letra in dict_letras.keys():
                    dict_letras[letra] += columna2
                else: dict_letras[letra] = columna2
    lst = sorted(dict_letras.items())
    dict_final = {}

    for item in lst:
        dict_final[item[0]] = item[1]
    return dict_final

def pregunta_12():
    """Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324}"""

    dict_letras = {}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            columna_1 = line[0]
            columna_5 = line[4]
            columna_5 = columna_5.replace(":",",").split(",")
            i = 0
            numero = 0
            for valor in columna_5:
                if valor.isnumeric() == True: numero = numero + int(valor)

            if columna_1 in dict_letras:
                dict_letras[columna_1] += numero
            else: dict_letras[columna_1] = numero
    
    dct = {}
    lst = sorted(dict_letras.items())
    for valor in lst: dct[valor[0]]=valor[1]
    
    return dct
