import json
import datetime
from conection_parameters import collection

# Modulo para leer peliculas
def read_movies(name=None):
    # Se declaran dos menus que se utilizaran dentro de modulo
    menu_1 = '''
    1. Consultar todas las peliculas registradas
    2. Consultar y filtrar las peliculas por fecha de emision
    '''
    menu_2 = '''
    1. Filtrar por fecha completa
    2. Filtrar por año
    '''
    if name is not None:
        query = {"name" : name}
        document = collection.find_one(query)
        if document == None:
            # Si no se encuentra la pelicula, podria no existir en la base o el nombre encontrarse mal escrito
            print(f'\nLa pelicula "{name}" no se encuentra en la base de datos.\nAsegurese que el nombre este escrito tal como se ingreso,\nrespetando mayusculas y minisculas')
        else:
            print(f'\n{document}\n')
    else:
        # El sistema mostrara el menu para consultar si se desean filtrar todas las peliculas por una fecha o año especifico
        print(f'\n{menu_1}')
        opcion = input(f'\nSeleccione una opcion: ')
        if opcion == '1':
            documents = collection.find()
            for document in documents:
                print(f'\n{document}\n')
        elif opcion == '2':
            print(menu_2)
            filtro = input(f'\nSeleccione una opcion: ')
            if filtro == '1':
                # Si se desea ingresar la fecha completa se debe leer con el formato siguiente
                while True:
                    try:
                        year = int(input('Año: '))
                        month = int(input('Mes: '))
                        day = int(input('Dia: '))
                        valid_date = datetime.datetime(year, month, day)
                        break
                    except ValueError:
                        print('Fecha no válida. Intente de nuevo.')
                documents = collection.find({"release_date":{"year" : year, "month" : month, "day" : day}})
                counter = collection.count_documents({"release_date":{"year" : year, "month" : month, "day" : day}})
                if counter == 0:
                    print(f'\nNo hay peliculas estrenadas en la fecha: {day}-{month}-{year}\n')
                else:
                    for document in documents:
                        print(f'\n{document}')
            elif filtro == '2':
                year = int(input('Año: '))
                documents = collection.find({"release_date.year": year})
                counter = collection.count_documents({"release_date.year": year})
                if counter == 0:
                    print(f'\nNo hay peliculas estrenadas en el año: {year}\n')
                else:
                    for document in documents:
                        print(f'\n{document}')

# Modulo para la creacion de una nueva pelicula
def create_movie(movie):
    result = collection.insert_one(movie)
    print(f'\nEl id insertado es: {result.inserted_id}')

# Modulo para actualizar una pelicula
def update_movie(name, json_index_values):
    query = {"name" : name}
    new_value = {"$set" : json_index_values}
    result = collection.update_one(query, new_value)
    print(f'El indice modificado fue: {result.modified_count}')

# Modulo para borrar una pelicula
def delete_movie(name=None):
    if name is not None:
        query = {"name" : name}
        result = collection.delete_one(query)
        if result.deleted_count == 0:
            # Se valida si se elimino una pelicula, si no, el sistema muestra el mensaje de error
            print(f'\nLa pelicula "{name}" no se encuentra en la base de datos.\nAsegurese que el nombre este escrito tal como se ingreso,\nrespetando mayusculas y minisculas')
        else:
            print(f'\nSe ha eliminado la pelicula "{name}" exitosamente!\n')
            print(f'\nPeliculas borradas: {result.deleted_count}\n')