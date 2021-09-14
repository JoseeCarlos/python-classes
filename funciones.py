def miFuncion():
    print('Mi primera funcion')

#
# miFuncion()

def imprimeDato(*nombre):
    print('El nombre completo es ', nombre[0])

#imprimeDato('holaaa','holaa','lelel')


def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='chanchito',apellido='feliz')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

nombreCompleto2(nombre='chanchito',apellido='feliz')

def miFuncion2(argumento='chanchito'):
    print(argumento)


# miFuncion2('batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['chanchito','Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i

hola =concatenaNombres(['chanchito','feliz'])
# print(hola)




def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i-1)

recursion(6)