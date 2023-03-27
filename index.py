from crud import *
from basic_functions import *
menu = '''
###############  MENU  #################
#             |Bienvenido|             #
#                                      #
# 1. Consultar todas las peliculas     #
# 2. Consultar una pelicula            #
# 3. Agregar pelicula                  #
# 4. Actualizar pelicula               #
# 5. Borrar pelicula                   #  
#                                      #
# 6. Salir del programa                #
#                                      #
########################################
'''
while True:
    print(menu)
    opcion = input(f'\nSeleccione una opcion: ')
    if opcion == '1':
        read_movies()
    elif opcion == '2':
        name = input(f'\nIngrese el nombre de la pelicula a buscar: ')
        read_movies(name)
    elif opcion == '3':
        print(f'\nIngrese los datos de la nueva pelicula: ')
        movie = create_json_movie()
        create_movie(movie)
    elif opcion == '4':
        name = input(f'\nIngrese el nombre de la pelicula que desea modificar: ')
        movie = create_json_update_movie()
        update_movie(name, movie)
    elif opcion == '5':
        name = input(f'\nDigite el nombre de la pelicula que desea borrar: ')
        delete_movie(name)
    elif opcion == '6':
        print(f'\nSaliendo del sistema...\nHasta la proxima!\n')
        break