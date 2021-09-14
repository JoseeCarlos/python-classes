# c = open('chanchito.txt','w')

# # for x in c:
# #     print(x)

# c.write('\nagregaremos una nueva line en este txt')

# c.close()

# x = open('chanchito.txt')

# print(x.read())

import os

if(os.path.exists('chanchito.txt')):
    os.remove('chanchito.txt')
else:
    print('el archivo no existe')


os.rmdir('micarpeta')

