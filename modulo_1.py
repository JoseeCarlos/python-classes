# from modulos import saludo, mascotas 
from camelcase import CamelCase

# print(mascotas)
# saludo('jose')

c = CamelCase()
s = 'esta oracion necesita Camelcase'
camelcased = c.hump(s)
print(camelcased)