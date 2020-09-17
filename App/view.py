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
castingfile = 'Data/MoviesCastingRaw-small.csv'


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
        print('Promedio: ' + str(author['average_rating']))
        print('Total de películas: ' + str(lt.size(author['movies'])))
        iterator = it.newIterator(author['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['title'])
    else:
        print('No se encontro la productora')


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar los datos con información")
    print("3- Opcion algo...")
    print("4- Películas de una productora")
    print("5- ")
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
        controller.loadData(cont, moviesfilefull)
        print('Películas cargadas: ' + str(controller.booksSize(cont)))
        print("Directores cargados: " + str(controller.companiesSize(cont)))
    elif int(inputs[0]) == 3:
        lista1=controller.loadMovies1(moviesfile)
        lista2=controller.loadCasting(castingfile)
        numero= controller.numeroPeliculas(lista1)
        primeraPelicula= controller.primeraPelicula(l<ista1)
        ultimaPelicula= controller.ultimaPelicula(lista1)
        fechaEstrenoP=controller.fechaEstrenoP(lista1)
        fechaEstrenoU=controller.fechaEstrenoU(lista1)
        promP=controller.promP(lista1)
        promU=controller.promU(lista1)
        votP=controller.votP(lista1)
        votU=controller.votU(lista1)
        idiomaP=controller.idiomaP(lista1)
        idiomaU=controller.idiomaU(lista1)
        print("\nEl número de películas es: " + str(numero))
        print("\nLa primera película es: " + primeraPelicula)
        print("La fecha de estreno es: " + fechaEstrenoP)
        print("El promedio de la votación fue: " + str(promP))
        print("El número de votos fue: " + str(votP))
        print("El idioma es: " + idiomaP)
        print("\nLa última película es: " + ultimaPelicula)
        print("La fecha de estreno es: " + fechaEstrenoU)
        print("El promedio de la votación fue: " + str(promU))
        print("El número de votos fue: " + str(votU))
        print("El idioma es: " + idiomaU+"\n")
    elif int(inputs[0]) == 4:
        nombre = input("Ingrese el nombre de la productora deseada: \n" + ": ")
        companyinfo = controller.getMoviesByCompany(cont, nombre)
        printCompanyData(companyinfo)
    else:
        sys.exit(0)
sys.exit(0)
