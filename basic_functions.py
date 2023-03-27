import datetime

# Modulo para la creacion de una pelicula en formato json
def create_json_movie():
    cast = []  # Esta variable se utilizara para guardar la lista de actores y actrices

    name = input('Nombre: ')
    director = input('Director: ')

    print(f'Escriba la fecha de emision:\n')
    # Validaremos que la fecha ingresada sea una fecha valida
    while True:
        try:
            year = int(input('Año: '))
            month = int(input('Mes: '))
            day = int(input('Dia: '))
            valid_date = datetime.datetime(year, month, day)
            break
        except ValueError:
            print('Fecha no válida. Intente de nuevo.')

    gender = input('Genero: ')
    # El usuario puede ingresar varios actores por pelicula
    while True:
        validation = input(f'\n¿Desea ingresar un actor o actriz?[s/n] ')
        if validation.lower() == 's':
            pass
        elif validation.lower() == 'n':
            break
        else:
            print(f'\nOpcion invalida. Escriba unicamente "s" o "n"')
            continue
        actor = input(f'\nEscriba nombre y apellido del actor o actriz: ')
        cast.append(actor)
    franchise = input('Franquicia: ')
    country = input('Pais: ')
    clasification = input('Clasificacion: ')
    sinopsis = input('Sinopsis: ')
    release_date = {
        "year": year,
        "month": month,
        "day": day
    }

    movie = {
        "name": name,
        "director": director,
        "release_date": release_date,
        "gender": gender,
        "cast": cast,
        "franchise": franchise,
        "country": country,
        "clasification": clasification,
        "sinopsis": sinopsis
    }

    return movie

# Modulo para la creacion de un objeto json para actualizar una pelicula
def create_json_update_movie():
    menu = '''
    1. Actualizar todo el documento
    2. Modificar solo un elemento del documento
    '''
    print(menu)

    opcion = input(f'\nSeleccione una opcion: ')
    if opcion == '1':
        cast = []  # Esta variable se utilizara para guardar la lista de actores y actrices

        name = input('Nombre: ')
        director = (input('Director: ')).title()

        print(f'Escriba la fecha de emision:\n')
        # Validaremos que la fecha ingresada sea una fecha valida
        while True:
            try:
                year = int(input('Año (formato aaaa): '))
                month = int(input('Mes (formato mm): '))
                day = int(input('Dia (formato dd): '))
                valid_date = datetime.datetime(year, month, day)
                break
            except ValueError:
                print('Fecha no válida. Intente de nuevo.')

        gender = input('Genero:')
        # El usuario puede ingresar varios actores por pelicula
        while True:
            validation = input(f'\n¿Desea ingresar un actor o actriz?[s/n] ')
            if validation.lower() == 's':
                pass
            elif validation.lower() == 'n':
                break
            else:
                print(f'\nOpcion invalida. Escriba unicamente "s" o "n"')
                continue
            actor = input(f'\nEscriba nombre y apellido del actor o actriz: ')
            cast.append(actor)
        franchise = input('Franquicia: ')
        country = input('Pais: ')
        clasification = input('Clasificacion: ')
        sinopsis = input('Sinopsis: ')
        release_date = {
            "year": year,
            "month": month,
            "day": day
        }

        movie = {
            "name": name,
            "director": director,
            "release_date": release_date,
            "gender": gender,
            "cast": cast,
            "franchise": franchise,
            "country": country,
            "clasification": clasification,
            "sinopsis": sinopsis
        }
        return movie

    elif opcion == '2':
        index = input(f'\nIngrese el valor del indice a modificar: ')
        if index.lower() == "release_date":
            print(f'\nIngrese el valor a modificar:\n')
            # Si el valor a modificar es la fecha de emision, se solicitan en el siguiente formato
            while True:
                try:
                    year = int(input('Año (formato aaaa): '))
                    month = int(input('Mes (formato mm): '))
                    day = int(input('Dia (formato dd): '))
                    valid_date = datetime.datetime(year, month, day)
                    value = {
                        "year": year,
                        "month": month,
                        "day": day
                    }
                    movie = {index: value}
                    break
                except ValueError:
                    print('Fecha no válida. Intente de nuevo.')
# Como el programa se diseño para ingresar varios actores y actrices, se hace la consulta
        elif index.lower() == "cast":
            cast = []
            while True:
                validation = input(f'\n¿Desea ingresar un actor o actriz?[s/n] ')
                if validation.lower() == 's':
                    pass
                elif validation.lower() == 'n':
                    break
                else:
                    print(f'\nOpcion invalida. Escriba unicamente "s" o "n"')
                    continue
                actor = input(f'\nEscriba nombre y apellido del actor o actriz: ')
                cast.append(actor)
            movie = {index: cast}
        else:
            value = input(f'\nIngrese el valor a modificar: ')
            movie = {index: value}
        return movie