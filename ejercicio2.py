#multiplicar sin signo 
a = 4
b = 8
res = 0


for x in range(b):
    res=res+a

print(res)

# ingresa nombre y apellido y imprimilo al reves

nombre = 'Nicolas'
apellido = 'Feliz'

concatenacion= nombre+ ' '+ apellido

print(concatenacion[::-1])

# el menor numero de uina lista

lista = [1, 2, 3, 4, 6, 5, 55, -24, -13]


menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)


# escribir una funcion que devuelva el volumen de una esfera por su radio 

def CalcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3 


resultado = CalcularVolumen(6)

print(resultado)

#escribir una funcion que indique el usuario es mayor de edad 

def VerificarEdad(edad):
    if edad < 18:
        print(' es menor de edad')
    else:
        print(' es mayor de edad')

VerificarEdad(18)

# escribir una funcion que indiqque si un numero es par o impar

def esPar(n):
    return n % 2 == 0


res=esPar(10)

print(res)

#escribit cuantas vocales tiene una palabra 

palabra= 'chanchitofeliz'

vocales = 0

for x in palabra:
   y = x.lower()
   vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocales)

#escribir un programa que reciba un cantidad infinita de numeros hastas decir basta 

lista = []

print('ingrese numeros y para salir escriba basta')

while True:
    valor = input('ingrese un numero')
    if valor == 'basta':
        break
    else:
        try: 
            valor = int(valor)
            lista.append(valor)
        except:
            print('dato invalido')
            exit()

resultado = 0;

for x in lista:
    resultado += x


print(resultado)

# escribit una funcion que resiba un nombre y un apellido y los agrege a un archivo

def agregaNombreArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre+ ' '+ apellido+ '\n')
    c.close()

agregaNombreArchivo('jose','carlos')
