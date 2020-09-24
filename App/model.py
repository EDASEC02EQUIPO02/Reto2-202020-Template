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
               'moviesid': None,
               'production_companies': None,
               'genres': None,
               'director_name': None,
               'ids': None,
               'actores' : None,
               'idsActor' : None,
               'pais': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesid'] = mp.newMap(360000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['production_companies'] = mp.newMap(36000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareCompanyByName)
    catalog['genres'] = mp.newMap(180,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareCompanyByName)
    catalog['director_name'] = mp.newMap(300000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareDirectorByName)
    catalog['ids'] = mp.newMap(360000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareTagIds)
    catalog['actores'] = mp.newMap(300000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareDirectorByName)
    catalog['idsActor'] = mp.newMap(360000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareTagIds)                              
    catalog['pais'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareCompanyByName)
    
    return catalog
#Nuevas cosas para agregar
def newCompany(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareCompanyByName)
    return author

def newGenre(name):
    author = {'name': "", "movies": None,  "average_count": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareCompanyByName)
    return author

def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_movies': 0,
           'movies': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['movies'] = lt.newList('ARRAY_LIST', compareCompanyByName)
    return tag

def newIdActor(name1, name2, name3, name4, name5, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name1': name1,
           'name2': name2,
           'name3': name3,
           'name4': name4,
           'name5': name5,
           'tag_id': ''}
    tag['tag_id'] = id
    return tag

def newActor(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': name,
           'tag_id': '',
           'total_movies': 0,
           'movies': None,
           'count': 0.0}
    tag['tag_id'] = id
    tag['movies'] = lt.newList('ARRAY_LIST', compareCompanyByName)
    return tag

def newCountry(name): 
    author = {'name': "", "movies": None}
    author['name'] = name
    author['movies'] = lt.newList('ARRAY_LIST', compareCompanyByName)
    #{'titulo': title, 'fecha de lanzamiento': date, 'director': director}
    return author

def infotitle(title, date, director):
    info = {'titulo': title, 'fecha de lanzamiento': date, 'director': director}
    return info
#Agregar cosas a los diccionarios
def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagBook(tag['director_name'], tag['id'])
    mp.put(catalog['director_name'], tag['director_name'], newtag)
    mp.put(catalog['ids'], tag['id'], newtag)

#Requerimiento 3

def addActor(catalog, tag):
    a1 = tag['actor1_name']
    a2 = tag['actor2_name']
    a3 = tag['actor3_name']
    a4 = tag['actor4_name']
    a5 = tag['actor5_name']
    newtag = newIdActor(a1, a2, a3, a4, a5, tag['id'])
    for i in range(1,6):
        mp.put(catalog['actores'], tag['actor' + str(i) + '_name'], newActor(tag['actor' + str(i) + '_name'], tag['id']))
    mp.put(catalog['idsActor'], tag['id'], newtag)
    


def addMovieActor(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    tagid = tag['id']
    entry = mp.get(catalog['idsActor'], tagid)

    if entry:
        for i in range(1, 6):
            tagbook = mp.get(catalog['actores'], me.getValue(entry)['name'+str(i)])
            tagbook['value']['total_movies'] += 1
            movie = mp.get(catalog['moviesid'], tagid)
            valor = me.getValue(movie)
            if (tagbook['value']['count'] == 0.0):
                tagbook['value']['count'] = float(valor['vote_average'])
            else:
                tagbook['value']['count'] += float(valor['vote_average'])
            if movie:
                lt.addLast(tagbook['value']['movies'], valor['original_title'])
    


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    tagid = tag['id']
    entry = mp.get(catalog['ids'], tagid)

    if entry:
        tagbook = mp.get(catalog['director_name'], me.getValue(entry)['name'])
        tagbook['value']['total_movies'] += 1
        movie = mp.get(catalog['moviesid'], tagid)
        valor = me.getValue(movie)
        if (tagbook['value']['count'] == 0.0):
            tagbook['value']['count'] = float(valor['vote_average'])
        else:
            tagbook['value']['count'] += float(valor['vote_average'])
        if movie:
            lt.addLast(tagbook['value']['movies'], valor['original_title'])


#agregar las peliculas a la lista
def addMovie(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['moviesid'], movie['id'], movie)

#Agregar las películas a una compañia 
def addMovieCompany(catalog, companyname, movie):

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
        author['average_rating'] += float(bookavg)


def addMovieGenre(catalog, genrename, movie):

    authors = catalog['genres']
    existauthor = mp.contains(authors, genrename)
    if existauthor:
        entry = mp.get(authors, genrename)
        author = me.getValue(entry)
    else:
        author = newGenre(genrename)
        mp.put(authors, genrename, author)
    lt.addLast(author['movies'], movie)

    authavg = author['average_count']
    bookavg = movie['vote_count']
    if (authavg == 0.0):
        author['average_count'] = float(bookavg)
    else:
        author['average_count'] += float(bookavg)

def addMovieCountry(catalog, countryname, movie):

    authors = catalog['pais']
    existauthor = mp.contains(authors, countryname)
    a = mp.get(catalog['ids'], movie['id'])
    dire = me.getValue(a)
    if existauthor:
        entry = mp.get(authors, countryname)
        author = me.getValue(entry)
    else:
        author = newCountry(countryname)
        mp.put(authors, countryname, author)
    info = infotitle(movie['original_title'], movie['release_date'], dire['name'])
    lt.addLast(author['movies'], info)



def getMoviesByCompany(catalog, authorname):

    author = mp.get(catalog['production_companies'], authorname)
    if author:
        return me.getValue(author)
    return None
    
def getMoviesByGenre(catalog, authorname):
 
    author = mp.get(catalog['genres'], authorname)
    if author:
        return me.getValue(author)
    return None


def getBooksByTag(catalog, tagname):

    tag = mp.get(catalog['director_name'], tagname)
    if tag:
        return me.getValue(tag)
    return None

def getMovieByActor(catalog, tagname):

    tag = mp.get(catalog['actores'], tagname)
    if tag:
        return me.getValue(tag)
    return None


def getMoviesByCountry(catalog, authorname):

    author = mp.get(catalog['pais'], authorname)
    if author:
        return me.getValue(author)
    return None



#los compare de TADmap
def compareCompanyByName(keyname, company):

    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareDirectorByName(keyname, director):

    authentry = me.getKey(director)
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

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0      

def compareMapMoviesIds(id, entry):

    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareRecordIds (element1, element2):
    if int(element1["id"]) == int(element2["id"]):
        return 0
    elif int(element1["id"]) > int(element2["id"]):
        return 1
    return -1


