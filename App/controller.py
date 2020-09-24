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

import config as cf
from App import model
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import csv
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

def loadData(catalog, moviefile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    t1 = process_time()
    loadMovies(catalog, moviefile)
    loadCasting(catalog, castingfile)
    loadBooksTags(catalog, moviefile)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadMovies(catalog, moviefile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    moviefile = cf.data_dir + moviefile
    input_file = csv.DictReader( open(moviefile, encoding="utf-8"), delimiter=";")
    
    for movie in input_file:
        model.addMovie(catalog, movie)
        companies = movie["production_companies"].split(",")  # Se obtienen los autores
        for company in companies:
            model.addMovieCompany(catalog, company.strip(), movie)
        genres = movie["genres"].split("|") # Se obtienen los datos de los géneros
        for genre in genres:
            model.addMovieGenre(catalog, genre.strip(), movie)

def loadCasting(catalog, castingfile):
    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader( open(castingfile, encoding="utf-8"), delimiter=";")
    for cast in input_file:
        model.addTag(catalog, cast)
        model.addActor(catalog, cast)


def loadBooksTags(catalog, moviefile):
    """
    Carga la información que asocia tags con libros.
    Primero se localiza el tag y se le agrega la información leida.
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    moviefile = cf.data_dir + moviefile
    input_file = csv.DictReader(open(moviefile, encoding="utf-8"), delimiter=";")
    for movie in input_file:
        model.addBookTag(catalog, movie)
        model.addMovieActor(catalog, movie)
        countries = movie["production_countries"].split(",")  # Se obtienen los paises
        for country in countries:
            model.addMovieCountry(catalog, country.strip(), movie)




def getMoviesByCompany(catalog, companyname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getMoviesByCompany(catalog, companyname)
    return authorinfo


def getMoviesByGenre(catalog, genrename):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getMoviesByGenre(catalog, genrename)
    return authorinfo

def getBooksByTag(catalog, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(catalog, tagname)
    return books

def getMovieByActor(catalog, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getMovieByActor(catalog, tagname)
    return books

def getMoviesByCountry(catalog, companyname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getMoviesByCountry(catalog, companyname)
    return authorinfo



def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])

def companiesSize(catalog):
    tamanio = mp.size(catalog["production_companies"])
    return tamanio

def directorSize(catalog):
    tamanio = mp.size(catalog["director_name"])
    return tamanio

def actorSize(catalog):
    tamanio = mp.size(catalog["actores"])
    return tamanio

def genresSize(catalog):
    tamanio = mp.size(catalog["genres"])
    return tamanio

def countrySize(catalog):
    tamanio = mp.size(catalog["pais"])
    return tamanio









    