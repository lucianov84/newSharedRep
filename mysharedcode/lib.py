import sys

def try_me(sed = 'poca'):
    """"
    funcion de prueba para compartir en el bootcamp
    """

    if sed == 'poca':
        return 'si tenes poca sed, tomate solo una cerveza'

    return 'si tenes mucha sed, tomate mas de una ;-)'


if __name__ == '__main__':

    print(try_me(sys.argv[1]))
