"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import csv
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time 
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'peliculas': None,
               'titulo': None,
               'moviesid': None,
               'production_companies': None,
               'vote_count': None,
               'idioma': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesid'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMoviesIds)
    catalog['production_companies'] = mp.newMap(18051,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareCompanyByName)
    return catalog

def loadCSVFile (file, cmpfunction):
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst



def newCompany(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareCompanyByName)
    return author


#agregar las peliculas a la lista
def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    #mp.put(catalog['moviesid'], movie['id'], movie)

#Agregar las películas a una compañia 
def addMovieCompany(catalog, companyname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    authors = catalog['production_companies']
    existauthor = mp.contains(authors, companyname)
    if existauthor:
        entry = mp.get(authors, companyname)
        author = me.getValue(entry)
    else:
        author = newCompany(companyname)
        mp.put(authors, companyname, author)
    lt.addLast(author['movies'], movie)

    authavg = author['average_rating']
    bookavg = movie['vote_average']
    if (authavg == 0.0):
        author['average_rating'] = float(bookavg)
    else:
        author['average_rating'] = (authavg + float(bookavg)) / 2



def getMoviesByCompany(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['production_companies'], authorname)
    if author:
        return me.getValue(author)
    return None




#los compare de TADmap
def compareCompanyByName(keyname, company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1











def numeroPeliculas(lista1):
    lst=lt.size(lista1)
    return lst


def primeraPelicula(lista1):
    dato = lt.getElement(lista1, 1)
    peliculaP = dato['original_title']
    return peliculaP


def ultimaPelicula(lista1):
    lst=lt.size(lista1)
    dato = lt.getElement(lista1, lst)
    peliculaU = dato['original_title']
    return peliculaU

def fechaEstrenoP(lista1):
    dato = lt.getElement(lista1, 1)
    fechaP = dato['release_date']
    return fechaP
    
def fechaEstrenoU(lista1):
    lst=lt.size(lista1)
    dato = lt.getElement(lista1, lst)
    fechaU = dato['release_date']
    return fechaU

def promP(lista1):
    dato = lt.getElement(lista1, 1)
    promP = dato['vote_average']
    return promP

def promU(lista1):
    lst=lt.size(lista1)
    dato = lt.getElement(lista1, lst)
    promU = dato['vote_average']
    return promU

def votP(lista1):
    dato = lt.getElement(lista1, 1)
    votP = dato['vote_count']
    return votP

def votU(lista1):
    lst=lt.size(lista1)
    dato = lt.getElement(lista1, lst)
    votU = dato['vote_count']
    return votU

def idiomaP(lista1):
    dato = lt.getElement(lista1, 1)
    idiomaP = dato['spoken_languages']
    return idiomaP

def idiomaU(lista1):
    lst=lt.size(lista1)
    dato = lt.getElement(lista1, lst)
    idiomaU = dato['spoken_languages']
    return idiomaU

# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
        
def compareRecordIds (element1, element2):
    if int(element1["id"]) == int(element2["id"]):
        return 0
    elif int(element1["id"]) > int(element2["id"]):
        return 1
    return -1


