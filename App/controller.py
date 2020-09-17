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

def loadData(catalog, moviefile):
    """
    Carga los datos de los archivos en el modelo
    """
    t1 = process_time()
    loadMovies(catalog, moviefile)
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



def getMoviesByCompany(catalog, companyname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getMoviesByCompany(catalog, companyname)
    return authorinfo






def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])

def companiesSize(catalog):
    tamanio = mp.size(catalog["production_companies"])
    return tamanio

















def loadMovies1(dato1):
    lst = model.loadCSVFile(dato1, model.compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting(dato2):
    lst = model.loadCSVFile(dato2, model.compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def numeroPeliculas(lista1):
    numero=model.numeroPeliculas(lista1)
    return numero

def primeraPelicula(lista1):
    peliculaP=model.primeraPelicula(lista1)
    return peliculaP

def ultimaPelicula(lista1):
    peliculaU=model.ultimaPelicula(lista1)
    return peliculaU

def fechaEstrenoP(lista1):
    fechaU=model.fechaEstrenoP(lista1)
    return fechaU

def fechaEstrenoU(lista1):
    fechaP=model.fechaEstrenoU(lista1)
    return fechaP

def promP(lista1):
    promP=model.promP(lista1)
    return promP

def promU(lista1):
    promU=model.promU(lista1)
    return promU

def votP(lista1):
    votP=model.votP(lista1)
    return votP

def votU(lista1):
    votU=model.votU(lista1)
    return votU

def idiomaP(lista1):
    idiomaP=model.idiomaP(lista1)
    return idiomaP

def idiomaU(lista1):
    idiomaU=model.idiomaU(lista1)
    return idiomaU
    