#dato = input('ingrese un dato: ')

#lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']


#if lista.count(dato) > 0:
 #   print('el dato existe', dato)
#else: print('el dato no existe', dato)

numero1 = input('ingrese un numero: ')

try:
    numero1 = int(numero1)
except:
    numero1 = 'chanchito feliz'

if numero1=='chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

numero2 = input('ingrese un numero: ')

try:
    numero2 = int(numero2)
except:
    numero2 = 'chanchito feliz'

if numero2=='chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

simbolo = input('ingrese el simbolo de la operacion')

if simbolo == '+':
 print(numero1+numero2)
elif simbolo =='-':
    print(numero1-numero2)
elif simbolo == '*':
    print(numero1*numero2)
elif simbolo == '/':
    print(numero1/numero2)
else: print('valor ingresado no valido')



