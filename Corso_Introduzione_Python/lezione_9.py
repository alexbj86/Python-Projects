'''
DATA TYPES

1.Strings
2.Numbers
3.Bool
4.List
5.Set
    6.Dict
7.Tuple
'''

# DIZIONARI
dizionario = {}

#chiave, valore

dizionario = {'nome': 'mario', 'cognome': 'rossi'}
print(dizionario)
print('#########################')
#STAMPA SOLO IL NOME
print(dizionario['nome'])
print('#########################')
#SOSTITUZIONE NOME
dizionario['nome'] = 'giuseppe'
print(dizionario)
print('#########################')
#STAMPA K,V ITEMS
for k,v in dizionario.items():
    print('key: '+k, 'valore: '+v)
print('#########################')
#STAMPA SOLO VALORE
for k,v in dizionario.items():
    print('valore '+v)
print('#########################')
#STAMPA CHIAVI
for el in dizionario.keys():
    print('chiave ' + el)
print('#########################')
#STAMPA VALORE
for el in dizionario.values():
    print('valore: ' + el)
