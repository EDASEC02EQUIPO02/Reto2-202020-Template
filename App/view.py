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
import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller


assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
moviesfilefull = 'AllMoviesDetailsCleaned.csv'
moviesfile = 'SmallMoviesDetailsCleaned.csv'
castingfile = 'MoviesCastingRaw-small.csv'
castingfilefull = 'AllMoviesCastingRaw.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printCompanyData(author):
    """
    Imprime los libros de un autor determinado
    """
    if author:
        print('Productora encontrada: ' + author['name'])
        print('Promedio: ' + str(round(author['average_rating']/lt.size(author['movies']),3)))
        print('Total de películas: ' + str(lt.size(author['movies'])))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['title'])
    else:
        print('No se encontro la productora')

def printGenreData(author):
    """
    Imprime los libros de un autor determinado
    """
    lista = []
    if author:
        print('Género encontrado: ' + author['name'])
        print('Promedio: ' + str(round(author['average_count']/lt.size(author['movies']),3)))
        print('Total de películas: ' + str(lt.size(author['movies'])))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            lista.append(movie)     
    else:
        print('No se encontro el género')

def printDirectorData(author):
    """
    Imprime los libros de un autor determinado
    """
    lista = []
    if author:
        print('Director encontrado: ' + author['name'])
        print('Promedio: ' + str(round(author['count']/author['total_movies'], 3)))
        print('Total de películas: ' + str(author['total_movies']))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            lista.append(movie)     
        print('La lista de películas del productor: ' + str(lista))
    else:
        print('No se encontro el director')



def printActorData(author):
    """
    Imprime los libros de un autor determinado
    """
    lista = []
    if author:
        print('Actor encontrado: ' + author['name'])
        print('Promedio: ' + str(round(author['count']/author['total_movies'], 3)))
        print('Total de películas: ' + str(author['total_movies']))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            lista.append(movie)     
        print('La lista de películas del productor: ' + str(lista))
    else:
        print('No se encontro el actor')


def printCountryData(author):
    """
    Imprime los libros de un autor determinado
    """
    lista = []
    if author:
        print('País encontrado: ' + author['name'])
        print('Total de películas: ' + str(lt.size(author['movies'])))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['titulo']+ ',' + ' Fecha: ' + str(movie['fecha de lanzamiento'])+ ',' + ' Director: ' + movie['director'])
            #print('Fecha: ' + str(movie['fecha de lanzamiento']))
            #print('Director: ' + movie['director'])
    else:
        print('No se encontro el país')
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar los datos con información")
    print("3- Películas de una productora")
    print("4- Información de un director")
    print("5- Información de un actor")
    print("6- Géneros de una película")
    print("7- Películas a partir de un país")
    print("0- Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, moviesfile, castingfile)
        print('Películas cargadas: ' + str(controller.booksSize(cont)))
        print("Productoras cargados: " + str(controller.companiesSize(cont)))
        print("Directores cargados: " + str(controller.directorSize(cont)))
        print("Actores cargados: " + str(controller.actorSize(cont)))
        print("Géneros cargados: " + str(controller.genresSize(cont)))
        print("Paises cargados: " + str(controller.countrySize(cont)))
    elif int(inputs[0]) == 3:
        nombre = input("Ingrese el nombre de la productora deseada: \n" + ": ")
        companyinfo = controller.getMoviesByCompany(cont, nombre)
        printCompanyData(companyinfo)
    elif int(inputs[0]) == 4:
        name = input("Ingrese el nombre del director: \n" + ": ")
        movies = controller.getBooksByTag(cont, name)
        printDirectorData(movies)
    elif int(inputs[0]) == 5:
        actor = input("ingrese el nombre del actor: \n" + ": ")
        actores = controller.getMovieByActor(cont, actor)
        printActorData(actores)
    elif int(inputs[0]) == 6:
        genero = input("Ingrese el género a buscar: \n" + ": ")
        genreinfo = controller.getMoviesByGenre(cont, genero)
        printGenreData(genreinfo)
    elif int(inputs[0]) == 7:
        pais = input("Ingrese el país a buscar: \n" + ": ")
        countryinfo = controller.getMoviesByCountry(cont, pais)
        printCountryData(countryinfo)
    else:
        sys.exit(0)
sys.exit(0)
