'''
DATA TYPES

1.Strings
2.Numbers
3.Bool
4.List
5.Set
6.Dict
'''

lista1 = ['a','b','c']
lista2 = ['d','e','f']

lista1.extend(lista2)
lista1.append('xxx')
lista1.append([1,2,3]) # APPEND aggiunge una nuova lista all'interno di una esistente, nidificandola
lista1.extend([1,2,3]) # EXTEND aggiunge elementi di una lista all'interno di un'altra
print(lista1)
