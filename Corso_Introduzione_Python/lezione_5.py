'''
DATA TYPES

1.Strings
2.Numbers
3.Bool
4.List
5.Set
6.Dict
'''

# NESTED LISTS

lista2 = ['a','b','c']
lista = [0,1,2,3,4,5,6,7,8,9,10, lista2]
print(lista)

print('******************')

lista3 = ['d','e','f']
lista0 = [lista2, lista3]
print(lista0)

lista4 = []
print(lista4)

for i in lista0:
    #print(i)
    for j in i:
        lista4.append(j)

print(lista4)

