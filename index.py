
# Aca va un comentario
#if 3 > 5:
  #  print('esto no se va a imprimir')

#if 5 > 3: # Aca va otro comentario
  #  print('5 es mayor que 3')
# variables
a = 5
b = 'chanchito feliz'
print(a, b)

email = 'chanchitoFeliz.com'

print(email)

_mi_var = 'chanchito'
MIVAR23 = 'chanchito'
x, y, z = 'lala', 'lele', 'lili'

#print(x, y, z)


valor1 = valor2 = valor3 = 'chanchito Feliz'

#print(valor1, valor2, valor3)

inicio = 'hola'
final = 'Mundo'

#print(inicio + final)

#datos
#string
palabra = 'hola mundo'
oracion = "hola mundo comilla doble"

#numeros
entero = 20 #integer
decimales =20.2  #float
complejo = 1j

#print(palabra, oracion, entero, decimales, complejo)

#listas 

lista = ['hola', 'mundo', 'chanchito feliz']
lista2 = lista.copy()
lista.append('chanchito triste')
#lista.clear()

#print(lista , lista2.count(3))
#print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2= len(lista2)

#print(largoLista, largoLista2)

#print(lista[1])

#eliminar datos de una lista 
#lista.pop()
#lista.pop()
#elimina una dato especifico
#lista.remove('hola')

lista.reverse()
# para ordenar una lista tienen que tener los mismos tipos de datos
lista.sort()

#tuplas
tupla = ('hola', 'mundo', 'somos', 'tupla')
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
#print(tupla.count('hola'), tupla.index('hola'), tupla[0], listaDeTupla)

#rangos
rango = range(6)
#print(rango)

#diccionario
diccionario = {
    "nombre": "chanchito feliz",
    "raza": "persa",
    "edad": 5
}
#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario['raza'])
#print(diccionario.get('nombre'))
diccionario['nombre'] = 'fluffly'
#print(len(diccionario))

diccionario['ronronea'] = 'Si'

#print(diccionario)
#diccionario.pop('ronronea')
#diccionario.popitem()
copiaGatito = dict(diccionario) 
#del diccionario['ronronea']
diccionario.clear()
#print(diccionario, copiaGatito)

fluffy ={
        "nombre": "Flully",
        "edad": 4
    }
mamba = {
        "nombre" : "Black Mamba",
        "edad": 12
    }
gatitos = {
    "Flully":fluffy,
    "Mamba":mamba
}

print(gatitos)

perritos = dict(nombre="chanchito feliz", edad=5)
print(perritos)

#booleans

verdadero = True
falso= False


#control de flujos
#if


